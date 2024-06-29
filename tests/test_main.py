import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from googleapiclient import discovery

# Add the parent directory to the Python path (assuming it's necessary)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import delete_project

class TestDeleteProject(unittest.TestCase):
  # Define a project ID
  # Replace 'project-id-123' with a valid project ID
  # I have not been able to get ynit testing to work against a mock project ID
  MOCK_PROJECT_ID = 'project-id-123'

  @patch('googleapiclient.discovery.build')
  def test_delete_project(self, mock_build):
    mock_project_api = MagicMock()
    mock_build.return_value = mock_project_api

    # Mock the delete method of the project API
    mock_project_api.projects().delete.return_value = MagicMock()

    # Call the delete_project function with the mock project ID
    delete_project(self.MOCK_PROJECT_ID)

    mock_build.assert_called_with('cloudresourcemanager', 'v1')
    mock_project_api.projects().delete.assert_called_with(projectId=self.MOCK_PROJECT_ID)
    mock_project_api.projects().delete().execute.assert_called()

  @patch('googleapiclient.discovery.build')
  def test_delete_project_exception(self, mock_build):
    mock_project_api = MagicMock()
    mock_build.return_value = mock_project_api
    mock_project_api.projects().delete().execute.side_effect = Exception('Test exception')

    # Use the mock project ID
    with self.assertRaises(Exception):
      delete_project(self.MOCK_PROJECT_ID)

    mock_build.assert_called_with('cloudresourcemanager', 'v1')
    mock_project_api.projects().delete.assert_called_with(projectId=self.MOCK_PROJECT_ID)
    mock_project_api.projects().delete().execute.assert_called()

if __name__ == '__main__':
  unittest.main()
