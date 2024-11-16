$ve="$HOME\.virtualenvs\ksilorama"
$bin="$ve\Scripts"

# Upload to PyPI.
& $bin\twine.exe upload dist\ksilorama-*.tar.gz dist\ksilorama-*.whl
