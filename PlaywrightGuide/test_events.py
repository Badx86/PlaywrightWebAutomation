# def test_event1(page):
#     with page.expect_request("**/*logo*.png") as first:
#         page.goto("https://wikipedia.org")
#         print(first.value.url)


def test_events(page):
    def print_request_sent(request):
        print("Request sent: " + request.url)

    def print_request_finished(request):
        print("Request finished: " + request.url)

    page.on("request", print_request_sent)
    page.on("request_finished", print_request_finished)
    page.goto("https://wikipedia.org")

    page.remove_listener("request_finished", print_request_finished)
    page.goto("https://openstreetmap.org/")

