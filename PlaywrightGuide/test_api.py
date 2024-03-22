import os
import json
import pytest
from typing import Generator
from dotenv import load_dotenv
from playwright.sync_api import Playwright, Page, APIRequestContext, expect


load_dotenv()
# Инициализация: получаем API token из переменных окружения
api_token = os.getenv('GITHUB_API_TOKEN')
# Убедимся, что token установлен
assert api_token, 'GITHUB_API_TOKEN is not set'

GITHUB_USER = 'Badx86'
assert GITHUB_USER, 'GITHUB_USER is not set'
# Имя репозитория для тестов
GITHUB_REPO = 'Test_API'


@pytest.fixture(scope='session')
def api_request_context(
        playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    # Заголовки для всех тестов через playwright
    headers = {
        "Accept": "application/vnd.github.v3+json",  # Указываем версию API GitHub
        "Authorization": f"token {api_token}",  # Авторизация с использованием токена
        "Content-Type": "application/json"  # Формат передачи данных - JSON
    }
    # Создаем контекст запроса с базовым URL и заголовками
    request_context = playwright.request.new_context(
        base_url="https://api.github.com", extra_http_headers=headers
    )
    # Предоставляем контекст для тестов
    yield request_context
    # Закрываем контекст после выполнения тестов
    request_context.dispose()


@pytest.fixture(scope='session', autouse=True)
def create_test_repo(
        api_request_context: APIRequestContext,
) -> Generator[None, None, None]:
    # Создание тестового репозитория
    data = json.dumps({"name": GITHUB_REPO})
    # Отправляем запрос на создание репозитория
    new_repo = api_request_context.post("/user/repos", data=data)
    assert new_repo.ok, f"Failed to create repo: {new_repo.status} {new_repo.text()}"

    yield
    # Удаление тестового репозитория после тестов
    if new_repo.ok:
        delete_repo = api_request_context.delete(f"/repos/{GITHUB_USER}/{GITHUB_REPO}")
        assert delete_repo.ok, f"Failed to delete repo: {delete_repo.status} {delete_repo.text()}"


# Тест для создания задачи 'Bug Report' в репозитории
def test_bug_report(api_request_context: APIRequestContext) -> None:
    # Отправляем запрос на создание задачи
    data = json.dumps({
        "title": "[Bug] report 1",
        "body": "Bug description"
    })
    new_issue = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
    )
    assert new_issue.ok, f"Failed to create issue: {new_issue.status} {new_issue.text()}"
    # Получаем список всех задач в репозитории
    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok, f"Failed to get issues: {issues.status} {issues.text()}"
    # Разбираем ответ
    issues_response = issues.json()
    """
    Использование next() с генераторным выражением для поиска первой подоходящей задачи эффективнее filter(lambda:),
    потому что:
    1. Прекращает поиск, как только находит первый подходящий элемент, не проходя весь список.
    2. Не создает промежуточный поиск в памяти, экономя ресурсы.
    """
    # Используем next для поиска созданной задачи
    issue = next((issue for issue in issues_response if issue["title"] == "[Bug] report 1"), None)
    assert issue, f"Bug issue not found"
    # Проверяем соотеветствие описания задачи
    assert issue["body"] == "Bug description"


def test_feature(api_request_context: APIRequestContext) -> None:
    data = json.dumps({
        "title": "[Feature] report 1",
        "body": "Feature description"
    })

    new_issue = api_request_context.post(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues", data=data
    )
    assert new_issue.ok, f"Failed to create feature: {new_issue.status} {new_issue.text()}"

    issues = api_request_context.get(f"/repos/{GITHUB_USER}/{GITHUB_REPO}/issues")
    assert issues.ok, f"Failed to get issues: {issues.status} {issues.text()}"

    issues_response = issues.json()
    issue = next((issue for issue in issues_response if issue["title"] == "[Feature] report 1"), None)
    assert issue, f"Feature issue not found"
    assert issue["body"] == "Feature description"
