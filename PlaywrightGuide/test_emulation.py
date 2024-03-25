from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.webkit.launch(headless=False)
    # создаем новый контекст браузера с заданным размером окна
    context = browser.new_context(
        viewport={'width': 1280, 'height': 1024},
    )

    # сСоздаем второй контекст браузера с другими параметрами: размер окна, масштаб, локаль и часовой пояс
    context2 = browser.new_context(
        viewport={'width': 2560, 'height': 1440},
        device_scale_factor=2,
        locale='de-DE',
        timezone_id='Europe/Berlin',
    )

    # открываем новую страницу в первом контексте и переходим на сайт discovery.com
    page = context.new_page()
    page.goto("https://discovery.com")
    # открываем новую страницу во втором контексте и переходим на сайт youtube.com
    page2 = context2.new_page()
    page2.goto("https://youtube.com")
    # останавливаем выполнение скрипта и ждем ввода пользователя
    page.pause()
    page2.pause()


with sync_playwright() as playwright:
    run(playwright)
