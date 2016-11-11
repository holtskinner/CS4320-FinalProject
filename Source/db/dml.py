from pymongo import MongoClient #Mongodb functionality

#initialize to the collections that we want
client = MongoClient() 
db = client.test

m_col = db.Manifests #the collection of manifests

def search_manifest(lookup):
    ''' finds all manifests that match pattern provided and returns the cursor of results
    Returned value is a cursor that can be iterated through with a for loop '''
    return m_col.find(lookup) 

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
    or False if unable to delete (No matching oid, no oid provided) '''
    if(oid):
        ''' Delete based on oid. Only can fail if the oid is invalid
        In which case, wow, we are corrupting our own metadata somewhere
        in the buisness logic or the view. At least we would know that we have
        an error '''
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
        if(old_doc[0]):
            return True
    return False