#Wildcard imports are a bad idea, so we import all individually
from dml import search_by_all, search_by_title, search_by_author, search_by_date, insert_manifest, remove_manifest, update_manifest, search_manifest, add_file, remove_file, get_all_files, remove_all_files, get_file
#Yes, we could do 
#from dml import *
#but this is bad practice, as it is very easy to accadentially rebind something, and it is hard to tell where something came from
#honestly, we should just use import dml then go dml.insert_manifest, but as this is a testing script, we can get away with it
#in our buisness logic, it should be import dml, then dml.insert_manifest

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

#search by full title
found = search_by_title("iDAS Manifest")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("Full title match")
else:
	print("Unable to match by full title")

#partial search
found = search_by_title("iDAS")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("partial title match")
else:
	print("Unable to match by partial title")

#lower case search
found = search_by_title("idas")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("lower case title match")
else:
	print("Unable to match by lower case title")

#second part search
found = search_by_title("Manifest")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("second part of title match")
else:
	print("Unable to match by second part of title")

#bad search
found = search_by_title("iDAS Manafest")
if(found.count() != 0):
	print("found a manifest that shouldn't exist")
else:
	print("Passed bad search test")

#search by full author, interior manifest
found = search_by_author("Ali Raza")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("Full author match, interior")
else:
	print("Unable to Full author match, interior")

#search by full author, exterior creator
found = search_by_author("Chi-Ren Shyu")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("Full author match, exterior")
else:
	print("Unable to Full author match, exterior")

#search by full author, interior manifest
found = search_by_author("AliRaza")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("Full author no spaces match, interior")
else:
	print("Unable to Full author no spaces match, interior")

#search by full author, exterior creator
found = search_by_author("Chi-RenShyu")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("Full author no spaces match, exterior")
else:
	print("Unable to Full author no spaces match, exterior")

#partial search, interior manifest
found = search_by_author("Raz")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("partial author match, interior")
else:
	print("Unable to partial author match, interior")

#partial search, exterior manifest
found = search_by_author("Ren")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("partial author match, exterior")
else:
	print("Unable to partial author match, exterior")

#lower case search, interior manifest
found = search_by_author("ali raza")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("lower case author match")
else:
	print("Unable to match by lower case author")

#lower case search, exterior manifest
found = search_by_author("chi-ren shyu")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("lower case author match")
else:
	print("Unable to match by lower case author")


#lower case search, interior manifest
found = search_by_author("ALI RAZA")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("upper case author match")
else:
	print("Unable to match by upper case author")

#lower case search, exterior manifest
found = search_by_author("CHI-REN SHYU")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("upper case author match")
else:
	print("Unable to match by upper case author")

#search by full author, interior manifest
found = search_by_author("Ali  Raza")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("extra spaces author match, interior")
else:
	print("Unable to extra spaces author match, interior")

#search by full author, exterior creator
found = search_by_author("Chi-Ren  Shyu")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("extra spaces author match, exterior")
else:
	print("Unable to extra spaces author match, exterior")


#bad search
found = search_by_author("iDAS")
if(found.count() != 0):
	print("found a manifest that shouldn't exist")
else:
	print("Passed bad search test")

#date searches
#search by full date, interior manifest
found = search_by_date("2005 - 04 - 27")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("Full date match, interior")
else:
	print("Unable to Full date match, interior")

#search by full date, exterior date
found = search_by_date("2014 - 02 - 15")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("Full date match, exterior")
else:
	print("Unable to Full date match, exterior")

#partial search, interior manifest
found = search_by_date("2005")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("partial date match, interior")
else:
	print("Unable to partial date match, interior")

#partial search, exterior manifest
found = search_by_date("2014")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("partial date match, exterior")
else:
	print("Unable to partial date match, exterior")

#no spaces case search, interior manifest
found = search_by_date("2005-04-27")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("no spaces date match")
else:
	print("Unable to match by no spaces date")

#no spaces search, exterior manifest
found = search_by_date("2014-02-15")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("no spaces date match")
else:
	print("Unable to match by no spaces date")

#extra spaces case search, interior manifest
found = search_by_date("2005  -  04  -  27")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("extra spaces date match")
else:
	print("Unable to match by no spaces date")

#extra spaces search, exterior manifest
found = search_by_date("2014  -  02  -  15")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("extra spaces date match")
else:
	print("Unable to match by no spaces date")

#bad search
found = search_by_date("2229")
if(found.count() != 0):
	print("found a manifest that shouldn't exist")
else:
	print("Passed bad search test")

#Search by all tests
found = search_by_all("ali")[0]
if(found['creators']['contact'] == to_insert['creators']['contact']):
	print("found from search by all")
else:
	print("did not find from a search by all")

#empty search
found = search_by_date("")
if(found.count != 0):
	print("Empty search returns manifests")
else:
	print("Empty search did not return a manifest")

#Update to Second manifest
found = search_manifest({})[0] #reset
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

#add a test file
if(add_file(found['_id'], "This a file that is a string")):
	print("Added string file")
else:
	print("Did not add string file")

#reset our internal manifest
found = search_manifest({})[0]

#get the file we Added
found_file = get_file(found["file_ids"][0])
if(found_file):
	print(found_file)
else:
	print("We did not find any files")

#remove the file
if(remove_file(found["_id"], found["file_ids"][0])):
	print("We removed the string file")
else:
	print("We did not remove the string file")

#add several files
if(add_file(found['_id'], "This is the first sting file")):
	print("Added 1st string file")
else:
	print("Did not add 1st string file")
if(add_file(found['_id'], "This is the second sting file")):
	print("Added 2nd string file")
else:
	print("Did not add 2nd string file")
if(add_file(found['_id'], "This is the third sting file")):
	print("Added 3rd string file")
else:
	print("Did not add 3rd string file")
found = search_manifest({})[0]

#get the files
found_files = get_all_files(found["_id"])
if(found_files):
	for found_file in found_files:
		print(found_file)
else:
	print("unable to get files")


#remove the manifest
test = remove_manifest(found['_id'])
if(not test):
    print("Bad remove")
else:
    print("Good remove") 
