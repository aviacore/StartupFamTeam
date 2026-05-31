@echo off
cd /d "%~dp0"
title CraftStack
set PORT=8765

echo.
echo  ========================================
echo     CraftStack v0.4
echo  ========================================
echo.

echo  [1/3] Killing old servers...
taskkill /f /im pythonw.exe 2>nul >nul
taskkill /f /im python.exe 2>nul >nul

echo  [2/3] Starting server on port %PORT%...
start /min "" "C:\Python314\pythonw.exe" "%~dp0server.py" %PORT%
timeout /t 2 /nobreak >nul

echo  [3/3] Opening Dashboard...
start "" "http://127.0.0.1:%PORT%/dashboard.html"

echo.
echo  ========================================
echo   Dashboard: http://127.0.0.1:%PORT%/dashboard.html
echo   Agents:    http://127.0.0.1:%PORT%/agents.html
echo   Providers: http://127.0.0.1:%PORT%/providers.html
echo   Monitor:   http://127.0.0.1:%PORT%/monitor.html
echo  ========================================
echo.
