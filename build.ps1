$ve="$HOME\.virtualenvs\ksilorama"
$bin="$ve\Scripts"

& $bin\python.exe -m pip install --upgrade build
& $bin\python.exe -m build
