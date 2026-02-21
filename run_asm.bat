@echo off
echo [ASM] Starting Automated Attack Surface Scan...

:: Navigate to the project directory (Change this to your actual project path)
cd /d "C:\Path\To\Your\Project"

:: Activate virtual environment if you have one (Optional but recommended)
:: call venv\Scripts\activate

:: Run the main orchestrator
python asm.py

echo [ASM] Scan Complete. Check the output folder for reports.
pause