1.  Build user acceptance test scenarios for documented requirements on separate Wiki page, linked to all sprints.
2.  Build unit test scenarios
3.  Describe regression testing and your regression testing plan.
4.  Describe how your team will perform integration testing. What needs to be integrated? When?
5.  Describe which tests are for verification and which tests are for validation

# User Acceptance Test(UAT) Scenatios
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
