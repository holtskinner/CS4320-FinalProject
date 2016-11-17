from dml import insert_manifest, remove_manifest, update_manifest, search_manifest

to_insert = {
	"manifests": {
		"manifest": {
			"standardVersions": "ocdxManifest schema v.1",
			"id": "https: //datahub.io/dataset/iDas",
			"creator": "Ali Raza",
			"dateCreated": "2016 - 10 - 27",
			"comment": "First test manifest",
			"researchObject": {
				"title": "iDAS Manifest",
				"abstract": "Data collected at the Interdisciplinary Data Analytics and Search lab at the University of Missouri by Computer Science researchers and Data Scientists.",
				"dates": {
					"date": {
						"date": "2005 - 04 - 27",
						"label": "start"
					}
				}
			},
			"privacyEthics": {
				"oversight": {
					"label": "No assertion"
				}
			},
			"informedConsent": "No assertion",
			"anonymizedData": {
				"label": "No assertion"
			},
			"privacyConsiderations": "No assertion"
		},
		"provenance": {
			"narrative": "The Interdisciplinary Data Analytics and Search (iDAS) lab is one of the many research labs operating out of The University of Missouri, Columbia. As the name implies, iDAS combines researcher across departments to achieve  solutions to problems in academia. Founded in 2005 by Dr. Chi-Ren Shyu, iDAS researchers are primarily Computer Scientist, but the lab also works with Medical Doctors, Biologist, and Statisticans."
		},
		"publications": {
			"publication": "No assertion"
		},
		"locations": {
			"location": {
				"url": "",
				"comment": ""
			}
		},
		"files": {
			"file": {
				"name": "iDAS - data.csv"
			},
			"format": ".csv",
			"abstract": "Metadata for 5000 records collected",
			"size": "No assertion",
			"url": "No assertion",
			"checksum": "No assertion"
		},
		"permissions": "No assertion"
	},
	"dates": {
		"date": {
			"date": "2014 - 02 - 15"
		},
		"label": "Created"
	},
	"creators": {
		"creator": {
			"name": "Chi-Ren Shyu",
			"role": {
				"label": "Other"
			}
		},
		"type": {
			"label": "No assertion"
		},
		"contact": "cshyu@wikimedia.org"
	}
}

to_replace = {
	"manifests": {
		"manifest": {
			"standardVersions": "ocdxManifest schema v.1",
			"id": "https: //datahub.io/dataset/sociallyCompute",
			"creator": "Sean Goggins",
			"dateCreated": "2016 - 08 - 13",
			"comment": "Second test manifest",
			"researchObject": {
				"title": "Socially Compute Manifest",
				"abstract": "Data mined from socail networks for the purpose of consumer trend analytics.",
				"dates": {
					"date": {
						"date": "1992 - 03 - 11",
						"label": "start"
					}
				}
			},
			"privacyEthics": {
				"oversight": {
					"label": "No assertion"
				}
			},
			"informedConsent": "no assertion",
			"anonymizedData": {
				"label": "No assertion"
			},
			"privacyConsiderations": "No assertion"
		},
		"provenance": {
			"narrative": "Socially Compute is an ongoing project aiming to analyze trends of everyday people to make meaningful connections."
		},
		"publications": {
			"publication": "No assertion"
		},
		"locations": {
			"location": {
				"url": "",
				"comment": ""
			}
		},
		"files": {
			"file": {
				"name": "Socially Compute - sc.csv"
			},
			"format": ".csv",
			"abstract": "Metadata for 15000 records collected over two decades",
			"size": "No assertion",
			"url": "No assertion",
			"checksum": "No assertion"
		},
		"permissions": "No assertion"
	},
	"dates": {
		"date": {
			"date": "2016 - 10 - 28"
		},
		"label": "Created"
	},
	"creators": {
		"creator": {
			"name": "Sean Goggins",
			"role": {
				"label": "Other"
			}
		},
		"type": {
			"label": "No assertion"
		},
		"contact": "sg@wikimedia.org"
	}
}

#Insert the first test manifest
test = insert_manifest(to_insert)
if(not test):
    print("Bad insert")
else:
    print("Good insert")

#Ensure thata the manifest was inserted properly
found = search_manifest({})[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
    print("Match")
else:
    print("No Match")

#Update to Second manifest
test = update_manifest(found['_id'], to_replace)
if(not test):
    print("Bad update")
else:
    print("Good update")

#Ensure good manifest update
found = search_manifest({})[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
    print("Did not replace")
elif(found['creators']['contact'] == to_replace['creators']['contact']):
    print("Good Replace")
else:
    printf("replace corruption")

#remove the manifest
test = remove_manifest(found['_id'])
if(not test):
    print("Bad remove")
else:
    print("Good remove")
