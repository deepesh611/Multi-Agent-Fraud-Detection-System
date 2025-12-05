if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python is not installed or not in the PATH."
    exit 1
}

if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
} else {
    Write-Host "Virtual environment already exists."
}

$pipPath = ".\.venv\Scripts\pip.exe"

if (-not (Test-Path $pipPath)) {
    Write-Error "pip not found at $pipPath. Virtual environment creation might have failed."
    exit 1
}

if (Test-Path "requirements.txt") {
    Write-Host "Upgrading pip..."
    & $pipPath install --upgrade pip
    
    Write-Host "Installing requirements..."
    & $pipPath install -r requirements.txt
    
    Write-Host "Setup complete. Activate the environment with: .\.venv\Scripts\Activate.ps1"
} else {
    Write-Warning "requirements.txt not found. Skipping package installation."
}
