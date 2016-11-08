(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.modal').modal();
    $('#search').on('click', function(){
      $("#table-header").animate({ opacity: 0 }, 400);
      $("#table-header").animate({ height: 10 }, 400);
      var i = 0;
      for(i = 0 ; i < 1 ; i++){
        $('#manifest-table').append(
          '<thead>' +
              '<tr>' +
                  '<th data-field="title">Title</th>' +
                  '<th data-field="author">Author</th>' +
                  '<th data-field="dateCreated">Date Created</th>' +
                  '<th data-field="dateModified">Date Modified</th>' +
                  '<th data-field="comments">Comments</th>' +
                  '<th data-field="edit"></th>' +
                  '<th data-field="view"></th>' +
              '</tr>' +
          '</thead>' +
          '<tbody id="test">' +
            
          '</tbody>'
        );
      }
      for (var j = 0 ; j < 5 ; j++){
        $('#test').append(
          '<tr>' +
              '<td>dataset1</td>' +
              '<td>First Last</td>' +
              '<td>12-10-2015</td>' +
              '<td>3-1-2016</td>' +
              '<td>lorem ipsum</td>' +
              '<td><a>Edit</a></td>' +
              '<td><a>View</a></td>' +
            '</tr>' +
            '<tr>' +
              '<td>dataset2</td>' +
              '<td>First Last</td>' +
              '<td>12-13-2015</td>' +
              '<td>3-5-2016</td>' +
              '<td>lorem ipsum</td>' +
              '<td><a>Edit</a></td>' +
              '<td><a>View</a></td>' +
            '</tr>' +
            '<tr>' +
              '<td>dataset3</td>' +
              '<td>First Last</td>' +
              '<td>1-10-2015</td>' +
              '<td>4-8-2016</td>' +
              '<td>lorem ipsum</td>' +
              '<td><a>Edit</a></td>' +
              '<td><a>View</a></td>' +
            '</tr>'
        );
      }
    })
  }); // end of document ready
})(jQuery); // end of jQuery name space
