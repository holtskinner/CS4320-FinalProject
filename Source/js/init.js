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
        $('#cancel-button').css('display', 'inherit');
    });
    $('#cancel-button').on('click', function() {
        $('.edit-field').attr('readonly', true);
        $('.edit-field').css('border-bottom', '')
        $(this).css('display', 'none');
        $('#edit-button').css('display', 'inherit');
    });
  }); // end of document ready
})(jQuery); // end of jQuery name space
