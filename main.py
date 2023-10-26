from github import Github
from datetime import datetime, timedelta

# Read GitHub access token from access_token.txt
with open('access_token.txt', 'r') as token_file:
    access_token = token_file.read().strip()

repository_name = 'cvs0/AutoCommit'  # Change to your repository
file_path = 'count.txt'  # Change to the file path in your repo

# Initialize GitHub
g = Github(access_token)

# Get the repository
repo = g.get_repo(repository_name)

# Get the existing file content and SHA
file = repo.get_contents(file_path)
content = int(file.decoded_content)
content += 1

# Calculate the date for the commit message
today = datetime.now()
commit_date = today - timedelta(days=1)

# Update and commit the file
commit_message = f'Incremented the value to {content}'
repo.update_file(file_path, commit_message, str(content), file.sha, branch='main')

print(f'Committed: {commit_message}')
