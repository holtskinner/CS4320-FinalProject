from flask import Flask, render_template, request, jsonify, send_from_directory
from dml import *

app = Flask(__name__)

'''
Route the default URL to the index page
'''
@app.route("/")
@app.route("/index.html")
def renderIndex():
    return render_template('index.html')

'''
Route the browse page. 
Send it an array holding all manifests
'''
@app.route("/browse.html")
def renderBrowse():
	result = search_manifest({})
	return render_template('browse.html', result = result)

'''
Route the upload page
If a post request is sent, insert the record into the database and then route to the browse page
If a get request is sent, display the contents of the upload pagge
'''
@app.route("/upload.html", methods=['GET', 'POST'])
def renderUpload():
	if request.method == 'POST':
		result = insert_manifest(request.form.to_dict())
		if(not result):
			return "Insertion failed"
		else:
			result = search_manifest({})
			return render_template('browse.html', result = result)
	else:
		return render_template('upload.html')

'''
Route the profile page
Add functionality to this
'''
@app.route("/profile.html")
def renderProfile():
	return render_template('profile.html')

'''
Route the upload file page
This page is where clicking on the upload manifest button on the browse page will take you to
This page should only be accessed if the user clicks the upload button on the browse page or else the file getting 
uploaded will not be tied to a proper manifest id, causing all sorts of problems.
'''
@app.route("/uploadFile.html", methods=['GET'])
def uploadFile():
		return render_template('uploadFile.html')

'''
This page is the action of the form that is submitted when a user inserts a file to a manifest
This page will link a manifest to a file and then redirect the user to the browse page
This URL should not be directly accessed by the user
'''
@app.route("/handleFileUpload.html", methods=['GET', 'POST'])
def handleUpload():
	if request.method == 'POST':
		if 'file' not in request.files:
			return "no file provided"
		file = request.files['file']
		oid = oid_to_oid(request.form['oid'])
		add_file(oid, file)
		result = search_manifest({})
		return render_template('browse.html', result = result)
	else:
		return render_template('index.html')

'''
Route the delete manaifest page.
A post request from the browse page will submit the manifest ID.
We will call a DML function that deletes manifest and all trails (associated files)
After this we will return to the browse page
'''
@app.route("/delete.html", methods=['GET', 'POST'])
def handleDelete():
	if request.method == 'POST':
		oid = oid_to_oid(request.form['id'])
		if remove_manifest(oid):
			result = search_manifest({})
			return render_template('browse.html', result = result)
	else:
		return render_template('index.html')

'''
Route the view manifest page. 
This is the page that comes up when the user clicks the view button on the browse page
'''
@app.route("/view.html", methods=['GET', 'POST'])
def handleView():
	if request.method == 'POST':
		oid = oid_to_oid(request.form['id'])
		files = get_all_files(oid)
		return render_template("view.html", files=files)
	else:
		return render_template("index.html")

'''
Figure out what is going on in here I might be able to delete all of this now 
this might get deleted
Route the upload page
Currently, a post request to this URL will lead to the edit page
I shoud probably route the edit page to a seperate URL
'''
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
'''
Route the search page
If the request is a get request, return to the indexx page
'''
@app.route("/search.html", methods=['GET', 'POST'])
def searchManifests():
	if request.method == 'POST':
		key = request.form['searchCategory']
		value = request.form['search']
		result = search(key, value)
		return render_template("search.html", result=result)
	else:
		return render_template('index.html')

@app.route("/edit.html", methods=['GET', 'POST'])
def viewManifest():
	if request.method == 'POST':
		data = request.form['json']
		return render_template("edit.html", data=data)
	else:
		return render_template("index.html")

# If the user tries to go to a non-existant page, they will be redirected to a custom 404 page
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404

# If the server malfunctions, the user will be directed to a custom 500 error page
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'),  500

'''
Run the application
'''
if __name__ == "__main__":
    app.debug = True
    app.run()
