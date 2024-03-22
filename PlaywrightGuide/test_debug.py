from playwright.sync_api import sync_playwright

# def test_microsoft(page):
#     page.goto("https://www.microsoft.com")
#     page.get_by_label("Shop Surface devices").click()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    print(page.title())
    page.pause()
    page.goto("https://www.cnn.com")
    browser.close()