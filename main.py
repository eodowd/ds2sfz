import xml.etree.ElementTree as ET
from webui import WebUI
import os
from flask import Flask, render_template,flash, request, redirect
from werkzeug.utils import secure_filename
app = Flask(__name__)
ui = WebUI(app)


UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = {'dspreset','xml'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



header = """

<control>
default_path= // relative path of your samples

<global>
// parameters that affect the whole instrument go here.

// *****************************************************************************
// Your mapping starts here
// *****************************************************************************



"""

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            tree = ET.parse(file.filename)
            for gro in tree.iter('group'):
                name = gro.get('name')
                f = open('instrument {}'.format(name)+'.sfz','w')
                f.write(header +'\n')
                if gro.get('name') == name:
                    for neighbor in gro.iter('sample'):
                        getchi = neighbor.get('path')
                        root = neighbor.get('rootNote')
                        lokey = neighbor.get('loNote')
                        hikey = neighbor.get('hiNote')
                        hivel = neighbor.get('hiVel')
                        lovel = neighbor.get('loVel')

                        if(hivel == None and lovel == None):
                            hivel = 127
                            lovel = 0
                            f.write('<region>' + 'sample='+str(getchi)+' key= '+str(root)+' lokey= '+str(lokey)+' hikey= '+str(hikey)+' pitch_keycenter= '+str(root)+' hivel= '+str(hivel)+' lovel= '+str(lovel) +'\n')
                        else:
                            f.write('<region>' + 'sample=' + str(getchi) + ' key= ' + str(root) + ' lokey= ' + str(lokey) + ' hikey= ' + str(hikey) + ' pitch_keycenter= ' + str(root) + ' hivel= ' + str(hivel) + ' lovel= ' + str(lovel) + '\n')


                f.close()
        return render_template("info.html")

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404

if __name__ == '__main__':
    ui.run()
