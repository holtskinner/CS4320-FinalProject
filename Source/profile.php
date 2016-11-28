<!DOCTYPE html>
<html>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"> </script>
<div id="includedHeader"></div>
<script>$("#includedHeader").load("header.php");</script>

<style media="screen">
  .img-circle {
    border-radius: 50%;
  }
  .row {
    font-size: 2rem;
  }
  label {
    font-size: 3rem;
  }
</style>

  <body>
    <div id="includedNav"></div>
    <script>$("#includedNav").load("nav.php");</script>
    <main>
      <div class="container center-align">
        <h2 class="header teal-text text-lighten-2">Profile</h2>
        <div class="row">
          <img id="profile-image" class="img-circle">
        </div>

        <label for="name">Name</label>
        <div id="name" class="row"></div>

        <label for="email">Email</label>
        <div id="email" class="row"></div>

        <label for="manifests">My Manifests</label>
        <div id="manifests" class="row">You have no manifests. :(</div>

      </div>
    </main>
  </body>
</html>
<script>
  function onSignIn(googleUser) {
      var profile = googleUser.getBasicProfile();

      //Display Info from Google
      $('#profile-image').attr('src', profile.getImageUrl());
      $("#name").html(profile.getName());
      $("#email").html(profile.getEmail());
  }
</script>
