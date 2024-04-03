from playwright.sync_api import expect


def test_scroll(page):
    page.goto("http://uitestingplayground.com/")
    page.get_by_role("link", name="Scrollbars").click()
    assert page.url == "http://uitestingplayground.com/scrollbars", "Page URL does not match expected"

    page.locator("section div").nth(3).click()
    page.mouse.wheel(80, 80)
    expect(page.locator(".btn-primary")).to_have_text("Hiding Button"), "Hiding Button not found"
    page.locator(".btn-primary").click()