<?php
    // connect to mongodb
    // database name: test
    // collection name: Manifests
	//$m = new MongoClient();
	$m = new Mongo();
    echo "Connection to database successfully";

/*
    $db = $m->selectDB('test');
    $collection=$db->selectCollection('Manifests');
    
    function insert_manifest($Manifest) {
	$collection.insert($Manifest);
    } 
    
    function update_manifest($object_id,$Manifest) {
	$collection.update($object_id,$Manifest);

    } 
    
    function remove_manifest($object_id){
        $collection.remove(array('ObjectId'=>$object_id));
    }

    // unit tests
    $Manifest = '{"name": "Justin"}';
    insert_manifest($Manifest);
    $ManifestQuery = array('name' => 'Justin');
    $cursor = $collection->find($ManifestQuery);
    var_dump($cursor);
*/
?>

