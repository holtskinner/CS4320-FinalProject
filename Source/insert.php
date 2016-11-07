<?php
    // connect to mongodb
    $m = new MongoClient();
    echo "Connection to database successfully";

    // select a database and use gridfs
    $db = $m->selectDB('test');
    $collection=$db->selectCollection('Manifests');
    
    function insert_manifest($Manifest) {
	$collection.insert($Manifest);

    } 

    $Manifest = '{"name": "Justin"}';
    insert_manifest($Manifest);
    
    function remove_manifest($objects_id){
    $collection.remove(array('ObjectsId'=>$objects_id));
}
?>

