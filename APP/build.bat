@echo off
REM Build script for LSCI Experiment Windows Executable
REM This script should be run on a Windows 11 PC with Python and Pylon SDK installed

echo ========================================
echo LSCI Experiment - Build Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11.x from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Step 1: Installing build dependencies...
pip install pyinstaller

echo.
echo Step 2: Installing application dependencies...
cd ..
pip install -r requirements.txt

echo.
echo Step 3: Building executable with PyInstaller...
cd APP
pyinstaller build_exe.spec --clean --noconfirm

echo.
echo ========================================
echo Build Complete!
echo ========================================
echo.
echo The executable and all files are in:
echo   APP\dist\LSCIExperiment\
echo.
echo To run the application:
echo   1. Navigate to APP\dist\LSCIExperiment\
echo   2. Double-click LSCIExperiment.exe
echo.
echo To distribute the application:
echo   Copy the entire APP\dist\LSCIExperiment\ folder
echo   to the target Windows 11 PC with Pylon SDK installed.
echo.
pause
