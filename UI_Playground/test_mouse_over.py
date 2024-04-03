from playwright.sync_api import expect


def test_mouse_over(page):
    page.goto("http://uitestingplayground.com/")
    page.get_by_role("link", name="Mouse Over").click()
    assert page.url == "http://uitestingplayground.com/mouseover", "Page URL does not match expected"

    page.get_by_text("Click me").click()
    expect(page.locator(".clickCount")).to_have_value("1")
    page.get_by_text("Click me").dblclick()
    expect(page.locator(".clickCount")).to_have_value("3")
