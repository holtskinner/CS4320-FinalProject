(function($) {
    $(function() {
    $('.button-collapse').sideNav();
    $('.modal').modal();

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
        $('.edit-field').attr('readonly', false);
        $('.edit-field').css('border-bottom', '1px solid #26a69a')
        $(this).css('display', 'none');
        $('.save-cancel').css('display', 'inherit');
        
    });
    $('.save-cancel').on('click', function() {
        $('.edit-field').attr('readonly', true);
        $('.edit-field').css('border-bottom', '')
        $(this).css('display', 'none');
        $('#edit-button').css('display', 'inherit');
    });

    
    $.getJSON('sampleManifest.json', function(data) {
        console.log(data);
        $('#standardVersion').val(data.manifests.manifest.standardVersions);
        $('#id').val(data.manifests.manifest.id);
        $('#creator').val(data.manifests.manifest.creator);
        $('#dateCreated').val(data.manifests.manifest.dateCreated);
        $('#comment').val(data.manifests.manifest.comment);
        $('#title').val(data.manifests.manifest.researchObject.title);
        $('#abstract').val(data.manifests.manifest.researchObject.abstract);
        $('#abstract').trigger('autoresize');
//        var inputHeight = $('#size-tester').outerHeight(true);
//        var textareaHeight = $('#abstract').outerHeight(true);
//        if(textareaHeight <= (inputHeight * 2)){
//            $('#abstract').height(15 + inputHeight);
//       }
//        $('#abstract-wrapper').height('100px');
//        console.log(textareaHeight);
        $.each(data.manifests.manifest.researchObject.dates, function(key, value){
            var label;
            if(value.label == 'start'){label = 'Start';}
            else if(value.label == 'end'){label = 'End';}
            else if(value.label == 'retrieved'){label = 'Retrieved';}
            else if(value.label == 'created'){label = 'Created';}
            else{label = 'No Assertion';}
            var date = value.date;
            $('.date-placeholder').append('<div class="input-field col s6 m3"><input type="text" value="'+ date +'"><label class="active">'+ label +' Date</label></div>')
//            $('.label-wrapper .date-placeholder').append('<div class="row"><label class="edit-label">Date - '+ label +':</label></div>');
//            $('.input-wrapper .date-placeholder').append('<div class="row"><span class="edit-span"><input class="edit-input edit-field" value="'+ date +'" readonly/></span></div>')
        });
        $('#oversight').val(data.manifests.manifest.privacyEthics.oversight.label);
        $('#informedConsent').val(data.manifests.manifest.informedConsent);
        $('#anonymizedData').val(data.manifests.manifest.anonymizedData[0].label);
        $('#privacyConsiderations').val(data.manifests.manifest.privacyConsiderations);
        $('#narrative').val(data.manifests.provenance.narrative);
        $('#narrative').trigger('autoresize');
        $('#publication').val(data.manifests.publications[0].publication);
        $('#locationUrl').val(data.manifests.locations[0].location.url);
        $('#locationComment').val(data.manifests.locations[0].location.comment);
        var numFiles = $(data.manifests.files).length;
        console.log(numFiles);
        if(numFiles >= 1){
            $('#files-table').append(
                "<thead>" +
                    "<tr>" +
                        "<th data-field='file_title'>Title</th>" +
                        "<th data-field='file_abstract'>Abstract</th>" +
                        "<th data-field='format'>Format</th>" +
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
                    "<tr>" +
                        "<td>"+ data.manifests.files[i].file.name +"</td>" +
                        "<td>"+ data.manifests.files[i].format +"</td>" +
                        "<td>"+ data.manifests.files[i].abstract +"</td>" +
                        "<td>"+ data.manifests.files[i].size +"</td>" +
                        "<td>"+ data.manifests.files[i].url +"</td>" +
                        "<td>"+ data.manifests.files[i].checksum +"</td>" +
                    "</tr>" 
                );       
            }
        }
        else {}
        Materialize.updateTextFields();
        
        
    });
    window.onresize = function() {
        $('#abstract').trigger('autoresize');
        $('#narrative').trigger('autoresize');
    }

  }); // end of document ready
})(jQuery); // end of jQuery name space