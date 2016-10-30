<?php
    // connect to mongodb
    $m = new MongoClient();
    echo "Connection to database successfully";
    
    // select a database and use gridfs
    $db = $m->selectDB('test');
    $gridfs = $db->getGridFS();
    // upload a file
    if (isset($_POST['upload'])) {
        $id = $gridfs->storeUpload('example.txt',
            array(
                'file_id' => $example_id,
                'fileType' => $example_type,
                'fileSize' => $example_size
            ));
        echo "File uploaded!!";
    }
    // download a file
    if (isset($_POST['download'])) {
        $object = $gridfs->findOne(array(
            'file_id' => $example_id;
        ));
        readfile($object);
    }
?>
