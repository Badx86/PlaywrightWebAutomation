import re
from playwright.sync_api import expect


def test_navigater(page):
    page.goto("https://www.instagram.com")

    page.get_by_role("link", name="Забыли пароль?").click()
    page.get_by_placeholder("Эл. адрес, телефон или имя пользователя").click()
    page.wait_for_url("https://www.instagram.com/accounts/password/reset/")
    expect(page.get_by_text("Не удается войти?")).to_have_text("Не удается войти?")

    page.get_by_role("link", name="Создать новый аккаунт").click()
    page.wait_for_url("https://www.instagram.com/accounts/emailsignup/")

    page.get_by_label("Моб. телефон или эл. адрес").click()
    page.get_by_label("Моб. телефон или эл. адрес").fill("stasure@gmail.com")

    page.get_by_label("Имя и фамилия").click()
    page.get_by_label("Имя и фамилия").fill("Stas Osipov")

    page.get_by_label("Имя пользователя").click()
    page.get_by_label("Имя пользователя").fill("b828927adx86")

    page.get_by_label("Пароль").click()
    page.get_by_label("Пароль").fill("qwerty666#")

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

    page.get_by_role("button", name="Далее").click()
    expect(page.get_by_text("Введите код подтверждения", exact=True)).to_have_text("Введите код подтверждения")
