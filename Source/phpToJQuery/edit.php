<!DOCTYPE html>
<html>
<head>
  <title>View Dataset</title>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"> </script>
<div id="includedHeader"></div>
<script>$("#includedHeader").load("header.php");</script>

<script>
function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    var id_token = googleUser.getAuthResponse().id_token;
    $("#author-name").value(profile.getName());
}
</script>
</head>
  <body>
    <div id="includedNav"></div>
    <script>$("#includedNav").load("nav.php");</script>
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
    <div id="includedFooter"></div>
    <script>$("#includedFooter").load("footer.php");</script>
  </body>
</html>
