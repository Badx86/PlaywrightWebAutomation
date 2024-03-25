def test_download(page):
    # переходим на страницу скачивания PyCharm для Linux
    page.goto("https://www.jetbrains.com/pycharm/download/?section=linux")
    # находим вкладку для Linux и кликаем по ней
    page.get_by_role("tab", name="Linux").click()
    # начинаем ожидание события загрузки файла
    with page.expect_download() as download_info:
        # находим вторую ссылку для скачивания (предполагается, что она ведет к файлу) и кликаем по ней
        page.get_by_role("link", name="Download").nth(1).click()
    # получаем информацию о загруженном файле
    download = download_info.value
    # выводим в консоль путь к загруженному файлу
    print(download.path())
    # сохраняем загруженный файл по указанному пути на локальном диске
    download.save_as(r"C:\Users\мвидео\Pycharm\Playwright Web Automation\PlaywrightGuide\at.txt")
