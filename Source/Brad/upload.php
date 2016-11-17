<!DOCTYPE html>
<html>
<head>
  <title>OCDX Upload</title>
<?php include 'header.php'; ?>

<script>
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
    $("#author-name").value(profile.getName());
}
</script>
</head>
  <body>
    <?php include "nav.php"; ?>
    <main>
        <div class="container">
          <h2 class="center-align header teal-text text-lighten-2">Upload Manifest</h2>
            <form action="#">
              <div class="row">
                <div class="input-field">
                  <input id="manifest-title" type="text" class="validate">
                  <label for="manifest-title">Manifest Title</label>
                </div>
              </div>
              <div class="row">
                <div class="input-field">
                  <input id="author-name" type="text" class="validate">
                  <label for="author-name">Author Name</label>
                </div>
              </div>
              <div class="row file-field input-field">
                <div class="btn">
                  <span>Manifests</span>
                  <input multiple type="file">
                </div>
                <div class="file-path-wrapper">
                  <input class="file-path validate" type="text" required placeholder="Upload File">
                </div>
              </div>
              <div class="row file-field input-field">
                <div class="btn">
                  <span>Scripts</span>
                  <input multiple type="file">
                </div>
                <div class="file-path-wrapper">
                  <input class="file-path validate" type="text" optional placeholder="Upload File">
                </div>
              </div>
            </form>
        </div>
      </main>
      <?php include 'footer.php' ?>
  </body>
</html>
