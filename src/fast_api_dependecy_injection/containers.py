import requests
from dependency_injector import containers, providers

from fast_api_dependecy_injection.clients.db_client import DBClient
from fast_api_dependecy_injection.clients.gitlab_client import GitlabClient
from fast_api_dependecy_injection.clients.jira_client import JiraClient, MockJIRA
from fast_api_dependecy_injection.settings import Settings


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.from_dict(Settings().dict())

    # Gitlab
    gitlab_session = providers.Singleton(
        requests.Session,
    )
    gitlab_client = providers.Singleton(
        GitlabClient,
        session=gitlab_session,
        gitlab_url=config.GITLAB_URL,
        gitlab_token=config.GITLAB_TOKEN
    )

    # Jira
    jira_connection = providers.Singleton(
        MockJIRA,
        server=config.JIRA_URL,
        token_auth=(config.JIRA_URL, "x"),
    )
    jira_client = providers.Singleton(
        JiraClient,
        jira_connection=jira_connection
    )

    # DB
    db_client = providers.Singleton(
        DBClient,
        db_url=config.db_url()
    )

    # Slurm
    slurm_client = providers.Singleton(
        requests.Session,
    )

    wiring_config = containers.WiringConfiguration(
        modules=[
            ".routers.default_route",
            ".routers.encoder_upgrader_router",
            ".routers.generate_router",
            ".routers.handler_one"
        ]
    )
