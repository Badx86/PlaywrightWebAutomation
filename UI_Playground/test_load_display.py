from playwright.sync_api import expect


def test_load_display(page):
    page.goto("http://uitestingplayground.com/")
    page.get_by_role("link", name="Load Delay").click()
    assert page.url == "http://uitestingplayground.com/loaddelay", "Page URL does not match expected"

    delay_btn = page.get_by_role("button", name="Button Appearing After Delay")
    delay_btn.click()
    assert delay_btn.is_enabled()


def test_ajax(page):
    page.goto("http://uitestingplayground.com/")

    page.get_by_role("link", name="AJAX Data").click()
    assert page.url == "http://uitestingplayground.com/ajax", "Page URL does not match expected"

    page.get_by_role("button", name="Button Triggering AJAX Request").click()
    assert page.text_content(
        'text=Data loaded with AJAX get request.') is not None, "Text after AJAX request did not appear"
    expect(page.locator(".bg-success")).to_have_text("Data loaded with AJAX get request.", timeout=16000)


def test_clicking(page):
    page.goto("http://uitestingplayground.com/")

    page.get_by_role("link", name="Click").click()
    assert page.url == "http://uitestingplayground.com/click", "Page URL does not match expected"

    expect(page.locator(".btn-primary")).to_have_text("Button That Ignores DOM Click Event")
    page.locator(".btn-primary").click()
    expect(page.locator(".btn-success")).to_have_text("Button That Ignores DOM Click Event")
