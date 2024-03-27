

def test_checkbox(page):

    page.goto("https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/examples/checkbox/")

    sprouts_checkbox = page.get_by_role("checkbox", name="Sprouts")
    lettuce_chackbox = page.get_by_role("checkbox", name="Lettuce")
    mustard_checkbox = page.get_by_role("checkbox", name="Mustard")
    tomato_checkbox = page.get_by_role("checkbox", name="Tomato")

    sprouts_checkbox.click()
    lettuce_chackbox.click()
    mustard_checkbox.dblclick()
    tomato_checkbox.click()

    assert sprouts_checkbox.is_checked() is True
    assert lettuce_chackbox.is_checked() is True
    assert mustard_checkbox.is_checked() is False
    assert tomato_checkbox.is_checked() is False


def test_type(page):

    page.goto("https://www.google.com/")

    page.get_by_label("Найти").click()
    page.get_by_label("Найти").type("social media")
    page.get_by_label("Найти").press("Enter")

