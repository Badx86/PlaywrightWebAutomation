from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        viewport={'width': 1280, 'height': 1024},
    )

    context2 = browser.new_context(
        viewport={'width': 2560, 'height': 1440},
        device_scale_factor=2,
        locale='de-DE',
        timezone_id='Europe/Berlin',
    )

    page = context.new_page()
    page2 = context2.new_page()
    page.goto("https://discovery.com")
    page2.goto("https://youtube.com")
    page.pause()
    page2.pause()


with sync_playwright() as playwright:
    run(playwright)
