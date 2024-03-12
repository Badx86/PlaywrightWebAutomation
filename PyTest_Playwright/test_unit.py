import pytest
import unittest
from playwright.sync_api import Page


class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    def test_foobar(self):
        self.page.goto("https://microsoft.com")
        self.page.get_by_label("Save up to $400 on Surface").click()
        assert self.page.evaluate("1 + 1") == 2
