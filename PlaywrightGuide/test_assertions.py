from playwright.sync_api import Page, expect


def test_submitted(page: Page) -> None:
    page.goto("https://www.google.com")
    page.get_by_role("button", name="Настройки").click()
    expect(page.get_by_role("menuitem", name="Настройки поиска")).to_have_text("Настройки поиска")


def test_visible(page: Page) -> None:
    page.goto("https://www.google.com")
    page.get_by_role("button", name="Настройки").click()
    expect(page.get_by_role("link", name="Условия")).to_be_visible()
