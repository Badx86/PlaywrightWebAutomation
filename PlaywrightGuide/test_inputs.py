

def test_facebook(page):

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

