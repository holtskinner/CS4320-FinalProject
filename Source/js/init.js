(function($) {
    $(function() {

        $('.button-collapse').sideNav();
        $('.modal').modal();

        function onSignIn(googleUser) {
            var profile = googleUser.getBasicProfile();
            var id_token = googleUser.getAuthResponse().id_token;
            // TODO Send id_token to PHP Backend (This is in place of their user id for authentication)
        }
    }); // end of document ready
})(jQuery); // end of jQuery name space
