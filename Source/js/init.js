(function($) {
    $(function() {
    $('.button-collapse').sideNav();
    $('.modal').modal();
    var prevValues;
    var prevValue;
    function onSignIn(googleUser) {
        var profile = googleUser.getBasicProfile();
        var id_token = googleUser.getAuthResponse().id_token;
        // TODO Send id_token to PHP Backend (This is in place of their user id for authentication)
        // $.ajax({
        //   type: "POST",
        //   url: 'insert.php',
        //   data:{
        //     userID: id_token
        //   }
        // });
        //Need url for insert
    }
    if (top.location.pathname === '/index.php')
    {
        $('#search').on('click', function(){
          $("#table-header").animate({ opacity: 0}, 400).animate({ height: 0 }, 400);
          $('#manifest-table').empty().load("table.html").hide().fadeIn(800);
        })
    }
    $('#edit-button').on('click', function() {
        prevValues = getJsonValues();
        $('.add-field').css('display', 'inherit');
        $('.editable').attr('readonly', false);
        $('.editable').css('border-bottom', '1px solid #26a69a');
        $('.editable').css('box-shadow', '0 1px 0 0 #26a69a');
        $(this).css('display', 'none');
        $('.save-cancel').css('display', 'inherit');
    });
        
    $('.editable').on('focus', function() {
        if($('.editable').is('[readonly]')){
        }
        else {
            prevValue = $(this).val();
            console.log("prev: " + prevValue);
        }
    });
    $('.editable').on('focusout', function(){
        if($('.editable').is('[readonly]')){
        }
        else {
            console.log('else');
            var curr = $(this).val();
            console.log("prev: " + prevValue);
            console.log("curr: " + curr);
            if(curr !== prevValue){
                
                $(this).css('border-bottom', '1px solid #fa6a74');
                $(this).css('box-shadow', '0 1px 0 0 #fa6a74');
            }
        }
    });
    
    $('#cancel-button').on('click', function(){
        appendJsonValues(prevValues);
    });
    
    $('.save-cancel').on('click', function() {
        $('.add-field').css('display', '');
        $('.editable').attr('readonly', true);
        $('.editable').css('border-bottom', '');
        $('.editable').css('box-shadow', '');
        $(this).css('display', 'none');
        $('#edit-button').css('display', 'inherit');
    });


    $.getJSON('sampleManifest.json', function(data) {
        appendJsonValues(data);

        Materialize.updateTextFields();      
    }); 

    window.onresize = function() {
        $('#abstract').trigger('autoresize');
        $('#narrative').trigger('autoresize');
    }

  }); // end of document ready

function getJsonValues() {
    var standardVersion = $('#standardVersion').val();
    var id = $('#id').val();
    var creator = $('#creator').val();
    var dateCreated = $('#dateCreated').val();
    var comment = $('#comment').val();
    var title = $('#title').val();
    var abstract = $('#abstract').val();
    var dateArray = [];
    $('.date-input').each(function(){
        dateArray.push({
            date: $(this).val(),
            label: $('label[for=' + $(this).attr('id') + ']').data('date-label')
        })
    });
    var oversight = $('#oversight').val();
    var informedConsent = $('#informedConsent').val();
    var anonymizedDataArray = [];
    $('.anonymized-data-input').each(function(){
        anonymizedDataArray.push({
            label: $(this).val()
        })
    });
    var privacyConsiderations = $('#privacyConsiderations').val();
    var narrative = $('#narrative').val();
    var publicationsArray = [];
    $('.publication-input').each(function(){
        publicationsArray.push({
            publication: $(this).val()
        })
    });
    var locationsArray = [];
    $('.location-input').each(function(){
        locationsArray.push({
            location: {
                url: $(this).val(),
                comment: $(this).siblings('label').text()
            }
        })
    });
    var filesArray = [];
    $('.file-input').each(function(){
        filesArray.push({
            file: {
                name: $(this).children('.file-name').text()
            },
            format: $(this).children('.file-format').text(),
            abstract: $(this).children('.file-abstract').text(),
            size: $(this).children('.file-size').text(),
            url: $(this).children('.file-url').text(),
            checksum: $(this).children('.file-checksum').text()
        })
    });
    var permission = $('#permission').val();
    var dates2 = $('#dates2').val();
    var dates2Label = $('#dates2Label').text();
    var creatorsArray = [];
    $('.creator-input').each(function(){
        creatorsArray.push({
            creator: {
                name: $(this).children('.creator-name').text(),
                role: {
                    label: $(this).children('.creator-role').text()
                }
            },
            type: {
                label: $(this).children('.creator-type').text()
            },
            contact: $(this).children('.creator-contact').text()
        })
    });

    var testObject = {
        "manifests":{
            "manifest": {
                "standardVersions": standardVersion,
                "id": id,
                "creator": creator,
                "dateCreated": dateCreated,
                "comment": comment,
                "researchObject": {
                    "title": title,
                    "abstract": abstract,
                    "dates": dateArray
                },
                "privacyEthics": {
                    "oversight": {
                        "label": oversight
                    }
                },
                "informedConsent": informedConsent,
                "anonymizedData": anonymizedDataArray,
                "privacyConsiderations": privacyConsiderations
            },
            "provenance": {
                "narrative": narrative
            },
            "publications": publicationsArray,
            "locations": locationsArray,
            "files": filesArray,
            "permissions": permission
        },
        "dates" : {
            "date": {
                "date": dates2
            },
            "label": dates2Label
        },
        "creators": creatorsArray
    };
    console.log(testObject);

    return testObject;
}

function appendJsonValues(data) {
    $('#standardVersion').val(data.manifests.manifest.standardVersions);
    $('#id').val(data.manifests.manifest.id);
    $('#creator').val(data.manifests.manifest.creator);
    $('#dateCreated').val(data.manifests.manifest.dateCreated);
    $('#comment').val(data.manifests.manifest.comment);
    $('#title').val(data.manifests.manifest.researchObject.title);
    $('#abstract').val(data.manifests.manifest.researchObject.abstract);
    $('#abstract').trigger('autoresize');
    $('.date-placeholder').empty();
    $('.date-placeholder').append('<div id="add-date" class="col s6 m3 add-field"><a class="waves-effect waves-light btn"><i class="material-icons left">add</i>New Date</a></div>');
    var dateCount = 0;
    $.each(data.manifests.manifest.researchObject.dates, function(key, value){
        var hiddenLabel = value.label;
        var shownLabel;
        if(value.label == 'start'){shownLabel = 'Start Date';}
        else if(value.label == 'end'){shownLabel = 'End Date';}
        else if(value.label == 'retrieved'){shownLabel = 'Retrieved Date';}
        else if(value.label == 'created'){shownLabel = 'Created Date';}
        else{shownLabel = 'No Assertion';}
        var date = value.date;
        $('#add-date').before('<div class="input-field col s6 m3"><input id="date-input-'+ dateCount +'" class="date-input editable" type="text" value="'+ date +'" readonly><label id="date-label-'+ dateCount +'" class="active date-label" data-date-label="'+ hiddenLabel +'" for="date-input-'+ dateCount +'">'+ shownLabel +'</label></div>');
        dateCount++;
    });
    $('#oversight').val(data.manifests.manifest.privacyEthics.oversight.label);
    $('#informedConsent').val(data.manifests.manifest.informedConsent);
    $('.anonymized-data-placeholder').empty();
    $.each(data.manifests.manifest.anonymizedData, function(key, value){
        var count = 0;
        var anonymizedData = value.label;
        $('.anonymized-data-placeholder').append('<div class="input-field col s12 l6"><input id="anonymized-data-input-'+ count +'" class="anonymized-data-input" type="text" value="'+ anonymizedData +'" readonly><label id="anonymized-data-label-'+ count +'" class="active anonymized-data-label">Anonymized Data</label></div>');
        count++;
    });
    $('#privacyConsiderations').val(data.manifests.manifest.privacyConsiderations);
    $('#narrative').val(data.manifests.provenance.narrative);
    $('#narrative').trigger('autoresize');
    $('.publications-placeholder').empty();
    $.each(data.manifests.publications, function(key, value){
        var count = 0;
        var publication = value.publication;
        $('.publications-placeholder').append('<div class="input-field col s12 l6"><input id="publication-input-'+ count +'" class="publication-input" type="text" value="'+ publication +'" readonly><label id="publication-label-'+ count +'" class="active publication-label">Publication</label></div>');
        count++;
    });
    $('.locations-placeholder').empty();
    $.each(data.manifests.locations, function(key, value){
        var count = 0;
        var label = value.location.comment
        var location = value.location.url;
        $('.locations-placeholder').append('<div class="input-field col s12 m6"><input id="location-input-'+ count +'" class="location-input" type="text" value="'+ location +'" readonly><label id="location-label-'+ count +'" class="active location-label">'+ label +'</label></div>');
        count++;
    });
    var numFiles = $(data.manifests.files).length;
    if(numFiles >= 1){
        $('#files-table').empty();
        $('#files-table').append(
            "<thead>" +
                "<tr>" +
                    "<th data-field='file_title'>Title</th>" +
                    "<th data-field='file_format'>Format</th>" +                        
                    "<th data-field='file_abstract'>Abstract</th>" +
                    "<th data-field='file_size'>Size</th>" +
                    "<th data-field='file_url'>URL</th>" +
                    "<th data-field='file_checksum'>Checksum</th>" +
                "</tr>" +
            "</thead>" +
            "<tbody id='files-body'>" +
            "</tbody>"
        );
        for(var i = 0 ; i < numFiles ; i++){
            $('#files-body').append(
                "<tr class='file-input'>" +
                    "<td class='file-name'>"+ data.manifests.files[i].file.name +"</td>" +
                    "<td class='file-format'>"+ data.manifests.files[i].format +"</td>" +
                    "<td class='file-abstract'>"+ data.manifests.files[i].abstract +"</td>" +
                    "<td class='file-size'>"+ data.manifests.files[i].size +"</td>" +
                    "<td class='file-url'>"+ data.manifests.files[i].url +"</td>" +
                    "<td class='file-checksum'>"+ data.manifests.files[i].checksum +"</td>" +
                "</tr>" 
            );       
        }
    }
    else {
        $('#files-table').append('<p>There are no files in this manifest</p>')
    }
    $('#permission').val(data.manifests.permissions);
    $('#dates2').val(data.dates.date.date);

    var numCreators = $(data.creators).length;
    if(numCreators >= 1){
        $('#creators-table').empty();
        $('#creators-table').append(
            "<thead>" +
                "<tr>" +
                    "<th data-field='creator_name'>Name</th>" +
                    "<th data-field='creator_role'>Role</th>" +                        
                    "<th data-field='creator_type'>Type</th>" +
                    "<th data-field='creator_contact'>Contact</th>" +
                "</tr>" +
            "</thead>" +
            "<tbody id='creators-body'>" +
            "</tbody>"
        );
        for(var j = 0 ; j < numCreators ; j++){
            $('#creators-body').append(
                "<tr class='creator-input'>" +
                    "<td class='creator-name'>"+ data.creators[j].creator.name +"</td>" +
                    "<td class='creator-role'>"+ data.creators[j].creator.role.label +"</td>" +
                    "<td class='creator-type'>"+ data.creators[j].type.label +"</td>" +
                    "<td class='creator-contact'>"+ data.creators[j].contact +"</td>" +
                "</tr>" 
            );       
        }
    }
    else {
        $('#files-table').append('<p>There are no files in this manifest</p>')
    }

    Materialize.updateTextFields();
}
})(jQuery); // end of jQuery name space