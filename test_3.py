from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://youtube.com')
    page.screenshot(path='example2.png')
    browser.close()

"""$env:PLAYWRIGHT_BROWSERS_PATH="0"
playwright install chromium"""

