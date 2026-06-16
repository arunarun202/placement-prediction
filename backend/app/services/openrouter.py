import json
import httpx
from fastapi import HTTPException
from app.core.config import settings

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "meta-llama/llama-3-8b-instruct:free"

async def _call_openrouter(messages: list, response_format: dict = None) -> str:
    if not settings.OPENROUTER_API_KEY:
        raise HTTPException(status_code=500, detail="OpenRouter API key is missing")

    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "Placement Predictor",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": DEFAULT_MODEL,
        "messages": messages,
    }
    if response_format:
        payload["response_format"] = response_format

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(OPENROUTER_URL, headers=headers, json=payload, timeout=60.0)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            raise HTTPException(status_code=502, detail=f"Error communicating with OpenRouter: {str(e)}")

async def predict_placement(stats: dict) -> str:
    prompt = f"""
    You are a career prediction AI. Based on the following user statistics, provide a prediction for their placement.
    Return a concise label like "High Probability", "Medium Probability", or "Low Probability", followed by a short explanation.
    
    Stats:
    {json.dumps(stats, indent=2)}
    """
    messages = [
        {"role": "system", "content": "You are a professional career advisor."},
        {"role": "user", "content": prompt}
    ]
    return await _call_openrouter(messages)

async def evaluate_resume(resume_text: str, job_role: str) -> dict:
    prompt = f"""
    You are an ATS (Applicant Tracking System) expert. Evaluate the following resume for the role of '{job_role}'.
    Provide the response strictly as a JSON object with the following keys:
    - "ats_score": A number between 0 and 100 representing the match score.
    - "suggestions": A string containing actionable feedback.
    - "course_products": A list of strings of recommended courses.
    - "alternative_roles": A list of strings of other roles they could apply for.
    - "role_courses": A list of strings with specific courses for the current role.
    
    Resume Text:
    {resume_text[:4000]}  # limit text just in case
    """
    messages = [
        {"role": "system", "content": "You are an ATS parser and career coach. Respond strictly in JSON."},
        {"role": "user", "content": prompt}
    ]
    # some models support response_format={"type": "json_object"}, but we'll try without strict enforcement
    response_text = await _call_openrouter(messages)
    
    try:
        # Try to parse the JSON output from the LLM
        # Sometimes LLMs wrap JSON in ```json ... ```
        clean_text = response_text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_text)
    except Exception:
        # fallback
        return {
            "ats_score": 50,
            "suggestions": "Failed to parse AI response. " + response_text,
            "course_products": [],
            "alternative_roles": [],
            "role_courses": []
        }

async def chat_response(history_messages: list, new_message: str) -> str:
    # Format history for OpenRouter
    messages = [{"role": "system", "content": "You are a helpful placement prediction assistant chatbot."}]
    for msg in history_messages:
        messages.append({"role": "user", "content": msg})
    
    messages.append({"role": "user", "content": new_message})
    
    return await _call_openrouter(messages)
