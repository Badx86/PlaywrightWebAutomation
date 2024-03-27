

def test_upload(page):

    page.goto("https://www.filemail.com/share/upload-file")
    page.get_by_text("Добавить файлы").click()
    page.locator("#addBtn").set_input_files(r"C:\Users\мвидео\Pycharm\Playwright Web Automation\PlaywrightGuide\test_1.txt")

    page.get_by_role("button", name=" Отправить").click()