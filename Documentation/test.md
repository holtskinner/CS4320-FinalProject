1.  Build user acceptance test scenarios for documented requirements on separate Wiki page, linked to all sprints.
2.  Build unit test scenarios
3.  Describe regression testing and your regression testing plan.
4.  Describe how your team will perform integration testing. What needs to be integrated? When?
5.  Describe which tests are for verification and which tests are for validation

# User Acceptance Test(UAT) Scenarios
 - The data scientists can search for manifests with keywords, the app returns the results or shows the reasons why no result is found. The data scientists can upload or download manifests, if it fails the reasons are also reported. o 
 - The system admin can ban an illegal data scientist when improper behaviors are frequently observed. the system admin will also leave the reason for this action, and the comment will be sent to the user.The system admin can also make change to a manifest when it is necessary, the reason is also given to the author.

# Unit Test Scenarios
## login 
 - If the user exist, the action continues.
 - If the user does not exist, further action is denied and the error message is shown.

## verify file
 - If the file size and type is ok, the action is allowed.
 - If the file size is too big or the type is illegal, the action is denied.

## search for manifest
 - The system finds the record from database by matching the keywords.
 - The system returns error message if no record is found.

## upload
 - The file is stored to database

## download 
 - The required file is pulled from database

## edit/delete manifest
 - The manifest is changed and database is updated.

# Regression Testing
 - Regression testingis a type of software testing that verifies that software previously developed and tested still performs correctly even after it was changed or interfaced with other software. 
 - In our case, a set of unit tests are prepared to cover all the functions of the software. The tests are run after every update or bug fixing. 

# Integration Testing
 - At the end of each sprint, we will perform integration testing
## Data scientists upload Manifest
 - If the user has not signed in, the action fails and the message "login first" shows on screen.
 - If the user signed in, but the file is not acceptable (file is too big or type is illegal), the action fails and the reminding message shows.

 - if the user signed in, and the file is valid, the action succeeds and the success message shows.

## Data scientists review manifest
 - If the manifest is still valid, it is extracted from database and shows to the user.
 - If the manifest is no longer valid, the action fails and the message "manifest does not exist" shows.

## Data scientists search for manifest
 - If the keyword match any records in database, they are shown to the user.
 - If the keyword cannot match any record in database, the error message is shown to the user.

## Data scientists notify changes to other users
 - If the user to be notified still exist, a notification is sent to the user, and it shows notification success.
 - If the user no longer exist, the message shows user not exist.

## System admin ban an illegal data scientist
 - The data scientist account is transferred to the "banned" group. A notification is sent to the user as well as the reason.

## System admin delete an illegal manifest
 - The manifest is deleted (move to "trash" group), and a notification and reason are sent to its author.

# Summary:
 - The unit testing, ingegration testing and regression testing are for verification, the user acceptance test is for validation 
