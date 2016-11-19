from flask import request, Flask
from dml import insert_manifest, remove_manifest, update_manifest, search_manifest

@app.route('/add', methods=['POST'])
def addManifest():
	result = insert_manifest(request.form['JSON'])
	if(not result):
		print("Insertion failed")
	else:
		print("Manifest succesfully inserted!")

@app.route('/update', methods=['POST'])
def updateManifest()
	result = update_manifest(request.form['oid'], request.form['JSON'])
	if(not result):
		print("Insertion failed")
	else:
		print("Manifest succesfully inserted!")

@app.route('/delete', methods=['POST'])
def removeManifest()
	result = remove_manifest(request.form['oid'])
	if(not result):
		print("Insertion failed")
	else:
		print("Manifest succesfully inserted!")
