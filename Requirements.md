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
	- Limit data access to authorized users only.

## User Requirements
-

## System Requirements
- **Web Server**
- **Database Backend**
- **Storage Array**
  - System must create intermediate backups and update logging to revert to earlier states if needed

<!-- Different Section-->
# Software Design
-
