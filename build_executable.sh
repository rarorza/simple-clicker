python -m venv venv
source ./venv/bin/activate
pip install pyinstaller
pyinstaller --onefile main.py
echo "builded succesfully"
