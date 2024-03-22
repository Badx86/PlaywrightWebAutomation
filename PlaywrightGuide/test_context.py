from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    iphone_11 = p.devices["iPhone 11 Pro"]
    browser = p.webkit.launch(headless=False, slow_mo=5000)
    context1 = browser.new_context(
        **iphone_11,
        locale='de-DE',
        geolocation={'longitude': 12.492507, 'latitude': 41.889938},
        permissions=['geolocation']
    )
    context2 = browser.new_context()

    page1 = context1.new_page()
    page11 = context1.new_page()
    page2 = context2.new_page()

    page1.goto("https://youtube.com")
    page11.goto("https://google.com")
    page2.goto("https://cnn.com")

    browser.close()
