<!DOCTYPE html>
<html>
<?php include 'header.php'; ?>
  <body>
    <script>
        function onSignIn(googleUser) {
            var profile = googleUser.getBasicProfile();
            var id_token = googleUser.getAuthResponse().id_token;
            // TODO Send id_token to PHP Backend (This is in place of their user id for authentication)
        }
    </script>
    <?php
      include "nav.php";


    ?>

  </body>
</html>
