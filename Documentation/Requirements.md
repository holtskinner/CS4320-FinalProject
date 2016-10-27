# CS 4320 Final Project: Requirements Analysis & Software Design

## OCDX Engine

### [GitHub Repository](https://github.com/holtwashere/CS4320-FinalProject)

### Team 4 Members:
  - Holt Skinner *Project Manager*
  - Justin Hofer
  - Ali Raza
  - Bo Zhang
  - Bradley Rogers
  - Pramod Pudotha

---

# Table of Contents
- Requirements Analysis
  - User Descriptions
  - Use Cases
  - Functional Requirements
  - Non-functional Requirements
  - User Requirements
  - System Requirements
- Software Design
  - Sketches
  - Data
  - Change Log

---

# Requirements Analysis

## User Descriptions
*Rogers/Pudotha*

- **Data Scientist**
  - Uploads and downloads data
  - Conducts sophisticated and systematic analyses of data
  - Extracts insights from large data sets
- **System Administrator**
  - Review the uploaded data
  - Manage users

## Use Cases
*Skinner/Hofer*
- A Data Scientist can Browse by keyword for Manifest
- A Data Scientist can Search on Manifest
- A Data Scientist can Contribute to Existing Dataset
- A Data Scientist can Download Info
- A Data Scientist can Generate or Upload Manifest
- A Data Scientist can Save
- A Data Scientist can Upload Data Set

## Functional Requirements
_Pudotha/Skinner_
- The system will take a inputted manifest and place it into storage.
- The system will retrieve a manifest from storage and present it to a Data Scientist.

## Non-Functional Requirements
*Hofer/Raza*

### User Non-functional
- Be able to perform efficient searches based on keywords. Users should not wait more than about two seconds for a query to resolve.
- Be able to upload and update manifests.
- Process search, upload, and update requests, both into and out of Database Layer
- The user interface can accept and serve search, upload, and update requests.
- Be able to upload and download data files, storing them effiencty. These may be very large, so we cannot have wasted space.

## System Requirements
*Raza/Pudotha/Hofer*
- **Space Requirements**
	- The system must have enough physical space to handle extremely large data-sets.
	- The system may need to be a distributed system using clusters for efficiency.
- **Reliability Requirements**
	- If the system crashes, the data and any manipulations/analytics must be preserved.
- **Privacy Requirements**
	- The data access must be limited to authorized users only.
	- The system must enable secure data transfer over the internet
- **Web Server**
  - Web Server must provide reliable service for the appropriate amount of traffic that will be sent and received from the system.
- **Database Backend**
  - Database must be able to convert data into easily storable format, and return in original format.
- **Storage Array**
  - System must create intermediate backups and update logging to revert to earlier states if needed

## User Requirements
*Zhang/Rogers*
- Data scientists will be able to upload Manifest.
- Manifest can be reviewed by other data scientists.
- Data scientists can edit or delete their Manifest.
- Data scientists can search for Manifest they wish to view or test.
- Data scientists will be able to include special comments or suggestions on manifest
- Data scientists should be able to notify the changes or suggestions that improves manifest to other users
- System admins can ban an illegal data scientist
- System admins can delete an illegal manifest

---

# Software Design

## Sketches
*Skinner/Rogers*
- User can Browse by keyword for Manifest
- User can Contribute to Existing Dataset
- User can Download Info
- User can Search on Manifest

![Browse Screen](./Scan4.jpg)

![Dataset Information](./Scan5.jpg)

- User can Generate or Upload Manifest
- User can Save
- User can Upload Data Set

![Upload Screen](./Scan3.jpeg)

## Data
*Zhang/Hofer*

- **Members**
    - ID
    - name

- **OCDX_manifest**
    - author
    - date
    - size
    - category
    - version
    - modify_request

- **Users**
    - ID
    - name
    - email
    - phone

- **Login_attempts**
    - userID
    - date
    - attempts

<!-- ## Functions

## Database Structure -->

---

# Change Log

- Version 1.0: Pre-Implementation Design *10-16-2016*
- Version 1.1: Sprint 1 *10-31-2016*

<!-- ---

# Glossary -->
