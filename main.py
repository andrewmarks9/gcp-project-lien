from googleapiclient import discovery

def delete_project(project_id):
    project_api = discovery.build('cloudresourcemanager', 'v1') 
    project_api.projects().delete(projectId=project_id).execute()
    print(f"Deleted project {project_id}")

# List of project IDs
project_ids = ['project-id-1', 'project-id-2', 'project-id-3']

# Initialize the Cloud Resource Manager API client
service = discovery.build('cloudresourcemanager', 'v1')

file = open("lienlog.txt", "w")

# List liens
for project_id in project_ids:
    request = service.liens().list(parent='projects/' + project_id)
    file.write(f"Retrieving liens for project ID: {project_id}\n")
    response = request.execute()
    liens = response.get('liens', [])
    
    # Get the first lien name
    lien_name = liens[0].get('name') if liens else None

    if lien_name:
        file.write(f"Deleting lien: {lien_name}\n")
        # Delete lien
        request = service.liens().delete(name=lien_name)
        response = request.execute()
        
    # Delete project
    # Uncomment the following lines to delete the projects
    #delete_project(project_id)
    #file.write(f"Deleted project: {project_id}\ngit ")

file.close()