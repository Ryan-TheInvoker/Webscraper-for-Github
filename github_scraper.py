import requests
from bs4 import BeautifulSoup

def get_user_info(username):
    url = f"https://github.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        user_data = {}

        # Extract user data from the GitHub profile page
        # For example, get user's full name, bio, followers, etc.

        return user_data
    else:
        return None

def get_repository_info(repo_name):
    url = f"https://github.com/{repo_name}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        repo_data = {}

        # Extract repository data from the GitHub repository page
        # For example, get repository's description, stars, forks, etc.

        return repo_data
    else:
        return None