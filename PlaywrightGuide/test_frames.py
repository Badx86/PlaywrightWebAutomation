

def test_frame(page):
    page.goto("https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe")
    page.frame_locator("iframe[title=\"MDN Web Docs Interactive Example\"]").locator(
        ".cm-content > div:nth-child(8)").click()
    page.frame_locator("iframe[title=\"MDN Web Docs Interactive Example\"]").get_by_role("textbox").fill(
        "<iframe\n  id=\"inlineFrameExample\"\n  title=\"Inline Frame Example\"\n  width=\"300\"\n  height=\"200\"\n  "
        "src=\"https://www.openstreetmap.org/export/embed.html?bbox=-0.004017949104309083%2C51.47612752641776%2C0"
        ".00030577182769775396%2C51.478569861898606&layer=mapnik\">\n</iframe>\nMy favorite tool is playwright!")
