$syspython="python.exe"
$ve="$HOME\.virtualenvs\ksilorama"
$bin="$ve\Scripts"

# Upload to the test PyPI.
& $bin\twine.exe upload --repository testpypi dist\ksilorama-*
if(!$?) {
    write-host "  > Expect a 400 if package was already uploaded"
}

# cd elsewhere so we cannot import from local source.
mkdir -force sandbox | out-null
cd sandbox

# Create a temporary disposable virtualenv.
& $syspython -m venv --clear venv

# TODO: What is the windows/powershell equivalent of this:
#    version=$(grep __version__ ksilorama/__init__.py | cut -d' ' -f3 | tr -d "'")
# This:
$version = (Select-String -Path "../ksilorama/__init__.py" -Pattern "__version__" | ForEach-Object { $_.Line.Split(' ')[2].Trim("'") })

# Install the package we just uploaded.
# (--extra-index-url for this project's requirements)
venv\Scripts\python -m pip install --quiet --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple ksilorama==$version
# Import and use ksilorama from the temp virtualenv.
venv\Scripts\python.exe -c @"
import ksilorama;
ksilorama.init();
print(ksilorama.Fore.GREEN + 'OK Ksilorama ' + ksilorama.__version__ + ' from test pypi install.')
"@

cd ..
