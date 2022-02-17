# tx2ds
dsconverter is a decent sampler conversion tool for the .sfz format, it allows you to convert dspreset files to sfz for import to other applications or just to port to more formats.

<img src="/ds1.PNG" alt="Alt text" title="Optional title">

<img src="/ds2.PNG" alt="Alt text" title="Optional title">

# requirements
```bash
pip install git+git://github.com/widdershin/flask-desktop.git
```
```bash
pip install pyinstaller 
```
# Creating an exe 
```bash
pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" --icon=static/icon.ico --name=dsconverter main.py
```
