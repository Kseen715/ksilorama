$syspython="python.exe"
$ve="$HOME\.virtualenvs\ksilorama"

remove-item -r -fo * -I build,dist,MANIFEST,ksilorama.egg-info,$ve,sandbox
& $syspython -Bc "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"

