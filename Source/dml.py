from pymongo import MongoClient, TEXT#Mongodb functionality
from bson import objectid
import gridfs #file system functionality

#initialize to the collections that we want
client = MongoClient() 
db = client.test
fs = gridfs.GridFS(db)

m_col = db.Manifests #the collection of manifests
m_col.create_index( [("$**", TEXT)]) #ensure existance of index 

def oid_to_oid(oid):
    return objectid.ObjectId(oid)

def search(key, value):
    return m_col.find_one({key:value})

def search_manifest(lookup):
    ''' finds all manifests that match pattern provided and returns the cursor of results
    Returned value is a cursor that can be iterated through with a for loop '''
    return m_col.find(lookup) 

def search_by_all(to_find):
    ''' Finds all manifests that contain the search terms provided. '''
    lookup = { "$text": { "$search" : "\"" + to_find + "\"" } }
    return _col.find(lookup)

def search_by_title(to_find):
    ''' Finds all manifests that contain the title provided. Can be formatted upstream to be a
    regex.  '''
    lookup = { "manifests.manifest.researchObject.title" : {"$regex" : to_find , "$options": "i"}}
    return m_col.find(lookup)

def search_by_author(to_find):
    ''' Finds all manifests that contain the author provided. Can be formatted upstream to be a
    regex. This searches both the exterior creator field and the interior research object '''
    lookup = { "$or": [{ "manifests.manifest.creator" : {"$regex" : to_find , "$options": "i"}},
        {"creators.creator.name" : {"$regex" : to_find , "$options": "i"}}]
    }
    return m_col.find(lookup)

def search_by_date(to_find):
    ''' Finds all manifests that contain the date provided. Can be formatted upstream to be a
    regex. This searches both the exterior date field and the interior research object dates '''
    #we need to fix the date formatted
    query = to_find
    query = query.replace(" ", "")
    tokens = query.split("-")
    new_to_find = ""
    for token in tokens:
        new_to_find += "\s*" + token + "\s*-*"
    lookup = { "$or": [{ "dates.date.date" : {"$regex" : new_to_find , "$options": "i"}},
        {"manifests.manifest.researchObject.dates.date.date" : {"$regex" : new_to_find , "$options": "i"}}]
    }
    return m_col.find(lookup)

def search_by_description(to_find):
    ''' Finds all manifests that contain the description pattern provided. Can be formatted upstream to be a
    regex.  '''
    return [1]

def insert_manifest(manifest):
    ''' Insert given manifest if it exists. Returns True on success,
    or False on error (Failed document validation or no manifest was passed in) '''
    if(manifest): #basic error checking
        post_id = m_col.insert_one(manifest)
        ''' we have the object id for the new manifest, and we could return it if we like
        We could also return a tuple containing the Boolean value and the object id
        This way we could later do a lookup on the manifest, which would give us
        access to its metadata. As we do not have any important metadata at the 
        moment, we will just give a simple error check '''
        if(post_id):
            return True
    return False

def remove_manifest(oid):
    ''' Delete manifest specified by internal object id. Access this object id
    within the manifests metadata. returns True on succesful delete,
    or False if unable to delete (No matching oid, no oid provided)
    This also removes all files referenced by the manifest, so you do not
    have to call remove_all_files. You can if you like, nothing bad will happen,
    but it is not needed. '''
    if(oid):
        ''' Delete based on oid. Only can fail if the oid is invalid
        In which case, wow, we are corrupting our own metadata somewhere
        in the buisness logic or the view. At least we would know that we have
        an error '''
        remove_all_files(oid) #we no longer need these files
        result = m_col.delete_one({'_id': oid}) 
        if(result.deleted_count == 1):
            return True

    return False
        
def update_manifest(oid, manifest):
    ''' Updates the manifest specified by the given internal object id. 
    Changed to match the new manifest provided. Returns True
    if the document was succesfuly updated, and returns False if it
    failed. '''
    if(oid and manifest):
        #We actually want to remove the old manifest, and replace it with a new one
        old_doc = m_col.find_one_and_replace({"_id": oid}, manifest)
        #the old manifest was returned, so we can store an archive of manifests down
        #the road. For the monent, we will just check that something was there before
        if(old_doc):
            return True
    return False

