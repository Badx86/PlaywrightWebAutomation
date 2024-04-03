

def test_dynamic(page):
    page.goto("http://uitestingplayground.com/")
    page.get_by_role("link", name="Dynamic Table").click()
    assert page.url == "http://uitestingplayground.com/dynamictable", "Page URL does not match expected"

    bg_warn = page.locator(".bg-warning").inner_text().split(" ")[2]
    # print(bg_warn)
    table_list = page.locator("span[role=\'cell\']").all_inner_texts()
    chrome_values = table_list[table_list.index("Chrome"):
                               table_list.index("Chrome")+5]
    # print(chrome_values)
    table_value = 'None'
    for value in chrome_values:
        if '%' in value:
            table_value = value
            break
    # print(table_value)
    assert bg_warn == table_value, "Chrome CPU values do not match"

