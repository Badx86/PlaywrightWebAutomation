from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.wikipedia.org/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.get_by_label("Top languages").click()
    page.get_by_role("link", name="English 6,790,000+ articles").click()
    page.get_by_placeholder("Search Wikipedia").click()
    page.get_by_placeholder("Search Wikipedia").fill("dogs")
    page.get_by_role("link", name="Dogs in warfare Overview of").click()
    page.goto("https://en.wikipedia.org/wiki/Dogs_in_warfare#Logistics_and_communication")

    # ---------------------
    context.tracing.stop(path='trace.zip')
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
