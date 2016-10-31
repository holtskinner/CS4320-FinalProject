1.  Build user acceptance test scenarios for documented requirements on separate Wiki page, linked to all sprints.
2.  Build unit test scenarios
3.  Describe regression testing and your regression testing plan.
4.  Describe how your team will perform integration testing. What needs to be integrated? When?
5.  Describe which tests are for verification and which tests are for validation

# User Acceptance Test (UAT) Scenarios
 - The data scientists can search for manifests with keywords, the app returns the results or shows the reasons why no result is found. The data scientists can upload or download manifests, if it fails the reasons are also reported.
 - The system administrator can ban a data scientist when improper behaviors are frequently observed. The system admin will also leave the reason for this action, and the comment will be sent to the user. The system admin can also make change to a manifest when it is necessary, the reason is also given to the author.

# Unit Test Scenarios
## Login
 - If the user exists, the action continues.
 - If the user does not exist, further action is denied and the error message is shown.

## Verify File
 - If the file size and type is an acceptable format, the action is allowed.
 - If the file size is too big or the type is illegal, the action is denied.

## Search for Manifest
 - The system finds the record from database by matching the keywords.
 - The system returns an error message if no record is found.

## Upload
 - The file is stored in the database.

## Download
 - The required file is pulled from database and presented to the user.

## Edit/Delete Manifest
 - The manifest is changed and database is updated.

# Regression Testing
 - Regression testing is a type of software testing that verifies that software previously developed and tested still performs correctly even after it was changed or interfaced with other software.
 - In this system, a set of unit tests are prepared to cover all the functions of the software. The tests are run after every update or bug fixing.

# Integration Testing
 - At the end of each sprint, we will perform integration testing

## Data Scientist Uploads Manifest
 - If the user has not signed in, the action fails and the message "login first" shows on screen.
 - If the user signed in, but the file is not acceptable (file is too big or type is illegal), the action fails and the reminding message shows.
 - If the user signed in, and the file is valid, the action succeeds and the success message shows.

## Data Scientists Review Manifest
 - If the manifest is still valid, it is extracted from database and shows to the user.
 - If the manifest is no longer valid, the action fails and the message "manifest does not exist" shows.

## Data Scientists Search for Manifest
 - If the keyword matches any records in the database, they are shown to the user.
 - If the keyword cannot match any record in the database, the error message is shown to the user.

## Data Scientists Notify Changes to Other Users
 - If the user to be notified still exists, a notification is sent to the user, and it shows notification success.
 - If the user no longer exist, the message shows user not exist.

## System Admin Bans an Illegal Data Scientist
 - The data scientist account is transferred to the "banned" group. A notification is sent to the user as well as the reason for the ban.

## System Admin Deletes an Illegal Manifest
 - The manifest is deleted (moved to "trash" group), and a notification and reason are sent to its author.

# Summary:
 - The unit testing, integration testing and regression testing are for verification, the user acceptance test is for validation.
