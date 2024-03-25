# ожидает запрос к изображению логотипа
# и затем переходит на страницу, после совершения перехода она выводит URL запрошенного изображения
# def test_event1(page):
#     with page.expect_request("**/*logo*.png") as first:
#         page.goto("https://wikipedia.org")
#         print(first.value.url)


# функция test_events регистрирует обработчики событий для отслеживания и печати URL отправленных и завершенных запросов
def test_events(page):
    # функция, которая выводит сообщение и URL каждого отправленного запроса
    def print_request_sent(request):
        print("Запрос отправлен: " + request.url)

    # функция, которая выводит сообщение и URL каждого завершенного запроса
    def print_request_finished(request):
        print("Запрос завершен: " + request.url)

    # регистрируем обработчик для события 'request', который будет вызывать функцию print_request_sent при каждом
    # отправленном запросе
    page.on("request", print_request_sent)
    # регистрируем обработчик для события 'request_finished', который будет вызывать функцию print_request_finished
    # при каждом завершенном запросе
    page.on("request_finished", print_request_finished)
    # Переходим на страницу Википедии
    page.goto("https://wikipedia.org")

    # удаляем обработчик события 'request_finished' чтобы он больше не вызывался
    page.remove_listener("request_finished", print_request_finished)
    # переходим на страницу OpenStreetMap
    page.goto("https://openstreetmap.org/")
