from playwright.sync_api import expect


def test_inputs(page):
    page.goto("http://uitestingplayground.com/")
    page.get_by_role("link", name="Text Input").click()
    assert page.url == "http://uitestingplayground.com/textinput", "Page URL does not match expected"

    page.locator(".form-control").click()
    page.locator(".form-control").fill("First try")
    page.locator(".btn-primary").click()
    expect(page.locator(".btn-primary")).to_have_text("First try")

    page.locator(".form-control").click()
    page.locator(".form-control").fill("Second try")
    page.locator(".form-control").press("Enter")
    expect(page.locator(".btn-primary")).not_to_have_text("Second try")

    page.locator(".form-control").click()
    page.locator(".form-control").fill("Third try")
    page.locator(".btn-primary").click()
    expect(page.locator(".btn-primary")).to_have_text("Third try")
