# CS 4320 Final Project Requirements Analysis

### Skinner, Hofer, Raza, Zhang, Rogers, Pudotha

### 10-18-2016

## User Descriptions

## Use Cases
- User can Browse by keyword for Manifest
- User can Contribute to Existing Dataset
- User can Download Info
- User can Generate or Upload Manifest
- User can Save
- User can Search on Manifest
- User can Upload Data Set

## Functional Requirements
- **Database Backend**
  - The system will be able to perform efficient searches, using keywords.
  - The system should be able to upload and update manifests.
- **Business Logic**
  - Process search, upload, and update requests, both into and out of Database Layer
- **Front-End Framework**
  - Accept and serve search, upload, and update requests

## Non-Functional Requirements
- **Space Requirments**
	- The system must have enough physical space to handle extremly large data-sets.
	- We may need to implement a distributed system using clusters for efficiency.
- **Realiability Requirments**
	- If the system crashes, the data and any manipulations/analytics must be preserved.
- **Privacy Requirments**
	- The data access must be limited to authorized users only.
	- The system must enable secure data transfer over the internet

## User Requirements
- User will be able to upload Manifest.
- Manifest can be reviewed by others.
- User can edit or delete their Manifest.
- User can search for Manifest they are interested in. 

## System Requirements
- **Web Server**
  - Web Server must provide reliable service for the appropriate amount of traffic that will be sent and received from the system.
- **Database Backend**
  - Database must be able to convert data into easily storable format, and return in original format.
- **Storage Array**
  - System must create intermediate backups and update logging to revert to earlier states if needed

<!-- Different Section-->
# Software Design
-
