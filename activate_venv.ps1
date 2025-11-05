# Script para activar el entorno virtual en PowerShell
# Uso: .\activate_venv.ps1

$projectPath = "C:\Users\ManuelPC\Documents\Visual Studio Code\Python\Proyecto bd1\databases-inventory-app"

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "    Sistema de Inventario - Base de Datos 1" -ForegroundColor Cyan
Write-Host "    Universidad de Sonora" -ForegroundColor Cyan
Write-Host "    Estudiante: Manuel Munguia Rubio" -ForegroundColor Cyan
Write-Host "    Configurando Entorno Virtual" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan

# Cambiar al directorio del proyecto
Set-Location $projectPath

# Verificar si el entorno virtual existe
if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "Activando entorno virtual..." -ForegroundColor Green
    & "venv\Scripts\Activate.ps1"
    
    Write-Host "Entorno virtual activado!" -ForegroundColor Green
    Write-Host "Para ejecutar la aplicación: python src\main.py" -ForegroundColor Yellow
    Write-Host "Para desactivar: deactivate" -ForegroundColor Yellow
} else {
    Write-Host "Error: No se encontró el entorno virtual." -ForegroundColor Red
    Write-Host "Ejecuta primero: python -m venv venv" -ForegroundColor Yellow
}