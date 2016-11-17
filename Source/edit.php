<!DOCTYPE html>
<html>
<head>
  <title>View Dataset</title>
<?php include 'header.php'; ?>

<script>
function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    var id_token = googleUser.getAuthResponse().id_token;
    $("#author-name").value(profile.getName());
}
</script>
</head>
  <body>
    <?php include "nav.php"; ?>
    <main>
      <div class="wrapper">
        <div class="row">
          <form class="col s12">           
            <div class="row">
              <label class="edit-label">Title:</label>
              <span class="edit-span"><input class="edit-input"/></span>
            </div>
            <div class="row">
              <label class="edit-label">Creator:</label>
              <span class="edit-span"><input class="edit-input"/></span>
            </div>
            <div class="row">
              <label class="edit-label">Date Created:</label>
              <span class="edit-span"><input class="edit-input"/></span>
            </div>
            <div class="row">
              <label class="edit-label">Comment:</label>
              <span class="edit-span"><input class="edit-input"/></span>
            </div>
          </form>
        </div>
      </div>
    </main>
    <?php include 'footer.php' ?>
  </body>
</html>