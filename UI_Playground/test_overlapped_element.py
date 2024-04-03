from playwright.sync_api import expect


def test_overlapped_element(page):
    page.goto("http://uitestingplayground.com/")
    page.get_by_role("link", name="Overlapped Element").click()
    assert page.url == "http://uitestingplayground.com/overlapped", "Page URL does not match expected"

    page.get_by_placeholder("Id").click()
    page.get_by_placeholder("Id").fill("86")

    page.mouse.wheel(0, 15)

    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("TestName")
