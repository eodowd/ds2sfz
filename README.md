# tx2ds
txconverter is a tx16wx sampler conversion tool for the decent sampler format, it allows you to design your velocity levels,keys and root notes and then convert out to a dspreset playable instrument file.

<img src="/ds1.PNG" alt="Alt text" title="Optional title">

<img src="/ds2.PNG" alt="Alt text" title="Optional title">

# requirements
```bash
pip install git+git://github.com/widdershin/flask-desktop.git
```
```bash
pip install pyinstaller (opptional)
```
# Creating an exe 
```bash
pyinstaller -w -F --add-data "templates;templates" --add-data "static;static" --icon=static/icon.ico --name=dsconverter main.py
```
