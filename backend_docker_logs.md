2026-06-16 10:33:03.257 | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2026-06-16 10:33:03.257 | INFO  [alembic.runtime.migration] Will assume transactional DDL.
2026-06-16 10:33:03.950 | 
2026-06-16 10:33:03.951 |    FastAPI   Starting production server 🚀
2026-06-16 10:33:03.951 |  
2026-06-16 10:33:03.952 |              Searching for package file structure from directories with         
2026-06-16 10:33:03.952 |              __init__.py files                                                  
2026-06-16 10:33:03.953 | ERROR    Import error: No module named 'app'                                    
2026-06-16 10:33:03.954 | WARNING  Ensure all the package directories have an __init__.py file            
2026-06-16 10:33:03.954 | 
2026-06-16 10:33:04.019 | ╭───────────────────── Traceback (most recent call last) ──────────────────────╮
2026-06-16 10:33:04.019 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:435 in run        │
2026-06-16 10:33:04.019 | │                                                                              │
2026-06-16 10:33:04.019 | │   432 │                                                                      │
2026-06-16 10:33:04.019 | │   433 │   Otherwise, it uses the first [bold]FastAPI[/bold] app found in the │
2026-06-16 10:33:04.019 | │       imported module or package.                                            │
2026-06-16 10:33:04.019 | │   434 │   """                                                                │
2026-06-16 10:33:04.019 | │ ❱ 435 │   _run(                                                              │
2026-06-16 10:33:04.019 | │   436 │   │   path=path,                                                     │
2026-06-16 10:33:04.019 | │   437 │   │   host=host,                                                     │
2026-06-16 10:33:04.019 | │   438 │   │   port=port,                                                     │
2026-06-16 10:33:04.019 | │                                                                              │
2026-06-16 10:33:04.019 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:152 in _run       │
2026-06-16 10:33:04.019 | │                                                                              │
2026-06-16 10:33:04.019 | │   149 │   │   try:                                                           │
2026-06-16 10:33:04.019 | │   150 │   │   │   # Resolve import data with priority: CLI path/app > config │
2026-06-16 10:33:04.019 | │       entrypoint > auto-discovery                                            │
2026-06-16 10:33:04.019 | │   151 │   │   │   if path or app:                                            │
2026-06-16 10:33:04.019 | │ ❱ 152 │   │   │   │   import_data = get_import_data(path=path, app_name=app) │
2026-06-16 10:33:04.019 | │   153 │   │   │   elif config.entrypoint:                                    │
2026-06-16 10:33:04.019 | │   154 │   │   │   │   import_data =                                          │
2026-06-16 10:33:04.019 | │       get_import_data_from_import_string(config.entrypoint)                  │
2026-06-16 10:33:04.019 | │   155 │   │   │   else:                                                      │
2026-06-16 10:33:04.019 | │                                                                              │
2026-06-16 10:33:04.019 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:125 in       │
2026-06-16 10:33:04.019 | │ get_import_data                                                              │
2026-06-16 10:33:04.019 | │                                                                              │
2026-06-16 10:33:04.019 | │   122 │   │   raise FastAPICLIException(f"Path does not exist {path}")       │
2026-06-16 10:33:04.019 | │   123 │   mod_data = get_module_data_from_path(path)                         │
2026-06-16 10:33:04.019 | │   124 │   sys.path.insert(0, str(mod_data.extra_sys_path))                   │
2026-06-16 10:33:04.019 | │ ❱ 125 │   use_app_name = get_app_name(mod_data=mod_data, app_name=app_name)  │
2026-06-16 10:33:04.019 | │   126 │                                                                      │
2026-06-16 10:33:04.019 | │   127 │   import_string = f"{mod_data.module_import_str}:{use_app_name}"     │
2026-06-16 10:33:04.019 | │   128                                                                        │
2026-06-16 10:33:04.019 | │                                                                              │
2026-06-16 10:33:04.019 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:69 in        │
2026-06-16 10:33:04.019 | │ get_app_name                                                                 │
2026-06-16 10:33:04.019 | │                                                                              │
2026-06-16 10:33:04.019 | │    66                                                                        │
2026-06-16 10:33:04.019 | │    67 def get_app_name(*, mod_data: ModuleData, app_name: str | None = None) │
2026-06-16 10:33:04.019 | │       -> str:                                                                │
2026-06-16 10:33:04.019 | │    68 │   try:                                                               │
2026-06-16 10:33:04.019 | │ ❱  69 │   │   mod = importlib.import_module(mod_data.module_import_str)      │
2026-06-16 10:33:04.019 | │    70 │   except (ImportError, ValueError) as e:                             │
2026-06-16 10:33:04.019 | │    71 │   │   logger.error(f"Import error: {e}")                             │
2026-06-16 10:33:04.019 | │    72 │   │   logger.warning(                                                │
2026-06-16 10:33:04.019 | │                                                                              │
2026-06-16 10:33:04.019 | │ /usr/local/lib/python3.11/importlib/__init__.py:126 in import_module         │
2026-06-16 10:33:04.019 | │                                                                              │
2026-06-16 10:33:04.019 | │   123 │   │   │   if character != '.':                                       │
2026-06-16 10:33:04.019 | │   124 │   │   │   │   break                                                  │
2026-06-16 10:33:04.019 | │   125 │   │   │   level += 1                                                 │
2026-06-16 10:33:04.019 | │ ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)        │
2026-06-16 10:33:04.019 | │   127                                                                        │
2026-06-16 10:33:04.019 | │   128                                                                        │
2026-06-16 10:33:04.019 | │   129 _RELOADING = {}                                                        │
2026-06-16 10:33:04.019 | │ in _gcd_import:1204                                                          │
2026-06-16 10:33:04.019 | │ in _find_and_load:1176                                                       │
2026-06-16 10:33:04.019 | │ in _find_and_load_unlocked:1147                                              │
2026-06-16 10:33:04.019 | │ in _load_unlocked:690                                                        │
2026-06-16 10:33:04.019 | │ in exec_module:940                                                           │
2026-06-16 10:33:04.019 | │ in _call_with_frames_removed:241                                             │
2026-06-16 10:33:04.019 | │                                                                              │
2026-06-16 10:33:04.019 | │ /app/app/main.py:4 in <module>                                               │
2026-06-16 10:33:04.019 | │                                                                              │
2026-06-16 10:33:04.019 | │    1 from fastapi import FastAPI                                             │
2026-06-16 10:33:04.019 | │    2 from fastapi.middleware.cors import CORSMiddleware                      │
2026-06-16 10:33:04.019 | │    3                                                                         │
2026-06-16 10:33:04.019 | │ ❱  4 from app.core.config import settings                                    │
2026-06-16 10:33:04.019 | │    5 from app.api import auth, predict, resume, chat                         │
2026-06-16 10:33:04.019 | │    6                                                                         │
2026-06-16 10:33:04.019 | │    7 app = FastAPI(                                                          │
2026-06-16 10:33:04.019 | ╰──────────────────────────────────────────────────────────────────────────────╯
2026-06-16 10:33:04.019 | ModuleNotFoundError: No module named 'app'
2026-06-16 10:33:04.984 | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2026-06-16 10:33:04.984 | INFO  [alembic.runtime.migration] Will assume transactional DDL.
2026-06-16 10:33:05.685 | 
2026-06-16 10:33:05.686 |    FastAPI   Starting production server 🚀
2026-06-16 10:33:05.686 |  
2026-06-16 10:33:05.686 |              Searching for package file structure from directories with         
2026-06-16 10:33:05.686 |              __init__.py files                                                  
2026-06-16 10:33:05.688 | ERROR    Import error: No module named 'app'                                    
2026-06-16 10:33:05.688 | WARNING  Ensure all the package directories have an __init__.py file            
2026-06-16 10:33:05.688 | 
2026-06-16 10:33:05.753 | ╭───────────────────── Traceback (most recent call last) ──────────────────────╮
2026-06-16 10:33:05.753 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:435 in run        │
2026-06-16 10:33:05.753 | │                                                                              │
2026-06-16 10:33:05.753 | │   432 │                                                                      │
2026-06-16 10:33:05.753 | │   433 │   Otherwise, it uses the first [bold]FastAPI[/bold] app found in the │
2026-06-16 10:33:05.753 | │       imported module or package.                                            │
2026-06-16 10:33:05.753 | │   434 │   """                                                                │
2026-06-16 10:33:05.753 | │ ❱ 435 │   _run(                                                              │
2026-06-16 10:33:05.753 | │   436 │   │   path=path,                                                     │
2026-06-16 10:33:05.753 | │   437 │   │   host=host,                                                     │
2026-06-16 10:33:05.753 | │   438 │   │   port=port,                                                     │
2026-06-16 10:33:05.753 | │                                                                              │
2026-06-16 10:33:05.753 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:152 in _run       │
2026-06-16 10:33:05.753 | │                                                                              │
2026-06-16 10:33:05.753 | │   149 │   │   try:                                                           │
2026-06-16 10:33:05.753 | │   150 │   │   │   # Resolve import data with priority: CLI path/app > config │
2026-06-16 10:33:05.753 | │       entrypoint > auto-discovery                                            │
2026-06-16 10:33:05.753 | │   151 │   │   │   if path or app:                                            │
2026-06-16 10:33:05.753 | │ ❱ 152 │   │   │   │   import_data = get_import_data(path=path, app_name=app) │
2026-06-16 10:33:05.753 | │   153 │   │   │   elif config.entrypoint:                                    │
2026-06-16 10:33:05.753 | │   154 │   │   │   │   import_data =                                          │
2026-06-16 10:33:05.753 | │       get_import_data_from_import_string(config.entrypoint)                  │
2026-06-16 10:33:05.753 | │   155 │   │   │   else:                                                      │
2026-06-16 10:33:05.753 | │                                                                              │
2026-06-16 10:33:05.753 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:125 in       │
2026-06-16 10:33:05.753 | │ get_import_data                                                              │
2026-06-16 10:33:05.753 | │                                                                              │
2026-06-16 10:33:05.753 | │   122 │   │   raise FastAPICLIException(f"Path does not exist {path}")       │
2026-06-16 10:33:05.753 | │   123 │   mod_data = get_module_data_from_path(path)                         │
2026-06-16 10:33:05.753 | │   124 │   sys.path.insert(0, str(mod_data.extra_sys_path))                   │
2026-06-16 10:33:05.753 | │ ❱ 125 │   use_app_name = get_app_name(mod_data=mod_data, app_name=app_name)  │
2026-06-16 10:33:05.753 | │   126 │                                                                      │
2026-06-16 10:33:05.753 | │   127 │   import_string = f"{mod_data.module_import_str}:{use_app_name}"     │
2026-06-16 10:33:05.753 | │   128                                                                        │
2026-06-16 10:33:05.753 | │                                                                              │
2026-06-16 10:33:05.753 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:69 in        │
2026-06-16 10:33:05.753 | │ get_app_name                                                                 │
2026-06-16 10:33:05.753 | │                                                                              │
2026-06-16 10:33:05.753 | │    66                                                                        │
2026-06-16 10:33:05.753 | │    67 def get_app_name(*, mod_data: ModuleData, app_name: str | None = None) │
2026-06-16 10:33:05.753 | │       -> str:                                                                │
2026-06-16 10:33:05.753 | │    68 │   try:                                                               │
2026-06-16 10:33:05.753 | │ ❱  69 │   │   mod = importlib.import_module(mod_data.module_import_str)      │
2026-06-16 10:33:05.753 | │    70 │   except (ImportError, ValueError) as e:                             │
2026-06-16 10:33:05.753 | │    71 │   │   logger.error(f"Import error: {e}")                             │
2026-06-16 10:33:05.753 | │    72 │   │   logger.warning(                                                │
2026-06-16 10:33:05.753 | │                                                                              │
2026-06-16 10:33:05.753 | │ /usr/local/lib/python3.11/importlib/__init__.py:126 in import_module         │
2026-06-16 10:33:05.753 | │                                                                              │
2026-06-16 10:33:05.753 | │   123 │   │   │   if character != '.':                                       │
2026-06-16 10:33:05.753 | │   124 │   │   │   │   break                                                  │
2026-06-16 10:33:05.753 | │   125 │   │   │   level += 1                                                 │
2026-06-16 10:33:05.753 | │ ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)        │
2026-06-16 10:33:05.753 | │   127                                                                        │
2026-06-16 10:33:05.753 | │   128                                                                        │
2026-06-16 10:33:05.753 | │   129 _RELOADING = {}                                                        │
2026-06-16 10:33:05.753 | │ in _gcd_import:1204                                                          │
2026-06-16 10:33:05.753 | │ in _find_and_load:1176                                                       │
2026-06-16 10:33:05.753 | │ in _find_and_load_unlocked:1147                                              │
2026-06-16 10:33:05.753 | │ in _load_unlocked:690                                                        │
2026-06-16 10:33:05.753 | │ in exec_module:940                                                           │
2026-06-16 10:33:05.753 | │ in _call_with_frames_removed:241                                             │
2026-06-16 10:33:05.753 | │                                                                              │
2026-06-16 10:33:05.753 | │ /app/app/main.py:4 in <module>                                               │
2026-06-16 10:33:05.753 | │                                                                              │
2026-06-16 10:33:05.753 | │    1 from fastapi import FastAPI                                             │
2026-06-16 10:33:05.753 | │    2 from fastapi.middleware.cors import CORSMiddleware                      │
2026-06-16 10:33:05.753 | │    3                                                                         │
2026-06-16 10:33:05.753 | │ ❱  4 from app.core.config import settings                                    │
2026-06-16 10:33:05.753 | │    5 from app.api import auth, predict, resume, chat                         │
2026-06-16 10:33:05.753 | │    6                                                                         │
2026-06-16 10:33:05.753 | │    7 app = FastAPI(                                                          │
2026-06-16 10:33:05.753 | ╰──────────────────────────────────────────────────────────────────────────────╯
2026-06-16 10:33:05.753 | ModuleNotFoundError: No module named 'app'
2026-06-16 10:33:06.789 | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2026-06-16 10:33:06.789 | INFO  [alembic.runtime.migration] Will assume transactional DDL.
2026-06-16 10:33:07.480 | 
2026-06-16 10:33:07.481 |    FastAPI   Starting production server 🚀
2026-06-16 10:33:07.481 |  
2026-06-16 10:33:07.481 |              Searching for package file structure from directories with         
2026-06-16 10:33:07.481 |              __init__.py files                                                  
2026-06-16 10:33:07.483 | ERROR    Import error: No module named 'app'                                    
2026-06-16 10:33:07.483 | WARNING  Ensure all the package directories have an __init__.py file            
2026-06-16 10:33:07.483 | 
2026-06-16 10:33:07.546 | ╭───────────────────── Traceback (most recent call last) ──────────────────────╮
2026-06-16 10:33:07.546 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:435 in run        │
2026-06-16 10:33:07.546 | │                                                                              │
2026-06-16 10:33:07.546 | │   432 │                                                                      │
2026-06-16 10:33:07.546 | │   433 │   Otherwise, it uses the first [bold]FastAPI[/bold] app found in the │
2026-06-16 10:33:07.546 | │       imported module or package.                                            │
2026-06-16 10:33:07.546 | │   434 │   """                                                                │
2026-06-16 10:33:07.546 | │ ❱ 435 │   _run(                                                              │
2026-06-16 10:33:07.546 | │   436 │   │   path=path,                                                     │
2026-06-16 10:33:07.546 | │   437 │   │   host=host,                                                     │
2026-06-16 10:33:07.546 | │   438 │   │   port=port,                                                     │
2026-06-16 10:33:07.546 | │                                                                              │
2026-06-16 10:33:07.546 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:152 in _run       │
2026-06-16 10:33:07.546 | │                                                                              │
2026-06-16 10:33:07.546 | │   149 │   │   try:                                                           │
2026-06-16 10:33:07.546 | │   150 │   │   │   # Resolve import data with priority: CLI path/app > config │
2026-06-16 10:33:07.546 | │       entrypoint > auto-discovery                                            │
2026-06-16 10:33:07.546 | │   151 │   │   │   if path or app:                                            │
2026-06-16 10:33:07.546 | │ ❱ 152 │   │   │   │   import_data = get_import_data(path=path, app_name=app) │
2026-06-16 10:33:07.546 | │   153 │   │   │   elif config.entrypoint:                                    │
2026-06-16 10:33:07.546 | │   154 │   │   │   │   import_data =                                          │
2026-06-16 10:33:07.546 | │       get_import_data_from_import_string(config.entrypoint)                  │
2026-06-16 10:33:07.546 | │   155 │   │   │   else:                                                      │
2026-06-16 10:33:07.546 | │                                                                              │
2026-06-16 10:33:07.546 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:125 in       │
2026-06-16 10:33:07.546 | │ get_import_data                                                              │
2026-06-16 10:33:07.546 | │                                                                              │
2026-06-16 10:33:07.546 | │   122 │   │   raise FastAPICLIException(f"Path does not exist {path}")       │
2026-06-16 10:33:07.546 | │   123 │   mod_data = get_module_data_from_path(path)                         │
2026-06-16 10:33:07.546 | │   124 │   sys.path.insert(0, str(mod_data.extra_sys_path))                   │
2026-06-16 10:33:07.546 | │ ❱ 125 │   use_app_name = get_app_name(mod_data=mod_data, app_name=app_name)  │
2026-06-16 10:33:07.546 | │   126 │                                                                      │
2026-06-16 10:33:07.546 | │   127 │   import_string = f"{mod_data.module_import_str}:{use_app_name}"     │
2026-06-16 10:33:07.546 | │   128                                                                        │
2026-06-16 10:33:07.546 | │                                                                              │
2026-06-16 10:33:07.546 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:69 in        │
2026-06-16 10:33:07.546 | │ get_app_name                                                                 │
2026-06-16 10:33:07.546 | │                                                                              │
2026-06-16 10:33:07.546 | │    66                                                                        │
2026-06-16 10:33:07.546 | │    67 def get_app_name(*, mod_data: ModuleData, app_name: str | None = None) │
2026-06-16 10:33:07.546 | │       -> str:                                                                │
2026-06-16 10:33:07.546 | │    68 │   try:                                                               │
2026-06-16 10:33:07.546 | │ ❱  69 │   │   mod = importlib.import_module(mod_data.module_import_str)      │
2026-06-16 10:33:07.546 | │    70 │   except (ImportError, ValueError) as e:                             │
2026-06-16 10:33:07.546 | │    71 │   │   logger.error(f"Import error: {e}")                             │
2026-06-16 10:33:07.546 | │    72 │   │   logger.warning(                                                │
2026-06-16 10:33:07.546 | │                                                                              │
2026-06-16 10:33:07.546 | │ /usr/local/lib/python3.11/importlib/__init__.py:126 in import_module         │
2026-06-16 10:33:07.546 | │                                                                              │
2026-06-16 10:33:07.546 | │   123 │   │   │   if character != '.':                                       │
2026-06-16 10:33:07.546 | │   124 │   │   │   │   break                                                  │
2026-06-16 10:33:07.546 | │   125 │   │   │   level += 1                                                 │
2026-06-16 10:33:07.546 | │ ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)        │
2026-06-16 10:33:07.546 | │   127                                                                        │
2026-06-16 10:33:07.546 | │   128                                                                        │
2026-06-16 10:33:07.546 | │   129 _RELOADING = {}                                                        │
2026-06-16 10:33:07.546 | │ in _gcd_import:1204                                                          │
2026-06-16 10:33:07.546 | │ in _find_and_load:1176                                                       │
2026-06-16 10:33:07.546 | │ in _find_and_load_unlocked:1147                                              │
2026-06-16 10:33:07.546 | │ in _load_unlocked:690                                                        │
2026-06-16 10:33:07.546 | │ in exec_module:940                                                           │
2026-06-16 10:33:07.546 | │ in _call_with_frames_removed:241                                             │
2026-06-16 10:33:07.546 | │                                                                              │
2026-06-16 10:33:07.546 | │ /app/app/main.py:4 in <module>                                               │
2026-06-16 10:33:07.546 | │                                                                              │
2026-06-16 10:33:07.546 | │    1 from fastapi import FastAPI                                             │
2026-06-16 10:33:07.546 | │    2 from fastapi.middleware.cors import CORSMiddleware                      │
2026-06-16 10:33:07.546 | │    3                                                                         │
2026-06-16 10:33:07.546 | │ ❱  4 from app.core.config import settings                                    │
2026-06-16 10:33:07.546 | │    5 from app.api import auth, predict, resume, chat                         │
2026-06-16 10:33:07.546 | │    6                                                                         │
2026-06-16 10:33:07.546 | │    7 app = FastAPI(                                                          │
2026-06-16 10:33:07.546 | ╰──────────────────────────────────────────────────────────────────────────────╯
2026-06-16 10:33:07.546 | ModuleNotFoundError: No module named 'app'
2026-06-16 10:33:08.739 | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2026-06-16 10:33:08.739 | INFO  [alembic.runtime.migration] Will assume transactional DDL.
2026-06-16 10:33:09.441 | 
2026-06-16 10:33:09.442 |    FastAPI   Starting production server 🚀
2026-06-16 10:33:09.442 |  
2026-06-16 10:33:09.443 |              Searching for package file structure from directories with         
2026-06-16 10:33:09.443 |              __init__.py files                                                  
2026-06-16 10:33:09.444 | ERROR    Import error: No module named 'app'                                    
2026-06-16 10:33:09.445 | WARNING  Ensure all the package directories have an __init__.py file            
2026-06-16 10:33:09.445 | 
2026-06-16 10:33:09.508 | ╭───────────────────── Traceback (most recent call last) ──────────────────────╮
2026-06-16 10:33:09.508 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:435 in run        │
2026-06-16 10:33:09.508 | │                                                                              │
2026-06-16 10:33:09.508 | │   432 │                                                                      │
2026-06-16 10:33:09.508 | │   433 │   Otherwise, it uses the first [bold]FastAPI[/bold] app found in the │
2026-06-16 10:33:09.508 | │       imported module or package.                                            │
2026-06-16 10:33:09.508 | │   434 │   """                                                                │
2026-06-16 10:33:09.508 | │ ❱ 435 │   _run(                                                              │
2026-06-16 10:33:09.508 | │   436 │   │   path=path,                                                     │
2026-06-16 10:33:09.508 | │   437 │   │   host=host,                                                     │
2026-06-16 10:33:09.508 | │   438 │   │   port=port,                                                     │
2026-06-16 10:33:09.508 | │                                                                              │
2026-06-16 10:33:09.508 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:152 in _run       │
2026-06-16 10:33:09.508 | │                                                                              │
2026-06-16 10:33:09.508 | │   149 │   │   try:                                                           │
2026-06-16 10:33:09.508 | │   150 │   │   │   # Resolve import data with priority: CLI path/app > config │
2026-06-16 10:33:09.508 | │       entrypoint > auto-discovery                                            │
2026-06-16 10:33:09.508 | │   151 │   │   │   if path or app:                                            │
2026-06-16 10:33:09.508 | │ ❱ 152 │   │   │   │   import_data = get_import_data(path=path, app_name=app) │
2026-06-16 10:33:09.508 | │   153 │   │   │   elif config.entrypoint:                                    │
2026-06-16 10:33:09.508 | │   154 │   │   │   │   import_data =                                          │
2026-06-16 10:33:09.508 | │       get_import_data_from_import_string(config.entrypoint)                  │
2026-06-16 10:33:09.508 | │   155 │   │   │   else:                                                      │
2026-06-16 10:33:09.508 | │                                                                              │
2026-06-16 10:33:09.508 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:125 in       │
2026-06-16 10:33:09.508 | │ get_import_data                                                              │
2026-06-16 10:33:09.508 | │                                                                              │
2026-06-16 10:33:09.508 | │   122 │   │   raise FastAPICLIException(f"Path does not exist {path}")       │
2026-06-16 10:33:09.508 | │   123 │   mod_data = get_module_data_from_path(path)                         │
2026-06-16 10:33:09.508 | │   124 │   sys.path.insert(0, str(mod_data.extra_sys_path))                   │
2026-06-16 10:33:09.508 | │ ❱ 125 │   use_app_name = get_app_name(mod_data=mod_data, app_name=app_name)  │
2026-06-16 10:33:09.508 | │   126 │                                                                      │
2026-06-16 10:33:09.508 | │   127 │   import_string = f"{mod_data.module_import_str}:{use_app_name}"     │
2026-06-16 10:33:09.508 | │   128                                                                        │
2026-06-16 10:33:09.508 | │                                                                              │
2026-06-16 10:33:09.508 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:69 in        │
2026-06-16 10:33:09.508 | │ get_app_name                                                                 │
2026-06-16 10:33:09.508 | │                                                                              │
2026-06-16 10:33:09.508 | │    66                                                                        │
2026-06-16 10:33:09.508 | │    67 def get_app_name(*, mod_data: ModuleData, app_name: str | None = None) │
2026-06-16 10:33:09.508 | │       -> str:                                                                │
2026-06-16 10:33:09.508 | │    68 │   try:                                                               │
2026-06-16 10:33:09.508 | │ ❱  69 │   │   mod = importlib.import_module(mod_data.module_import_str)      │
2026-06-16 10:33:09.508 | │    70 │   except (ImportError, ValueError) as e:                             │
2026-06-16 10:33:09.508 | │    71 │   │   logger.error(f"Import error: {e}")                             │
2026-06-16 10:33:09.508 | │    72 │   │   logger.warning(                                                │
2026-06-16 10:33:09.508 | │                                                                              │
2026-06-16 10:33:09.508 | │ /usr/local/lib/python3.11/importlib/__init__.py:126 in import_module         │
2026-06-16 10:33:09.508 | │                                                                              │
2026-06-16 10:33:09.508 | │   123 │   │   │   if character != '.':                                       │
2026-06-16 10:33:09.508 | │   124 │   │   │   │   break                                                  │
2026-06-16 10:33:09.508 | │   125 │   │   │   level += 1                                                 │
2026-06-16 10:33:09.508 | │ ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)        │
2026-06-16 10:33:09.508 | │   127                                                                        │
2026-06-16 10:33:09.508 | │   128                                                                        │
2026-06-16 10:33:09.508 | │   129 _RELOADING = {}                                                        │
2026-06-16 10:33:09.508 | │ in _gcd_import:1204                                                          │
2026-06-16 10:33:09.508 | │ in _find_and_load:1176                                                       │
2026-06-16 10:33:09.508 | │ in _find_and_load_unlocked:1147                                              │
2026-06-16 10:33:09.508 | │ in _load_unlocked:690                                                        │
2026-06-16 10:33:09.508 | │ in exec_module:940                                                           │
2026-06-16 10:33:09.508 | │ in _call_with_frames_removed:241                                             │
2026-06-16 10:33:09.508 | │                                                                              │
2026-06-16 10:33:09.508 | │ /app/app/main.py:4 in <module>                                               │
2026-06-16 10:33:09.508 | │                                                                              │
2026-06-16 10:33:09.508 | │    1 from fastapi import FastAPI                                             │
2026-06-16 10:33:09.508 | │    2 from fastapi.middleware.cors import CORSMiddleware                      │
2026-06-16 10:33:09.508 | │    3                                                                         │
2026-06-16 10:33:09.508 | │ ❱  4 from app.core.config import settings                                    │
2026-06-16 10:33:09.508 | │    5 from app.api import auth, predict, resume, chat                         │
2026-06-16 10:33:09.508 | │    6                                                                         │
2026-06-16 10:33:09.508 | │    7 app = FastAPI(                                                          │
2026-06-16 10:33:09.508 | ╰──────────────────────────────────────────────────────────────────────────────╯
2026-06-16 10:33:09.508 | ModuleNotFoundError: No module named 'app'
2026-06-16 10:33:11.175 | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2026-06-16 10:33:11.175 | INFO  [alembic.runtime.migration] Will assume transactional DDL.
2026-06-16 10:33:11.910 | 
2026-06-16 10:33:11.911 |    FastAPI   Starting production server 🚀
2026-06-16 10:33:11.911 |  
2026-06-16 10:33:11.911 |              Searching for package file structure from directories with         
2026-06-16 10:33:11.911 |              __init__.py files                                                  
2026-06-16 10:33:11.913 | ERROR    Import error: No module named 'app'                                    
2026-06-16 10:33:11.913 | WARNING  Ensure all the package directories have an __init__.py file            
2026-06-16 10:33:11.913 | 
2026-06-16 10:33:11.977 | ╭───────────────────── Traceback (most recent call last) ──────────────────────╮
2026-06-16 10:33:11.977 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:435 in run        │
2026-06-16 10:33:11.977 | │                                                                              │
2026-06-16 10:33:11.977 | │   432 │                                                                      │
2026-06-16 10:33:11.977 | │   433 │   Otherwise, it uses the first [bold]FastAPI[/bold] app found in the │
2026-06-16 10:33:11.977 | │       imported module or package.                                            │
2026-06-16 10:33:11.977 | │   434 │   """                                                                │
2026-06-16 10:33:11.977 | │ ❱ 435 │   _run(                                                              │
2026-06-16 10:33:11.977 | │   436 │   │   path=path,                                                     │
2026-06-16 10:33:11.977 | │   437 │   │   host=host,                                                     │
2026-06-16 10:33:11.977 | │   438 │   │   port=port,                                                     │
2026-06-16 10:33:11.977 | │                                                                              │
2026-06-16 10:33:11.977 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:152 in _run       │
2026-06-16 10:33:11.977 | │                                                                              │
2026-06-16 10:33:11.977 | │   149 │   │   try:                                                           │
2026-06-16 10:33:11.977 | │   150 │   │   │   # Resolve import data with priority: CLI path/app > config │
2026-06-16 10:33:11.977 | │       entrypoint > auto-discovery                                            │
2026-06-16 10:33:11.977 | │   151 │   │   │   if path or app:                                            │
2026-06-16 10:33:11.977 | │ ❱ 152 │   │   │   │   import_data = get_import_data(path=path, app_name=app) │
2026-06-16 10:33:11.977 | │   153 │   │   │   elif config.entrypoint:                                    │
2026-06-16 10:33:11.977 | │   154 │   │   │   │   import_data =                                          │
2026-06-16 10:33:11.977 | │       get_import_data_from_import_string(config.entrypoint)                  │
2026-06-16 10:33:11.977 | │   155 │   │   │   else:                                                      │
2026-06-16 10:33:11.977 | │                                                                              │
2026-06-16 10:33:11.977 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:125 in       │
2026-06-16 10:33:11.977 | │ get_import_data                                                              │
2026-06-16 10:33:11.977 | │                                                                              │
2026-06-16 10:33:11.977 | │   122 │   │   raise FastAPICLIException(f"Path does not exist {path}")       │
2026-06-16 10:33:11.977 | │   123 │   mod_data = get_module_data_from_path(path)                         │
2026-06-16 10:33:11.977 | │   124 │   sys.path.insert(0, str(mod_data.extra_sys_path))                   │
2026-06-16 10:33:11.977 | │ ❱ 125 │   use_app_name = get_app_name(mod_data=mod_data, app_name=app_name)  │
2026-06-16 10:33:11.977 | │   126 │                                                                      │
2026-06-16 10:33:11.977 | │   127 │   import_string = f"{mod_data.module_import_str}:{use_app_name}"     │
2026-06-16 10:33:11.977 | │   128                                                                        │
2026-06-16 10:33:11.977 | │                                                                              │
2026-06-16 10:33:11.977 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:69 in        │
2026-06-16 10:33:11.977 | │ get_app_name                                                                 │
2026-06-16 10:33:11.977 | │                                                                              │
2026-06-16 10:33:11.977 | │    66                                                                        │
2026-06-16 10:33:11.977 | │    67 def get_app_name(*, mod_data: ModuleData, app_name: str | None = None) │
2026-06-16 10:33:11.977 | │       -> str:                                                                │
2026-06-16 10:33:11.977 | │    68 │   try:                                                               │
2026-06-16 10:33:11.977 | │ ❱  69 │   │   mod = importlib.import_module(mod_data.module_import_str)      │
2026-06-16 10:33:11.977 | │    70 │   except (ImportError, ValueError) as e:                             │
2026-06-16 10:33:11.977 | │    71 │   │   logger.error(f"Import error: {e}")                             │
2026-06-16 10:33:11.977 | │    72 │   │   logger.warning(                                                │
2026-06-16 10:33:11.977 | │                                                                              │
2026-06-16 10:33:11.977 | │ /usr/local/lib/python3.11/importlib/__init__.py:126 in import_module         │
2026-06-16 10:33:11.977 | │                                                                              │
2026-06-16 10:33:11.977 | │   123 │   │   │   if character != '.':                                       │
2026-06-16 10:33:11.977 | │   124 │   │   │   │   break                                                  │
2026-06-16 10:33:11.977 | │   125 │   │   │   level += 1                                                 │
2026-06-16 10:33:11.977 | │ ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)        │
2026-06-16 10:33:11.977 | │   127                                                                        │
2026-06-16 10:33:11.977 | │   128                                                                        │
2026-06-16 10:33:11.977 | │   129 _RELOADING = {}                                                        │
2026-06-16 10:33:11.977 | │ in _gcd_import:1204                                                          │
2026-06-16 10:33:11.977 | │ in _find_and_load:1176                                                       │
2026-06-16 10:33:11.977 | │ in _find_and_load_unlocked:1147                                              │
2026-06-16 10:33:11.977 | │ in _load_unlocked:690                                                        │
2026-06-16 10:33:11.977 | │ in exec_module:940                                                           │
2026-06-16 10:33:11.977 | │ in _call_with_frames_removed:241                                             │
2026-06-16 10:33:11.977 | │                                                                              │
2026-06-16 10:33:11.977 | │ /app/app/main.py:4 in <module>                                               │
2026-06-16 10:33:11.977 | │                                                                              │
2026-06-16 10:33:11.977 | │    1 from fastapi import FastAPI                                             │
2026-06-16 10:33:11.977 | │    2 from fastapi.middleware.cors import CORSMiddleware                      │
2026-06-16 10:33:11.977 | │    3                                                                         │
2026-06-16 10:33:11.977 | │ ❱  4 from app.core.config import settings                                    │
2026-06-16 10:33:11.977 | │    5 from app.api import auth, predict, resume, chat                         │
2026-06-16 10:33:11.977 | │    6                                                                         │
2026-06-16 10:33:11.977 | │    7 app = FastAPI(                                                          │
2026-06-16 10:33:11.977 | ╰──────────────────────────────────────────────────────────────────────────────╯
2026-06-16 10:33:11.977 | ModuleNotFoundError: No module named 'app'
2026-06-16 10:33:14.382 | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2026-06-16 10:33:14.382 | INFO  [alembic.runtime.migration] Will assume transactional DDL.
2026-06-16 10:33:15.090 | 
2026-06-16 10:33:15.090 |    FastAPI   Starting production server 🚀
2026-06-16 10:33:15.090 |  
2026-06-16 10:33:15.091 |              Searching for package file structure from directories with         
2026-06-16 10:33:15.091 |              __init__.py files                                                  
2026-06-16 10:33:15.092 | ERROR    Import error: No module named 'app'                                    
2026-06-16 10:33:15.093 | WARNING  Ensure all the package directories have an __init__.py file            
2026-06-16 10:33:15.093 | 
2026-06-16 10:33:15.158 | ╭───────────────────── Traceback (most recent call last) ──────────────────────╮
2026-06-16 10:33:15.158 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:435 in run        │
2026-06-16 10:33:15.158 | │                                                                              │
2026-06-16 10:33:15.158 | │   432 │                                                                      │
2026-06-16 10:33:15.158 | │   433 │   Otherwise, it uses the first [bold]FastAPI[/bold] app found in the │
2026-06-16 10:33:15.158 | │       imported module or package.                                            │
2026-06-16 10:33:15.158 | │   434 │   """                                                                │
2026-06-16 10:33:15.158 | │ ❱ 435 │   _run(                                                              │
2026-06-16 10:33:15.158 | │   436 │   │   path=path,                                                     │
2026-06-16 10:33:15.158 | │   437 │   │   host=host,                                                     │
2026-06-16 10:33:15.158 | │   438 │   │   port=port,                                                     │
2026-06-16 10:33:15.158 | │                                                                              │
2026-06-16 10:33:15.158 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:152 in _run       │
2026-06-16 10:33:15.158 | │                                                                              │
2026-06-16 10:33:15.158 | │   149 │   │   try:                                                           │
2026-06-16 10:33:15.158 | │   150 │   │   │   # Resolve import data with priority: CLI path/app > config │
2026-06-16 10:33:15.158 | │       entrypoint > auto-discovery                                            │
2026-06-16 10:33:15.158 | │   151 │   │   │   if path or app:                                            │
2026-06-16 10:33:15.158 | │ ❱ 152 │   │   │   │   import_data = get_import_data(path=path, app_name=app) │
2026-06-16 10:33:15.158 | │   153 │   │   │   elif config.entrypoint:                                    │
2026-06-16 10:33:15.158 | │   154 │   │   │   │   import_data =                                          │
2026-06-16 10:33:15.158 | │       get_import_data_from_import_string(config.entrypoint)                  │
2026-06-16 10:33:15.158 | │   155 │   │   │   else:                                                      │
2026-06-16 10:33:15.158 | │                                                                              │
2026-06-16 10:33:15.158 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:125 in       │
2026-06-16 10:33:15.158 | │ get_import_data                                                              │
2026-06-16 10:33:15.158 | │                                                                              │
2026-06-16 10:33:15.158 | │   122 │   │   raise FastAPICLIException(f"Path does not exist {path}")       │
2026-06-16 10:33:15.158 | │   123 │   mod_data = get_module_data_from_path(path)                         │
2026-06-16 10:33:15.158 | │   124 │   sys.path.insert(0, str(mod_data.extra_sys_path))                   │
2026-06-16 10:33:15.158 | │ ❱ 125 │   use_app_name = get_app_name(mod_data=mod_data, app_name=app_name)  │
2026-06-16 10:33:15.158 | │   126 │                                                                      │
2026-06-16 10:33:15.158 | │   127 │   import_string = f"{mod_data.module_import_str}:{use_app_name}"     │
2026-06-16 10:33:15.158 | │   128                                                                        │
2026-06-16 10:33:15.158 | │                                                                              │
2026-06-16 10:33:15.158 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:69 in        │
2026-06-16 10:33:15.158 | │ get_app_name                                                                 │
2026-06-16 10:33:15.158 | │                                                                              │
2026-06-16 10:33:15.158 | │    66                                                                        │
2026-06-16 10:33:15.158 | │    67 def get_app_name(*, mod_data: ModuleData, app_name: str | None = None) │
2026-06-16 10:33:15.158 | │       -> str:                                                                │
2026-06-16 10:33:15.158 | │    68 │   try:                                                               │
2026-06-16 10:33:15.158 | │ ❱  69 │   │   mod = importlib.import_module(mod_data.module_import_str)      │
2026-06-16 10:33:15.158 | │    70 │   except (ImportError, ValueError) as e:                             │
2026-06-16 10:33:15.158 | │    71 │   │   logger.error(f"Import error: {e}")                             │
2026-06-16 10:33:15.158 | │    72 │   │   logger.warning(                                                │
2026-06-16 10:33:15.158 | │                                                                              │
2026-06-16 10:33:15.158 | │ /usr/local/lib/python3.11/importlib/__init__.py:126 in import_module         │
2026-06-16 10:33:15.158 | │                                                                              │
2026-06-16 10:33:15.158 | │   123 │   │   │   if character != '.':                                       │
2026-06-16 10:33:15.158 | │   124 │   │   │   │   break                                                  │
2026-06-16 10:33:15.158 | │   125 │   │   │   level += 1                                                 │
2026-06-16 10:33:15.158 | │ ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)        │
2026-06-16 10:33:15.158 | │   127                                                                        │
2026-06-16 10:33:15.158 | │   128                                                                        │
2026-06-16 10:33:15.158 | │   129 _RELOADING = {}                                                        │
2026-06-16 10:33:15.158 | │ in _gcd_import:1204                                                          │
2026-06-16 10:33:15.158 | │ in _find_and_load:1176                                                       │
2026-06-16 10:33:15.158 | │ in _find_and_load_unlocked:1147                                              │
2026-06-16 10:33:15.158 | │ in _load_unlocked:690                                                        │
2026-06-16 10:33:15.158 | │ in exec_module:940                                                           │
2026-06-16 10:33:15.158 | │ in _call_with_frames_removed:241                                             │
2026-06-16 10:33:15.158 | │                                                                              │
2026-06-16 10:33:15.158 | │ /app/app/main.py:4 in <module>                                               │
2026-06-16 10:33:15.158 | │                                                                              │
2026-06-16 10:33:15.158 | │    1 from fastapi import FastAPI                                             │
2026-06-16 10:33:15.158 | │    2 from fastapi.middleware.cors import CORSMiddleware                      │
2026-06-16 10:33:15.158 | │    3                                                                         │
2026-06-16 10:33:15.158 | │ ❱  4 from app.core.config import settings                                    │
2026-06-16 10:33:15.158 | │    5 from app.api import auth, predict, resume, chat                         │
2026-06-16 10:33:15.158 | │    6                                                                         │
2026-06-16 10:33:15.158 | │    7 app = FastAPI(                                                          │
2026-06-16 10:33:15.158 | ╰──────────────────────────────────────────────────────────────────────────────╯
2026-06-16 10:33:15.158 | ModuleNotFoundError: No module named 'app'
2026-06-16 10:33:19.166 | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2026-06-16 10:33:19.166 | INFO  [alembic.runtime.migration] Will assume transactional DDL.
2026-06-16 10:33:19.863 | 
2026-06-16 10:33:19.863 |    FastAPI   Starting production server 🚀
2026-06-16 10:33:19.863 |  
2026-06-16 10:33:19.864 |              Searching for package file structure from directories with         
2026-06-16 10:33:19.864 |              __init__.py files                                                  
2026-06-16 10:33:19.866 | ERROR    Import error: No module named 'app'                                    
2026-06-16 10:33:19.866 | WARNING  Ensure all the package directories have an __init__.py file            
2026-06-16 10:33:19.866 | 
2026-06-16 10:33:19.930 | ╭───────────────────── Traceback (most recent call last) ──────────────────────╮
2026-06-16 10:33:19.930 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:435 in run        │
2026-06-16 10:33:19.930 | │                                                                              │
2026-06-16 10:33:19.930 | │   432 │                                                                      │
2026-06-16 10:33:19.930 | │   433 │   Otherwise, it uses the first [bold]FastAPI[/bold] app found in the │
2026-06-16 10:33:19.930 | │       imported module or package.                                            │
2026-06-16 10:33:19.930 | │   434 │   """                                                                │
2026-06-16 10:33:19.930 | │ ❱ 435 │   _run(                                                              │
2026-06-16 10:33:19.930 | │   436 │   │   path=path,                                                     │
2026-06-16 10:33:19.930 | │   437 │   │   host=host,                                                     │
2026-06-16 10:33:19.930 | │   438 │   │   port=port,                                                     │
2026-06-16 10:33:19.930 | │                                                                              │
2026-06-16 10:33:19.930 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:152 in _run       │
2026-06-16 10:33:19.930 | │                                                                              │
2026-06-16 10:33:19.930 | │   149 │   │   try:                                                           │
2026-06-16 10:33:19.930 | │   150 │   │   │   # Resolve import data with priority: CLI path/app > config │
2026-06-16 10:33:19.930 | │       entrypoint > auto-discovery                                            │
2026-06-16 10:33:19.930 | │   151 │   │   │   if path or app:                                            │
2026-06-16 10:33:19.930 | │ ❱ 152 │   │   │   │   import_data = get_import_data(path=path, app_name=app) │
2026-06-16 10:33:19.930 | │   153 │   │   │   elif config.entrypoint:                                    │
2026-06-16 10:33:19.930 | │   154 │   │   │   │   import_data =                                          │
2026-06-16 10:33:19.930 | │       get_import_data_from_import_string(config.entrypoint)                  │
2026-06-16 10:33:19.930 | │   155 │   │   │   else:                                                      │
2026-06-16 10:33:19.930 | │                                                                              │
2026-06-16 10:33:19.930 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:125 in       │
2026-06-16 10:33:19.930 | │ get_import_data                                                              │
2026-06-16 10:33:19.930 | │                                                                              │
2026-06-16 10:33:19.930 | │   122 │   │   raise FastAPICLIException(f"Path does not exist {path}")       │
2026-06-16 10:33:19.930 | │   123 │   mod_data = get_module_data_from_path(path)                         │
2026-06-16 10:33:19.930 | │   124 │   sys.path.insert(0, str(mod_data.extra_sys_path))                   │
2026-06-16 10:33:19.930 | │ ❱ 125 │   use_app_name = get_app_name(mod_data=mod_data, app_name=app_name)  │
2026-06-16 10:33:19.930 | │   126 │                                                                      │
2026-06-16 10:33:19.930 | │   127 │   import_string = f"{mod_data.module_import_str}:{use_app_name}"     │
2026-06-16 10:33:19.930 | │   128                                                                        │
2026-06-16 10:33:19.930 | │                                                                              │
2026-06-16 10:33:19.930 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:69 in        │
2026-06-16 10:33:19.930 | │ get_app_name                                                                 │
2026-06-16 10:33:19.930 | │                                                                              │
2026-06-16 10:33:19.930 | │    66                                                                        │
2026-06-16 10:33:19.930 | │    67 def get_app_name(*, mod_data: ModuleData, app_name: str | None = None) │
2026-06-16 10:33:19.930 | │       -> str:                                                                │
2026-06-16 10:33:19.930 | │    68 │   try:                                                               │
2026-06-16 10:33:19.930 | │ ❱  69 │   │   mod = importlib.import_module(mod_data.module_import_str)      │
2026-06-16 10:33:19.930 | │    70 │   except (ImportError, ValueError) as e:                             │
2026-06-16 10:33:19.930 | │    71 │   │   logger.error(f"Import error: {e}")                             │
2026-06-16 10:33:19.930 | │    72 │   │   logger.warning(                                                │
2026-06-16 10:33:19.930 | │                                                                              │
2026-06-16 10:33:19.930 | │ /usr/local/lib/python3.11/importlib/__init__.py:126 in import_module         │
2026-06-16 10:33:19.930 | │                                                                              │
2026-06-16 10:33:19.930 | │   123 │   │   │   if character != '.':                                       │
2026-06-16 10:33:19.930 | │   124 │   │   │   │   break                                                  │
2026-06-16 10:33:19.930 | │   125 │   │   │   level += 1                                                 │
2026-06-16 10:33:19.930 | │ ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)        │
2026-06-16 10:33:19.930 | │   127                                                                        │
2026-06-16 10:33:19.930 | │   128                                                                        │
2026-06-16 10:33:19.930 | │   129 _RELOADING = {}                                                        │
2026-06-16 10:33:19.930 | │ in _gcd_import:1204                                                          │
2026-06-16 10:33:19.930 | │ in _find_and_load:1176                                                       │
2026-06-16 10:33:19.930 | │ in _find_and_load_unlocked:1147                                              │
2026-06-16 10:33:19.930 | │ in _load_unlocked:690                                                        │
2026-06-16 10:33:19.930 | │ in exec_module:940                                                           │
2026-06-16 10:33:19.930 | │ in _call_with_frames_removed:241                                             │
2026-06-16 10:33:19.930 | │                                                                              │
2026-06-16 10:33:19.930 | │ /app/app/main.py:4 in <module>                                               │
2026-06-16 10:33:19.930 | │                                                                              │
2026-06-16 10:33:19.930 | │    1 from fastapi import FastAPI                                             │
2026-06-16 10:33:19.930 | │    2 from fastapi.middleware.cors import CORSMiddleware                      │
2026-06-16 10:33:19.930 | │    3                                                                         │
2026-06-16 10:33:19.930 | │ ❱  4 from app.core.config import settings                                    │
2026-06-16 10:33:19.930 | │    5 from app.api import auth, predict, resume, chat                         │
2026-06-16 10:33:19.930 | │    6                                                                         │
2026-06-16 10:33:19.930 | │    7 app = FastAPI(                                                          │
2026-06-16 10:33:19.930 | ╰──────────────────────────────────────────────────────────────────────────────╯
2026-06-16 10:33:19.930 | ModuleNotFoundError: No module named 'app'
2026-06-16 10:33:27.092 | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2026-06-16 10:33:27.093 | INFO  [alembic.runtime.migration] Will assume transactional DDL.
2026-06-16 10:33:27.800 | 
2026-06-16 10:33:27.800 |    FastAPI   Starting production server 🚀
2026-06-16 10:33:27.800 |  
2026-06-16 10:33:27.801 |              Searching for package file structure from directories with         
2026-06-16 10:33:27.801 |              __init__.py files                                                  
2026-06-16 10:33:27.802 | ERROR    Import error: No module named 'app'                                    
2026-06-16 10:33:27.803 | WARNING  Ensure all the package directories have an __init__.py file            
2026-06-16 10:33:27.803 | 
2026-06-16 10:33:27.867 | ╭───────────────────── Traceback (most recent call last) ──────────────────────╮
2026-06-16 10:33:27.867 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:435 in run        │
2026-06-16 10:33:27.867 | │                                                                              │
2026-06-16 10:33:27.867 | │   432 │                                                                      │
2026-06-16 10:33:27.867 | │   433 │   Otherwise, it uses the first [bold]FastAPI[/bold] app found in the │
2026-06-16 10:33:27.867 | │       imported module or package.                                            │
2026-06-16 10:33:27.867 | │   434 │   """                                                                │
2026-06-16 10:33:27.867 | │ ❱ 435 │   _run(                                                              │
2026-06-16 10:33:27.867 | │   436 │   │   path=path,                                                     │
2026-06-16 10:33:27.867 | │   437 │   │   host=host,                                                     │
2026-06-16 10:33:27.867 | │   438 │   │   port=port,                                                     │
2026-06-16 10:33:27.867 | │                                                                              │
2026-06-16 10:33:27.867 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:152 in _run       │
2026-06-16 10:33:27.867 | │                                                                              │
2026-06-16 10:33:27.867 | │   149 │   │   try:                                                           │
2026-06-16 10:33:27.867 | │   150 │   │   │   # Resolve import data with priority: CLI path/app > config │
2026-06-16 10:33:27.867 | │       entrypoint > auto-discovery                                            │
2026-06-16 10:33:27.867 | │   151 │   │   │   if path or app:                                            │
2026-06-16 10:33:27.867 | │ ❱ 152 │   │   │   │   import_data = get_import_data(path=path, app_name=app) │
2026-06-16 10:33:27.867 | │   153 │   │   │   elif config.entrypoint:                                    │
2026-06-16 10:33:27.867 | │   154 │   │   │   │   import_data =                                          │
2026-06-16 10:33:27.867 | │       get_import_data_from_import_string(config.entrypoint)                  │
2026-06-16 10:33:27.867 | │   155 │   │   │   else:                                                      │
2026-06-16 10:33:27.867 | │                                                                              │
2026-06-16 10:33:27.867 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:125 in       │
2026-06-16 10:33:27.867 | │ get_import_data                                                              │
2026-06-16 10:33:27.867 | │                                                                              │
2026-06-16 10:33:27.867 | │   122 │   │   raise FastAPICLIException(f"Path does not exist {path}")       │
2026-06-16 10:33:27.867 | │   123 │   mod_data = get_module_data_from_path(path)                         │
2026-06-16 10:33:27.867 | │   124 │   sys.path.insert(0, str(mod_data.extra_sys_path))                   │
2026-06-16 10:33:27.867 | │ ❱ 125 │   use_app_name = get_app_name(mod_data=mod_data, app_name=app_name)  │
2026-06-16 10:33:27.867 | │   126 │                                                                      │
2026-06-16 10:33:27.867 | │   127 │   import_string = f"{mod_data.module_import_str}:{use_app_name}"     │
2026-06-16 10:33:27.867 | │   128                                                                        │
2026-06-16 10:33:27.867 | │                                                                              │
2026-06-16 10:33:27.867 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:69 in        │
2026-06-16 10:33:27.867 | │ get_app_name                                                                 │
2026-06-16 10:33:27.867 | │                                                                              │
2026-06-16 10:33:27.867 | │    66                                                                        │
2026-06-16 10:33:27.867 | │    67 def get_app_name(*, mod_data: ModuleData, app_name: str | None = None) │
2026-06-16 10:33:27.867 | │       -> str:                                                                │
2026-06-16 10:33:27.867 | │    68 │   try:                                                               │
2026-06-16 10:33:27.867 | │ ❱  69 │   │   mod = importlib.import_module(mod_data.module_import_str)      │
2026-06-16 10:33:27.867 | │    70 │   except (ImportError, ValueError) as e:                             │
2026-06-16 10:33:27.867 | │    71 │   │   logger.error(f"Import error: {e}")                             │
2026-06-16 10:33:27.867 | │    72 │   │   logger.warning(                                                │
2026-06-16 10:33:27.867 | │                                                                              │
2026-06-16 10:33:27.867 | │ /usr/local/lib/python3.11/importlib/__init__.py:126 in import_module         │
2026-06-16 10:33:27.867 | │                                                                              │
2026-06-16 10:33:27.867 | │   123 │   │   │   if character != '.':                                       │
2026-06-16 10:33:27.867 | │   124 │   │   │   │   break                                                  │
2026-06-16 10:33:27.867 | │   125 │   │   │   level += 1                                                 │
2026-06-16 10:33:27.867 | │ ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)        │
2026-06-16 10:33:27.867 | │   127                                                                        │
2026-06-16 10:33:27.867 | │   128                                                                        │
2026-06-16 10:33:27.867 | │   129 _RELOADING = {}                                                        │
2026-06-16 10:33:27.867 | │ in _gcd_import:1204                                                          │
2026-06-16 10:33:27.867 | │ in _find_and_load:1176                                                       │
2026-06-16 10:33:27.867 | │ in _find_and_load_unlocked:1147                                              │
2026-06-16 10:33:27.867 | │ in _load_unlocked:690                                                        │
2026-06-16 10:33:27.867 | │ in exec_module:940                                                           │
2026-06-16 10:33:27.867 | │ in _call_with_frames_removed:241                                             │
2026-06-16 10:33:27.867 | │                                                                              │
2026-06-16 10:33:27.867 | │ /app/app/main.py:4 in <module>                                               │
2026-06-16 10:33:27.867 | │                                                                              │
2026-06-16 10:33:27.867 | │    1 from fastapi import FastAPI                                             │
2026-06-16 10:33:27.867 | │    2 from fastapi.middleware.cors import CORSMiddleware                      │
2026-06-16 10:33:27.867 | │    3                                                                         │
2026-06-16 10:33:27.867 | │ ❱  4 from app.core.config import settings                                    │
2026-06-16 10:33:27.867 | │    5 from app.api import auth, predict, resume, chat                         │
2026-06-16 10:33:27.867 | │    6                                                                         │
2026-06-16 10:33:27.867 | │    7 app = FastAPI(                                                          │
2026-06-16 10:33:27.867 | ╰──────────────────────────────────────────────────────────────────────────────╯
2026-06-16 10:33:27.867 | ModuleNotFoundError: No module named 'app'
2026-06-16 10:33:41.531 | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2026-06-16 10:33:41.531 | INFO  [alembic.runtime.migration] Will assume transactional DDL.
2026-06-16 10:33:42.339 | 
2026-06-16 10:33:42.340 |    FastAPI   Starting production server 🚀
2026-06-16 10:33:42.340 |  
2026-06-16 10:33:42.341 |              Searching for package file structure from directories with         
2026-06-16 10:33:42.341 |              __init__.py files                                                  
2026-06-16 10:33:42.342 | ERROR    Import error: No module named 'app'                                    
2026-06-16 10:33:42.343 | WARNING  Ensure all the package directories have an __init__.py file            
2026-06-16 10:33:42.343 | 
2026-06-16 10:33:42.414 | ╭───────────────────── Traceback (most recent call last) ──────────────────────╮
2026-06-16 10:33:42.414 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:435 in run        │
2026-06-16 10:33:42.414 | │                                                                              │
2026-06-16 10:33:42.414 | │   432 │                                                                      │
2026-06-16 10:33:42.414 | │   433 │   Otherwise, it uses the first [bold]FastAPI[/bold] app found in the │
2026-06-16 10:33:42.414 | │       imported module or package.                                            │
2026-06-16 10:33:42.414 | │   434 │   """                                                                │
2026-06-16 10:33:42.414 | │ ❱ 435 │   _run(                                                              │
2026-06-16 10:33:42.414 | │   436 │   │   path=path,                                                     │
2026-06-16 10:33:42.414 | │   437 │   │   host=host,                                                     │
2026-06-16 10:33:42.414 | │   438 │   │   port=port,                                                     │
2026-06-16 10:33:42.414 | │                                                                              │
2026-06-16 10:33:42.414 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:152 in _run       │
2026-06-16 10:33:42.414 | │                                                                              │
2026-06-16 10:33:42.414 | │   149 │   │   try:                                                           │
2026-06-16 10:33:42.414 | │   150 │   │   │   # Resolve import data with priority: CLI path/app > config │
2026-06-16 10:33:42.414 | │       entrypoint > auto-discovery                                            │
2026-06-16 10:33:42.414 | │   151 │   │   │   if path or app:                                            │
2026-06-16 10:33:42.414 | │ ❱ 152 │   │   │   │   import_data = get_import_data(path=path, app_name=app) │
2026-06-16 10:33:42.414 | │   153 │   │   │   elif config.entrypoint:                                    │
2026-06-16 10:33:42.414 | │   154 │   │   │   │   import_data =                                          │
2026-06-16 10:33:42.414 | │       get_import_data_from_import_string(config.entrypoint)                  │
2026-06-16 10:33:42.414 | │   155 │   │   │   else:                                                      │
2026-06-16 10:33:42.414 | │                                                                              │
2026-06-16 10:33:42.414 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:125 in       │
2026-06-16 10:33:42.414 | │ get_import_data                                                              │
2026-06-16 10:33:42.414 | │                                                                              │
2026-06-16 10:33:42.414 | │   122 │   │   raise FastAPICLIException(f"Path does not exist {path}")       │
2026-06-16 10:33:42.414 | │   123 │   mod_data = get_module_data_from_path(path)                         │
2026-06-16 10:33:42.414 | │   124 │   sys.path.insert(0, str(mod_data.extra_sys_path))                   │
2026-06-16 10:33:42.414 | │ ❱ 125 │   use_app_name = get_app_name(mod_data=mod_data, app_name=app_name)  │
2026-06-16 10:33:42.414 | │   126 │                                                                      │
2026-06-16 10:33:42.414 | │   127 │   import_string = f"{mod_data.module_import_str}:{use_app_name}"     │
2026-06-16 10:33:42.414 | │   128                                                                        │
2026-06-16 10:33:42.414 | │                                                                              │
2026-06-16 10:33:42.414 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:69 in        │
2026-06-16 10:33:42.414 | │ get_app_name                                                                 │
2026-06-16 10:33:42.414 | │                                                                              │
2026-06-16 10:33:42.414 | │    66                                                                        │
2026-06-16 10:33:42.414 | │    67 def get_app_name(*, mod_data: ModuleData, app_name: str | None = None) │
2026-06-16 10:33:42.414 | │       -> str:                                                                │
2026-06-16 10:33:42.414 | │    68 │   try:                                                               │
2026-06-16 10:33:42.414 | │ ❱  69 │   │   mod = importlib.import_module(mod_data.module_import_str)      │
2026-06-16 10:33:42.414 | │    70 │   except (ImportError, ValueError) as e:                             │
2026-06-16 10:33:42.414 | │    71 │   │   logger.error(f"Import error: {e}")                             │
2026-06-16 10:33:42.414 | │    72 │   │   logger.warning(                                                │
2026-06-16 10:33:42.414 | │                                                                              │
2026-06-16 10:33:42.414 | │ /usr/local/lib/python3.11/importlib/__init__.py:126 in import_module         │
2026-06-16 10:33:42.414 | │                                                                              │
2026-06-16 10:33:42.414 | │   123 │   │   │   if character != '.':                                       │
2026-06-16 10:33:42.414 | │   124 │   │   │   │   break                                                  │
2026-06-16 10:33:42.414 | │   125 │   │   │   level += 1                                                 │
2026-06-16 10:33:42.414 | │ ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)        │
2026-06-16 10:33:42.414 | │   127                                                                        │
2026-06-16 10:33:42.414 | │   128                                                                        │
2026-06-16 10:33:42.414 | │   129 _RELOADING = {}                                                        │
2026-06-16 10:33:42.414 | │ in _gcd_import:1204                                                          │
2026-06-16 10:33:42.414 | │ in _find_and_load:1176                                                       │
2026-06-16 10:33:42.414 | │ in _find_and_load_unlocked:1147                                              │
2026-06-16 10:33:42.414 | │ in _load_unlocked:690                                                        │
2026-06-16 10:33:42.414 | │ in exec_module:940                                                           │
2026-06-16 10:33:42.414 | │ in _call_with_frames_removed:241                                             │
2026-06-16 10:33:42.414 | │                                                                              │
2026-06-16 10:33:42.414 | │ /app/app/main.py:4 in <module>                                               │
2026-06-16 10:33:42.414 | │                                                                              │
2026-06-16 10:33:42.414 | │    1 from fastapi import FastAPI                                             │
2026-06-16 10:33:42.414 | │    2 from fastapi.middleware.cors import CORSMiddleware                      │
2026-06-16 10:33:42.414 | │    3                                                                         │
2026-06-16 10:33:42.414 | │ ❱  4 from app.core.config import settings                                    │
2026-06-16 10:33:42.414 | │    5 from app.api import auth, predict, resume, chat                         │
2026-06-16 10:33:42.414 | │    6                                                                         │
2026-06-16 10:33:42.414 | │    7 app = FastAPI(                                                          │
2026-06-16 10:33:42.414 | ╰──────────────────────────────────────────────────────────────────────────────╯
2026-06-16 10:33:42.414 | ModuleNotFoundError: No module named 'app'
2026-06-16 10:34:08.911 | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
2026-06-16 10:34:08.911 | INFO  [alembic.runtime.migration] Will assume transactional DDL.
2026-06-16 10:34:09.650 | 
2026-06-16 10:34:09.651 |    FastAPI   Starting production server 🚀
2026-06-16 10:34:09.651 |  
2026-06-16 10:34:09.652 |              Searching for package file structure from directories with         
2026-06-16 10:34:09.652 |              __init__.py files                                                  
2026-06-16 10:34:09.653 | ERROR    Import error: No module named 'app'                                    
2026-06-16 10:34:09.653 | WARNING  Ensure all the package directories have an __init__.py file            
2026-06-16 10:34:09.653 | 
2026-06-16 10:34:09.717 | ╭───────────────────── Traceback (most recent call last) ──────────────────────╮
2026-06-16 10:34:09.717 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:435 in run        │
2026-06-16 10:34:09.717 | │                                                                              │
2026-06-16 10:34:09.717 | │   432 │                                                                      │
2026-06-16 10:34:09.717 | │   433 │   Otherwise, it uses the first [bold]FastAPI[/bold] app found in the │
2026-06-16 10:34:09.717 | │       imported module or package.                                            │
2026-06-16 10:34:09.717 | │   434 │   """                                                                │
2026-06-16 10:34:09.717 | │ ❱ 435 │   _run(                                                              │
2026-06-16 10:34:09.717 | │   436 │   │   path=path,                                                     │
2026-06-16 10:34:09.717 | │   437 │   │   host=host,                                                     │
2026-06-16 10:34:09.717 | │   438 │   │   port=port,                                                     │
2026-06-16 10:34:09.717 | │                                                                              │
2026-06-16 10:34:09.717 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/cli.py:152 in _run       │
2026-06-16 10:34:09.717 | │                                                                              │
2026-06-16 10:34:09.717 | │   149 │   │   try:                                                           │
2026-06-16 10:34:09.717 | │   150 │   │   │   # Resolve import data with priority: CLI path/app > config │
2026-06-16 10:34:09.717 | │       entrypoint > auto-discovery                                            │
2026-06-16 10:34:09.717 | │   151 │   │   │   if path or app:                                            │
2026-06-16 10:34:09.717 | │ ❱ 152 │   │   │   │   import_data = get_import_data(path=path, app_name=app) │
2026-06-16 10:34:09.717 | │   153 │   │   │   elif config.entrypoint:                                    │
2026-06-16 10:34:09.717 | │   154 │   │   │   │   import_data =                                          │
2026-06-16 10:34:09.717 | │       get_import_data_from_import_string(config.entrypoint)                  │
2026-06-16 10:34:09.717 | │   155 │   │   │   else:                                                      │
2026-06-16 10:34:09.717 | │                                                                              │
2026-06-16 10:34:09.717 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:125 in       │
2026-06-16 10:34:09.717 | │ get_import_data                                                              │
2026-06-16 10:34:09.717 | │                                                                              │
2026-06-16 10:34:09.717 | │   122 │   │   raise FastAPICLIException(f"Path does not exist {path}")       │
2026-06-16 10:34:09.717 | │   123 │   mod_data = get_module_data_from_path(path)                         │
2026-06-16 10:34:09.717 | │   124 │   sys.path.insert(0, str(mod_data.extra_sys_path))                   │
2026-06-16 10:34:09.717 | │ ❱ 125 │   use_app_name = get_app_name(mod_data=mod_data, app_name=app_name)  │
2026-06-16 10:34:09.717 | │   126 │                                                                      │
2026-06-16 10:34:09.717 | │   127 │   import_string = f"{mod_data.module_import_str}:{use_app_name}"     │
2026-06-16 10:34:09.717 | │   128                                                                        │
2026-06-16 10:34:09.717 | │                                                                              │
2026-06-16 10:34:09.717 | │ /usr/local/lib/python3.11/site-packages/fastapi_cli/discover.py:69 in        │
2026-06-16 10:34:09.717 | │ get_app_name                                                                 │
2026-06-16 10:34:09.717 | │                                                                              │
2026-06-16 10:34:09.717 | │    66                                                                        │
2026-06-16 10:34:09.717 | │    67 def get_app_name(*, mod_data: ModuleData, app_name: str | None = None) │
2026-06-16 10:34:09.717 | │       -> str:                                                                │
2026-06-16 10:34:09.717 | │    68 │   try:                                                               │
2026-06-16 10:34:09.717 | │ ❱  69 │   │   mod = importlib.import_module(mod_data.module_import_str)      │
2026-06-16 10:34:09.717 | │    70 │   except (ImportError, ValueError) as e:                             │
2026-06-16 10:34:09.717 | │    71 │   │   logger.error(f"Import error: {e}")                             │
2026-06-16 10:34:09.717 | │    72 │   │   logger.warning(                                                │
2026-06-16 10:34:09.717 | │                                                                              │
2026-06-16 10:34:09.717 | │ /usr/local/lib/python3.11/importlib/__init__.py:126 in import_module         │
2026-06-16 10:34:09.717 | │                                                                              │
2026-06-16 10:34:09.717 | │   123 │   │   │   if character != '.':                                       │
2026-06-16 10:34:09.717 | │   124 │   │   │   │   break                                                  │
2026-06-16 10:34:09.717 | │   125 │   │   │   level += 1                                                 │
2026-06-16 10:34:09.717 | │ ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)        │
2026-06-16 10:34:09.717 | │   127                                                                        │
2026-06-16 10:34:09.717 | │   128                                                                        │
2026-06-16 10:34:09.717 | │   129 _RELOADING = {}                                                        │
2026-06-16 10:34:09.717 | │ in _gcd_import:1204                                                          │
2026-06-16 10:34:09.717 | │ in _find_and_load:1176                                                       │
2026-06-16 10:34:09.717 | │ in _find_and_load_unlocked:1147                                              │
2026-06-16 10:34:09.717 | │ in _load_unlocked:690                                                        │
2026-06-16 10:34:09.717 | │ in exec_module:940                                                           │
2026-06-16 10:34:09.717 | │ in _call_with_frames_removed:241                                             │
2026-06-16 10:34:09.717 | │                                                                              │
2026-06-16 10:34:09.717 | │ /app/app/main.py:4 in <module>                                               │
2026-06-16 10:34:09.717 | │                                                                              │
2026-06-16 10:34:09.717 | │    1 from fastapi import FastAPI                                             │
2026-06-16 10:34:09.717 | │    2 from fastapi.middleware.cors import CORSMiddleware                      │
2026-06-16 10:34:09.717 | │    3                                                                         │
2026-06-16 10:34:09.717 | │ ❱  4 from app.core.config import settings                                    │
2026-06-16 10:34:09.717 | │    5 from app.api import auth, predict, resume, chat                         │
2026-06-16 10:34:09.717 | │    6                                                                         │
2026-06-16 10:34:09.717 | │    7 app = FastAPI(                                                          │
2026-06-16 10:34:09.717 | ╰──────────────────────────────────────────────────────────────────────────────╯
2026-06-16 10:34:09.717 | ModuleNotFoundError: No module named 'app'