(function($) {
    $(function() {
    $('.button-collapse').sideNav();
    $('.modal').modal();

<<<<<<< HEAD
=======
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

>>>>>>> Skinnerh_sprint2
    $('#search').on('click', function(){

      $("#ocdx-title").animate({ opacity: 0}, 400).animate({ height: 10 }, 400);
      $('#manifest-table').empty().load("table.html").hide().fadeIn(800);
    })
  }); // end of document ready
})(jQuery); // end of jQuery name space
