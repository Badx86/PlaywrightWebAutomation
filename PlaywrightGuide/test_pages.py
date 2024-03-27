from playwright.sync_api import expect


def test_page(page):
    page.goto("https://google.com")
    page.get_by_label("Найти").click()
    page.get_by_label("Найти").fill("Mike Tyson")
    page.get_by_label("Поиск в Google").first.click()

    print(page.url)


def test_page2(context):
    page = context.new_page()
    page1 = context.new_page()
    page.goto("https://google.com")
    page1.goto("https://google.com")
    page1.get_by_label("Найти").click()
    page1.get_by_label("Найти").fill("Mike Tyson")
    page1.get_by_label("Поиск в Google").first.click()


def test_page3(context):
    page = context.new_page()
    page.goto("https://www.rrc.texas.gov/resource-center/research/gis-viewer/gis-popup-blocker-test/#")

    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="RUN POPUP TEST").click()

    page1 = popup_info.value
    expect(page1.get_by_role("heading", name="Test Page")).to_have_text("Test Page")
    print(f'\nPopup URL: {page1.url}')
    page1.close()

    print(f'Page URL: {page.url}')