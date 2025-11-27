# Script auxiliar para Code Runner
# Ejecuta Python usando el entorno virtual del workspace

param(
    [string]$FilePath
)

# Calcular la raiz del workspace (carpeta que contiene databases-inventory-app)
$ScriptDir = Split-Path -Parent $PSScriptRoot
$WorkspaceRoot = Split-Path -Parent $ScriptDir
$VenvPython = Join-Path $WorkspaceRoot ".venv\Scripts\python.exe"

if (Test-Path $VenvPython) {
    & $VenvPython -u $FilePath
} else {
    Write-Error "No se encontro el entorno virtual en: $VenvPython"
    Write-Host "Ejecuta setup.bat para crear el entorno virtual"
    exit 1
}
