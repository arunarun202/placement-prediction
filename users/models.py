from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)



    
class Chatbot(models.Model):
    message = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.message


class UserPredictModel1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # ✔ Add this

    Age = models.FloatField()
    Gender = models.CharField(max_length=20)
    Qualification = models.CharField(max_length=50)
    year = models.FloatField()
    cgpa = models.FloatField()
    Job_Role = models.CharField(max_length=50)
    Post_Graduation = models.CharField(max_length=20)
    ten_Percentage = models.FloatField()
    twelth_Percentage = models.FloatField()
    Salary = models.FloatField()
    Soft_Skills = models.CharField(max_length=50)
    Internship = models.CharField(max_length=50)
    Experience = models.FloatField()
    Round = models.IntegerField()
    Company_Name = models.CharField(max_length=100)
    label = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)







class ResumeUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # ✔ Add this

    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    job_role = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='resumes/')
    processed = models.BooleanField(default=False)
    ats_score = models.FloatField(blank=True, null=True)
    gemini_response = models.JSONField(blank=True, null=True)
    suggestions = models.TextField(blank=True, null=True)
    course_products = models.JSONField(blank=True, null=True)
    alternative_roles = models.JSONField(blank=True, null=True)
    role_courses = models.JSONField(blank=True, null=True)

