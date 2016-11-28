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
        <div class="header-row">
          <h5 id="dataset-title" class="header center teal-text text-lighten-2">Manifest</h5>
          <a id="edit-button" class="waves-effect waves-light btn-flat"><i class="material-icons left">mode_edit</i>Edit</a>
          <a id="cancel-button" class="waves-effect waves-light btn-flat"><i class="material-icons left">delete</i>Cancel</a>
        </div>
        <div class="row">
          <form class="col s12">
            <div class="label-wrapper">
              <div class="row"><label class="edit-label">Title:</label></div>
              <div class="row"><label class="edit-label">Creator:</label></div>
              <div class="row"><label class="edit-label">Date Created:</label></div>
              <div class="row"><label class="edit-label">Comment:</label></div>
              <div class="row"><label class="edit-label">Abstract:</label></div>
              <div class="row"><label class="edit-label">Start Date:</label></div>
              <div class="row"><label class="edit-label">Oversight:</label></div>
              <div class="row"><label class="edit-label">Informed Consent:</label></div>
              <div class="row"><label class="edit-label">Privacy Considerations:</label></div>
              <div class="row"><label class="edit-label temp">Narrative:</label></div>
              <div class="row"><label class="edit-label">Publication:</label></div>
              <div class="row"><label class="edit-label">Label:</label></div>
            </div>
            <div class="input-wrapper">
              <div class="row"><span class="edit-span"><input id="readonly-check" class="edit-input edit-field" value="Socially Computed Manifest" readonly/></span></div>
              <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="Sean Goggins" readonly/></span></div>
              <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="2016-08-13" readonly/></span></div>
              <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="Second test manifest" readonly/></span></div>
              <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="Data mined from social networks for the purpose of consumer trend analytics." readonly/></span></div>
              <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="1992-03-12" readonly/></span></div>
              <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="No assertion" readonly/></span></div>
              <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="No assertion" readonly/></span></div>
              <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="No assertion" readonly/></span></div>
              <div class="row"><span class="edit-span"><textarea class="edit-input edit-field" rows="8" readonly>The Interdisciplinary Data Analytics and Search (iDAS) lab is one of the many research labs operating out of The University of Missouri, Columbia. As the name implies, iDAS combines researcher across departments to achieve  solutions to problems in academia. Founded in 2005 by Dr. Chi-Ren Shyu, iDAS researchers are primarily Computer Scientist, but the lab also works with Medical Doctors, Biologist, and Statisticans.</textarea></span></div>
              <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="No assertion" readonly/></span></div>
              <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="Another input field" readonly/></span></div>
            </div>
<!--
            <div class="row">
              <label class="edit-label">Title:</label>
              <span class="edit-span"><input class="edit-input" value="Socially Compute Manifest"/></span>
            </div>
            <div class="row">
              <label class="edit-label">Creator:</label>
              <span class="edit-span"><input class="edit-input"/ value="Sean Goggins"></span>
            </div>
            <div class="row">
              <label class="edit-label">Date Created:</label>
              <span class="edit-span"><input class="edit-input" value="2016-08-13"/></span>
            </div>
            <div class="row">
              <label class="edit-label">Comment:</label>
              <span class="edit-span"><input class="edit-input" value="Second test manifest"/></span>
            </div>
            <div class="row">
              <label class="edit-label">Abstract:</label>
              <span class="edit-span"><input class="edit-input" value="Data mined from social networks for the purpose of consumer trend analytics."/></span>
            </div>
            <div class="row">
              <label class="edit-label">Start Date:</label>
              <span class="edit-span"><input class="edit-input" value="1992-03-12"/></span>
            </div>
-->

            <div class="files-wrapper">
              <label>Files</label>
              <div class="files-table-wrapper">
                <table class="bordered">
                  <thead>
                    <tr>
                      <th data-field="file_title">Title</th>
                      <th data-field="file_abstract">Abstract</th>
                      <th data-field="file_size">Size</th>
                      <th data-field="file_url">URL</th>
                      <th data-field="file_checksum">Checksum</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>iDAS - data.csv</td>
                      <td>Metadata for 5000 records collected</td>
                      <td>4 KB</td>
                      <td>No assertion</td>
                      <td>No assertion</td>
                    </tr>
                    <tr>
                      <td>Socially Compute - sc.csv</td>
                      <td>Metadata for 15000 records collected over two decades</td>
                      <td>624 Bytes</td>
                      <td>No assertion</td>
                      <td>No assertion</td>
                    </tr>
                    <tr>
                      <td>More - data.csv</td>
                      <td>Metadata for 10000 records</td>
                      <td>6 KB</td>
                      <td>No assertion</td>
                      <td>No assertion</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="contributors-wrapper">
              <div class="label-wrapper">
                <div class="row"><label class="edit-label">Additional Contributors:</label></div>
              </div>
              <div class="input-wrapper">
                <table class="bordered">
                  <tbody>
                    <tr>
                      <td>Holt Skinner</td>
                      <td>Grant funder</td>
                      <td>Individual</td>
                      <td>cshyu@wikimedia.org</td>
                    </tr>
                    <tr>
                      <td>Justin Hofer</td>
                      <td>Primary Investigator</td>
                      <td>Government</td>
                      <td>jh773@missouri.gov</td>
                    </tr>
                    <tr>
                      <td>Ali Raza</td>
                      <td>Other</td>
                      <td>Individual</td>
                      <td>aar456@missouri.gov</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <!--
              <div class="input-wrapper">
                <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="Holt Skinner" readonly/></span></div>
                <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="Justin Hofer" readonly/></span></div>
                <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="Ali Raza" readonly/></span></div>
                <div class="row"><span class="edit-span"><input class="edit-input edit-field" value="Brad Rogers" readonly/></span></div>
              </div>
              -->
            </div>
          </form>
        </div>
      </div>
    </main>
    <?php include 'footer.php' ?>
  </body>
</html>