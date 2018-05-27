Set-Location $PSScriptRoot

Start-Process powershell {
  virtualenv venv
  ./venv/scripts/activate
  Set-Location .\backend
  pip install -r requirements.txt
  deactivate; Read-Host
}

Start-Process powershell {
  Set-Location .\frontend
  npm install; Read-Host
}