from playwright.sync_api import sync_playwright


def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()

    # настраиваем обработчик для события запроса, при каждом запросе будет выводиться метод и URL запроса
    page.on("request",
            lambda request: print(">>", request.method, request.url)
            )
    # настраиваем обработчик для события получения ответа, при каждом ответе будет выводиться статус ответа и URL
    page.on("response",
            lambda response: print(">>", response.status, response.url)
            )
    page.goto("https://python.org/")
    page.close()


with sync_playwright() as playwright:
    run(playwright)
