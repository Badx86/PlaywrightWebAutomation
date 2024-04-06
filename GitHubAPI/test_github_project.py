import time
from playwright.sync_api import APIRequestContext, expect, Page


def test_create_project_card(
        gh_context: APIRequestContext,
        project_column_ids: list[str]) -> None:
    """
    Создает карточку в заданной колонке проекта и проверяет ее наличие

    :param gh_context: контекст запроса к API GitHub
    :param project_column_ids: список идентификаторов колонок проекта
    """
    now = time.time()
    card_name = f'A new task at {now}'

    logs = open('log.txt', 'w')
    # Создание карточки в первой колонке
    c_response = gh_context.post(
        f'projects/columns/{project_column_ids[0]}/cards',
        data={'note': card_name}
    )
    # Запись лога
    logs.write('\n' + 'Column IDs: ' + str(project_column_ids))
    logs.write('\n' + c_response.json()['note'])
    # Проверяем успешное создание карточки
    expect(c_response).to_be_ok()
    assert c_response.json()['note'] == card_name

    # Получение информации о созданной карточке
    card_id = c_response.json()['id']
    logs.write('\n' + 'Created Response: ' + str(c_response.json()))

    r_response = gh_context.get(f'/projects/columns/cards/{card_id}')
    logs.write('\n' + 'Retrieved Response: ' + str(r_response.json()))
    # Проверяем, что информация о карточке соответствует созданной
    expect(r_response).to_be_ok()
    assert r_response.json() == c_response.json()


def test_move_card(
        gh_context: APIRequestContext,
        gh_project: dict,
        project_column_ids: list[str],
        page: Page,
        gh_user: str,
        gh_password: str) -> None:
    """
    Перемещает карточку из одной колонки в другую и проверяет ее наличие.

    :param gh_context: контекст запроса к API GitHub
    :param gh_project: словарь с информацией о проекте
    :param project_column_ids: список идентификаторов колонок проекта
    :param page: экземпляр страницы Playwright
    :param gh_user: имя пользователя GitHub
    :param gh_password: пароль пользователя GitHub
    """
    logs = open("log2.txt", "w")
    source_col = project_column_ids[0]
    dest_col = project_column_ids[1]
    now = time.time()
    card_name = f"Move this card at {now}"

    # Создание карточки в исходной колонке
    c_response = gh_context.post(
        f'/projects/columns/{source_col}/cards',
        data={'note': card_name})
    expect(c_response).to_be_ok()
    # Авторизация на GitHub для работы с UI
    page.goto(f'https://github.com/login')
    page.locator('id=login_field').fill(gh_user)
    page.locator('id=password').fill(gh_password)
    page.locator('input[name="commit"]').click()
    # Переход на страницу проекта
    page.goto(f'https://github.com/users/{gh_user}/projects/{gh_project["number"]}')
    logs.write("\n" + "Project Data: " + str(gh_project))
    # Поиск карточки в исходной колонке и проверка ее видимости
    card_col = f'//div[@id="column-cards-{source_col}"]//p[contains(text(),' \
               f' "{card_name}")] '
    expect(page.locator(card_col)).to_be_visible()
    # Перемещение карточки в целевую колонку с помощью перетаскивания
    page.drag_and_drop(f'text="{card_name}"', f'id=column-cards-{dest_col}')
    # Проверка видимости карточки в целевой колонке
    card_col = f'//div[@id="column-cards-{dest_col}"]//p[contains(text(),' \
               f' "{card_name}")] '
    expect(page.locator(card_col)).to_be_visible()
    # Получение и проверка информации о перемещенной карточке
    card_id = c_response.json()["id"]
    r_response = gh_context.get(f'/projects/columns/cards/{card_id}')
    expect(r_response).to_be_ok()
    assert r_response.json()['column_url'].endswith(str(dest_col))
