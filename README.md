# Project Lien Removal Tool

This Python script automates the process of identifying and deleting liens from Google Cloud Platform (GCP) projects. It is designed to streamline the management of project liens, ensuring that unnecessary restrictions can be efficiently removed.
I needed this for a request to remove liens from a list of idle projects, that needed to be deleted. 

## Features

- **List Liens**: Retrieves all liens associated with a specified GCP project.
- **Delete Liens**: Removes the first lien found for each specified GCP project.
- **Delete Project**: Sets the GCP Project for deletion. Remove the comments to use this functionality

## Requirements

- Python 3.x
- Google Cloud SDK
- Google API Client Library for Python

## Setup

1. **Environment Setup**: Ensure Python 3.x is installed. Create a virtual environment and activate it:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
2. Install Dependencies: Install the required Python packages:
    pip install google-api-python-client

3. GCP Authentication: Authenticate your session with GCP:

gcloud auth application-default login

GCP Permissions
To successfully run this script, the executing account must have the following permissions in GCP:

resourcemanager.liens.list
resourcemanager.liens.delete

These permissions are typically included in roles like Project Owner or Project IAM Admin. Ensure the account has appropriate roles assigned.

Usage
Update the project_ids list in main.py with the IDs of the projects you wish to check and potentially remove liens from. Run the script:
Uncomment line 34-35 if you wish to use the delete project function.

python3 main.py

The script will log its operations, including liens found and deletions.

Unit Testing

Note I was unable to get this working with a mock project - the unit test will need to be updated with a real project to pass
I am not able to work on this at this time.

Unit tests cover the following functionalities:

List Liens: Test the retrieval of liens from a project to ensure the API call is correctly made and handled.
Delete Liens: Test the deletion process of a lien to verify the API call is correctly executed and the response is handled appropriately.

