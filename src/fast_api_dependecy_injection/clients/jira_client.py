class MockJIRA:
    def __init__(self, **kwargs):
        self._connection = None


class JiraClient:
    def __init__(self, jira_connection):
        self._connection = None

    def get_issues(self):
        return

    def create_issue(self):
        return

    def ping(self):
        return f"{__name__} is Working!!!"
