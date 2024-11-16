$syspython="python.exe"
# $ve="$HOME\.virtualenvs\ksilorama"
$ve=

# Debugging output
Write-Host "Removing build, dist, MANIFEST, ksilorama.egg-info, sandbox"
$paths = @("build", "dist", "MANIFEST", "ksilorama.egg-info", "sandbox")
foreach ($path in $paths) {
    if (Test-Path $path) {
        Write-Host "Path exists: $path"
    } else {
        Write-Host "Path does not exist: $path"
    }
}

# Removing specified paths
Write-Host "Removing build, dist, MANIFEST, ksilorama.egg-info, $ve, sandbox"
foreach ($path in $paths) {
    if (Test-Path $path) {
        Remove-Item -Recurse -Force $path
    }
}

# Debugging output
Write-Host "Removing __pycache__ directories"
& $syspython -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"

