<!DOCTYPE html>
<html lang="en">
  <head>
      <title>OCDX</title>
  <?php require_once 'header.php'; ?>
  </head>
<body>
    <?php include "nav.php"; ?>
    <main>
    <div id="index-banner">
        <div class="section">
            <div class="container">
                <h2 id="ocdx-title" class="header center teal-text text-lighten-2">Open Community Data Exchange</h2>
                <div class="row center">
                  <?php include "searchBox.php" ?>
                    <br>
                    <br>
                    <br>
                    <br>
                    <div id="searchResults">
                        <table id="manifest-table" class="highlight">

                        </table>
                    </div>
                </div>
            </div>
        </div>
      </main>
        <?php include 'footer.php'; ?>
</body>

</html>
