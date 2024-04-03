from playwright.sync_api import expect


def test_sample_app(page):
    page.goto("http://uitestingplayground.com/")
    page.get_by_role("link", name="Sample App").click()
    assert page.url == "http://uitestingplayground.com/sampleapp", "Page URL does not match expected"

    page.get_by_placeholder("User Name").click()
    page.get_by_placeholder("User Name").fill("TestUser")
    page.get_by_placeholder("********").click()
    page.get_by_placeholder("********").fill("pwd")
    page.locator("#login").click()
    expect(page.locator("#loginstatus")).to_have_text("Welcome, TestUser!")
    page.locator("#logout").click()
    expect(page.locator("#loginstatus")).to_have_text("User logged out.")

