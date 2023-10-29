from github import Github
from datetime import datetime, timedelta
import time

with open('access_token.txt', 'r') as token_file:
    access_token = token_file.read().strip()

repository_name = 'cvs0/AutoCommit'
file_path = 'count.txt'

while True:
    g = Github(access_token)

    repo = g.get_repo(repository_name)

    file = repo.get_contents(file_path)
    content = int(file.decoded_content)
    content += 1

    today = datetime.now()

    commit_message = f'Incremented the value to {content}'
    repo.update_file(file_path, commit_message, str(content), file.sha, branch='main')

    print(f'Committed: {commit_message}')

    time.sleep(1)
