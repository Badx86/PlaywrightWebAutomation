

def test_progress(page):
    page.goto("http://uitestingplayground.com/")
    page.get_by_role("link", name="Progress Bar").click()
    assert page.url == "http://uitestingplayground.com/progressbar", "Page URL does not match expected"

    page.locator("#startButton").click()
    page.wait_for_selector("#progressBar[aria-valuenow='75']")
    page.locator("#stopButton").click()

