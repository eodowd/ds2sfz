# ds2sfz
dsconverter is a decent sampler conversion tool for the .sfz format, it allows you to convert dspreset files to sfz for import to other applications or just to port to more formats.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/hhsFu8nNcj8/0.jpg)](https://www.youtube.com/watch?v=hhsFu8nNcj8)


# requirements
```bash
pip install git+git://github.com/eodowd/flask-desktop.git
```
```bash
pip install pyinstaller 
```
# Creating an .exe (windows 10)
```bash
pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" --icon=static/icon.ico --name=dsconverter main.py
```
# Creating an .app (mac os big sur)
```bash
pyinstaller -w -F --windowed --onedir --add-data "templates:templates" --add-data "static:static" --icon=static/icon.ico --name=dsconverter main.py
```
