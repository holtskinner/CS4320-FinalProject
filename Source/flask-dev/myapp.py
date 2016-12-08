from flask import Flask, render_template, request, jsonify, send_from_directory
from dml import insert_manifest, search_manifest, add_file
from werkzeug.utils import secure_filename
from pymongo import MongoClient, TEXT
import os

client = MongoClient() 
db = client.test
m_col = db.File #the collection of manifests
m_col.create_index( [("$**", TEXT)]) #ensure existance of index 

UPLOAD_FOLDER = '/var/www/flask-dev/uploads/'
ALLOWED_EXTENSIONS = set(['json'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
@app.route("/index.html")
def renderIndex():
    return render_template('index.html')

@app.route("/browse.html")
def renderBrowse():
	result = search_manifest({})
	return render_template('browse.html', result = result)

@app.route("/upload.html", methods=['GET', 'POST'])
def renderUpload():
	if request.method == 'POST':
		result = insert_manifest(request.form.to_dict())
		if(not result):
			return "Insertion failed"
		else:
			return render_template('browse.html')
	else:
		return render_template('upload.html')

@app.route("/edit.html")
def renderEdit():
	return render_template('edit.html')

@app.route("/profile.html")
def renderProfile():
	return render_template('profile.html')

@app.route("/uploadFile.html", methods=['GET'])
def uploadFile():
		return render_template('uploadFile.html')

@app.route("/handleFileUpload.html", methods=['GET', 'POST'])
def handleUpload():
	if request.method == 'POST':
		if 'file' not in request.files:
			return "no file provided"
		file = request.files['file']
		if file.filename == '':
			return "no file provided"
		if file:
			filename = secure_filename(file.filename)
			fileInfo = {}
			fileInfo["uid"] = request.form['oid']
		 	fileInfo['file'] = filename
		 	oid = request.form['oid']
		 	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		 	#return type(fileInfo)
		 	post_id = m_col.insert_one(dict(fileInfo))
		 	return (jsonify(fileInfo))
	else:
		return render_template('index.html')

@app.route("/uploads/<filename>")
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/uploads.html", methods=['GET', 'POST'])
def viewFile():
	if request.method == 'POST':
		uid = request.form['id']
		doc = m_col.find_one({"uid": uid})
		file = doc['file']
		filePath = UPLOAD_FOLDER + file
		return render_template("edit.html", filePath=file)
		#return send_from_directory(app.config['UPLOAD_FOLDER'], file)
	else:
		return render_template('index.html')

@app.route("/search.html", methods=['GET', 'POST'])
def searchManifests():
	if request.method == 'POST':
		key = request.form['searchCategory']
		value = request.form['search']
		return key
		#result = m_col.find_one({key:value})
		#return render_template('search.html', result = result)
	else:
		return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
