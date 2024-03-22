def test_download(page):
    page.goto("https://www.jetbrains.com/pycharm/download/?section=linux")
    page.get_by_role("tab", name="Linux").click()
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download").nth(1).click()
    download = download_info.value
    print(download.path())
    download.save_as(r"C:\Users\мвидео\Pycharm\Playwright Web Automation\PlaywrightGuide\at.txt")
