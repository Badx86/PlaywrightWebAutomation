import pytest


@pytest.mark.only_browser("chromium")
def test_youtube(page):
    page.goto("https://www.youtube.com")
