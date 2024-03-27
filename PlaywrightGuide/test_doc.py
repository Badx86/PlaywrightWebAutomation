import re
from playwright.sync_api import expect


def test_instagram(page):
    page.goto("https://www.instagram.com")

    page.get_by_role("link", name="Забыли пароль?").click()
    page.get_by_placeholder("Эл. адрес, телефон или имя пользователя").click()
    page.wait_for_url("https://www.instagram.com/accounts/password/reset/")
    expect(page.get_by_text("Не удается войти?")).to_have_text("Не удается войти?")

    page.get_by_role("link", name="Создать новый аккаунт").click()
    page.wait_for_url("https://www.instagram.com/accounts/emailsignup/")
    page.screenshot(path=r"C:\Users\мвидео\Pycharm\Playwright Web Automation\PlaywrightGuide\ScreenShots\sc1.png")
    page.get_by_label("Моб. телефон или эл. адрес").click()
    page.get_by_label("Моб. телефон или эл. адрес").fill("stasure@gmail.com")

    page.get_by_label("Имя и фамилия").click()
    page.get_by_label("Имя и фамилия").fill("Stas Osipov")

    page.get_by_label("Имя пользователя").click()
    page.get_by_label("Имя пользователя").fill("b828927adx86")

    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("qwerty666#")

    page.screenshot(path=r"C:\Users\мвидео\Pycharm\Playwright Web Automation\PlaywrightGuide\ScreenShots\sc2.png")

    page.locator("div").filter(has_text=re.compile(r"^Регистрация$")).nth(1).click()

    page.wait_for_url("https://www.instagram.com/accounts/emailsignup/")
    expect(page.get_by_text("Укажите дату вашего рождения")).to_have_text("Укажите дату вашего рождения")

    page.locator("span").filter(
        has_text=re.compile(r"^январьфевральмартапрельмайиюньиюльавгустсентябрьоктябрьноябрьдекабрь$")).get_by_role(
        "combobox").select_option("11")
    page.locator("span").filter(
        has_text=re.compile(r"^123456789101112131415161718192021222324252627282930$")).get_by_role(
        "combobox").select_option("21")
    page.get_by_role("combobox").nth(2).select_option("2005")

    page.screenshot(path=r"C:\Users\мвидео\Pycharm\Playwright Web Automation\PlaywrightGuide\ScreenShots\sc3.png")

    page.get_by_role("button", name="Далее").click()
    expect(page.get_by_text("Введите код подтверждения", exact=True)).to_have_text("Введите код подтверждения")


def test_facebook(browser):
    # browser -> context -> page

    # context = browser.new_context(record_video_dir="Videos/",
    #                               record_video_size={"width": 1280,
    #                                                  "height": 720}
    #                               )

    context = browser.new_context()
    context.tracing.start(snapshots=True, sources=True)

    page = context.new_page()
    page.goto('https://www.facebook.com/register')

    page.get_by_label("Имя").click()
    page.get_by_label("Имя").fill("Max")

    page.get_by_label("Фамилия").click()
    page.get_by_label("Фамилия").fill("Payne")

    page.get_by_label("Номер мобильного телефона или эл. адрес").click()
    page.get_by_label("Номер мобильного телефона или эл. адрес").fill("+37412345678")

    page.get_by_label("Новый пароль").click()
    page.get_by_label("Новый пароль").fill("new_password")

    page.get_by_label("День").select_option("10")
    page.get_by_label("Месяц").select_option("10")
    page.get_by_label("Год").select_option("2001")

    page.get_by_text("Другое").click()
    page.get_by_label("Укажите, как к вам обращаться").select_option("6")
    page.get_by_label("Пол (необязательно)").click()
    page.get_by_label("Пол (необязательно)").fill("Оно")

    page.get_by_role("button", name="Регистрация").click()

    context.tracing.stop(path="Tracing.zip")