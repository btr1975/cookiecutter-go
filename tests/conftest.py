import os
import sys
import pytest
base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))


@pytest.fixture
def bake_project_app_data() -> dict:
    options = {
        'git_repo_name': 'go-app',
        'git_url': 'https://github.com/some-username/python-with-cli',
    }

    return options
