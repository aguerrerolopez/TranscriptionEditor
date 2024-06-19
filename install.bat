@echo off
echo Installing the required packages...

REM Create a virtual environment
python -m venv manual_transcriptor
echo Virtual environment created.

echo Activating the virtual environment...
REM Activate the virtual environment
call manual_transcriptor\Scripts\activate

echo Installing the required packages...
REM Upgrade pip
pip install --upgrade pip

REM Install required packages
pip install -r requirements.txt

echo Installation complete. Run run.bat to run the app.
pause
