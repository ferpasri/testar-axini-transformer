@echo off
REM Create a Python virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Install dependencies from requirements.txt
pip install -r requirements.txt
