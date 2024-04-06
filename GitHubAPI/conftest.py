"""
GITHUB_USERNAME
$env:GITHUB_USERNAME="Badx86"
echo $env:GITHUB_USERNAME
GITHUB_PASSWORD
GITHUB_ACCESS_TOKEN
GITHUB_PROJECT_NAME
"""
import os
import pytest
from typing import Generator
from dotenv import load_dotenv
from playwright.sync_api import Playwright, APIRequestContext, expect

load_dotenv()


def _get_env_var(varname: str) -> str:
    """Получить переменную окружения или убедиться, что она установлена"""
    value = os.getenv(varname)
    assert value, f'{varname} is not set'
    return value


@pytest.fixture(scope='session')
def gh_username() -> str:
    """Получить имя пользователя GitHub из переменных окружения"""
    return _get_env_var('GITHUB_USERNAME')


@pytest.fixture(scope='session')
def gh_password() -> str:
    return _get_env_var('GITHUB_PASSWORD')


@pytest.fixture(scope='session')
def gh_token() -> str:
    return _get_env_var('GITHUB_ACCESS_TOKEN')


@pytest.fixture(scope='session')
def gh_project_name() -> str:
    return _get_env_var('GITHUB_PROJECT_NAME')


@pytest.fixture(scope='session')
def gh_context(
        playwright: Playwright,
        gh_token: str) -> Generator[APIRequestContext, None, None]:  # iterator, send type, return type
    """Создать контекст запроса Playwright для API GitHub с авторизацией"""
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f'token {gh_token}'
    }

    request_context = playwright.request.new_context(
        base_url='https://api.github.com',
        extra_http_headers=headers
    )

    yield request_context
    request_context.dispose()


@pytest.fixture(scope='session')
def gh_project(
        gh_context: APIRequestContext,
        gh_username: str,
        gh_project_name: str) -> dict:
    """Получить проект по имени для данного пользователя"""
    resource = f'/users/{gh_username}/projects'
    response = gh_context.get(resource)
    expect(response).to_be_ok()

    # Добавляем печать всего списка проектов, чтобы убедиться, что ответ не пустой
    print("Список проектов:", response.json())

    name_match = lambda x: x['name'] == gh_project_name

    filtered = filter(name_match, response.json())
    project = list(filtered)[0]
    assert project  # Убедиться, что проект был найден

    return project


@pytest.fixture()
def project_columns(
        gh_context: APIRequestContext,
        gh_project: dict) -> list[dict]:
    """Получить столбцы проекта GitHub"""
    response = gh_context.get(gh_project['columns_url'])
    expect(response).to_be_ok()

    columns = response.json()
    assert len(columns) >= 2
    return columns


@pytest.fixture()
def project_column_ids(project_columns: list[dict]) -> list[str]:
    """Извлечь ID столбцов из столбцов проекта"""
    return list(map(lambda x: x['id'], project_columns))
