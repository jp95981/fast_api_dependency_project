import requests


class GitlabClient:
    def __init__(self, session: requests.Session, gitlab_url: str, gitlab_token: str):
        self._session = session
        self._session.headers.update({"PRIVATE-TOKEN": gitlab_token})
        self._gitlab_url = gitlab_url

    def get_branches(self):
        return

    def get_commits(self):
        return

    def get_tags(self):
        return

    def get_releases(self):
        return

    def ping(self):
        print(f"{__file__} is Working!!!")
