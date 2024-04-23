from github import Github
from datetime import datetime
import time

# Read the access token from a file
with open('access_token.txt', 'r') as token_file:
    access_token = token_file.read().strip()

# Define the repository and file path
repository_name = 'cvs0/AutoCommit'
file_path = 'count.txt'

# Create a GitHub instance
g = Github(access_token)

# Get the repository
repo = g.get_repo(repository_name)

while True:
    try:
        # Get the current content of the file
        file = repo.get_contents(file_path)
        content = int(file.decoded_content)

        # Increment the content
        content += 1

        # Update the file with the new content
        commit_message = f'Incremented the value to {content}'
        repo.update_file(file_path, commit_message, str(content), file.sha, branch='main')

        # Print a message
        print(f'Committed: {commit_message}')

    except Exception as e:
        print(f'An error occurred: {e}')

    # Wait for 1 second before the next iteration
    time.sleep(1)