def insert_file(file_in):
    ''' Adds the passed file to the file system, returning its internal id. 
    This should never really be called, as we want to use add_file instead '''
    return fs.put(file_in)

def delete_file(oid):
    ''' Removes the file specified by oid from the file system.
    This is another function that shouldn't really be called externally, 
    but we use it as an internal wrapper. Marignally better than calling
    delete as it will not raise an error, but will instead return true/false'''
    try:
        fs.delete(oid)
    except NoFile:
        return False
    return True

def get_file(f_oid):
    ''' Returns the file represented by f_oid,
    or None if no such file exists '''
    try:
        return fs.get(f_oid).read()
    except NoFile:
        return None 

def add_file(oid, file_in):
    ''' Attaches the given file to the manifest represented by oid.
    has a true/false return type to show result of addition. Can fail if
    given an invalid oid, or if there was no file provided.'''
    if(oid and file_in):
        #make sure that the manifest exists before we write the file to the database
        newOID = objectid.ObjectId(oid)
        doc = m_col.find_one({"_id": newOID}) 
        if(doc):
            file_id = fs.put(file_in)
            if(file_id):
                m_col.find_one_and_update({"_id": newOID}, {"$push": {"file_ids": file_id}}) #we need to add the file id to the file id list
                return "True"
            return "Did not insert file"
        return "Did not find document"
    return "Did not get oid or file_in" #we failed somewhere

def remove_file(m_oid, f_oid):
    ''' Removes from the manifest represented by m_oid the file represented by f_oid.
    m_oid is the internal object id of the manifest, f_oid is the internal object id
    of the file (You can get this from the file_ids array in the manifest metadata).
    This function will remove the file id from the metadata, and remove the file from
    the system. At this time, we do not allow manifest to share files, and each manifest
    points to its own instance of a file. As such, we can safely remove the file from
    the file system without worrying about other people losing data. returns true/false '''
    if(m_oid and f_oid):
        #ensure that m_oid points to a valid manifest
        #if f_oid doesn't point to a vaild file, we still want to remove it anyways
        doc = m_col.find_one({"_id": m_oid})
        if(doc):
            #remove file reference from manifest metadata
            m_col.find_one_and_update({"_id": m_oid}, {"$pull": {"file_ids": f_oid}})
            #remove the file from our file system
            #our return value doesn't really matter, as it is only false if the file did not exist
            did_delete = delete_file(f_oid)
            return True

    return False #we failed somewhere


def get_all_files(m_oid):
    ''' Returns a list of files associated with the manifest represented by m_oid.
    m_oid is a unique internal identifier for a manifest that can be accessed
    by the _id field within a manifest's metadata (i.e. example_manifes["_id"])
    Treat it as a read only list, as you don't really want to remove or delete from it
    if you want to do those things, you should call one of these functions instead)
    Honestly, you can write to or remove from it, but don't expect it to change
    anything in the file system. Returns an empty list if there are no files in the manifest,
    or None if the manifest does not exist'''
    if(m_oid):
        #ensure that manifest exists
        doc = m_col.find_one({"_id": m_oid})
        if(doc):
            #manifest exists, fill a list with files
            files = []
            for file_id  in doc["file_ids"]:
                files.append(fs.get(file_id).read())
            return files
    return None

def remove_all_files(m_oid):
    ''' Removes all files referenced by the manifest represented by m_oid.
    m_oid is a unique internal identifier for a manifest that can be accessed
    by the _id field within a manifest's metadata (i.e. example_manifes["_id"])
    The files are removed from the file system, and the references are removed
    from the manifest. The purpose of this function is not to tear down a manifest,
    as remove_manifest will call this function anyways. This is only used if you
    need to kill all of the files in the manifest for some reason. There are some
    edge cases where calling this might make more sense than calling remove_file,
    but it is mostly intended for internal use. No return value, as if this fails,
    the manifest didn't exist, so it doesn't have any files in it. '''
    if(m_oid):
        doc = m_col.find_one({"_id": m_oid})
        if(doc):
            for file_id in doc["file_ids"]:
                delete_file(file_id) #we don't care if this succeds or not
            #remove the references from the manifest
            m_col.find_one_and_update({"_id": m_oid}, {"$set": {"file_ids": {}}})