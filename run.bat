@echo off
echo Checking if virtual environment exists...

IF NOT EXIST "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Changing to src directory...
cd src

echo Running the script...
..\venv\Scripts\python.exe timer.py

echo.
echo Script has ended. Press any key to close.
pause > nul
