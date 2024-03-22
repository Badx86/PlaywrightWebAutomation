import os
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


def test_auth(page):
    page.goto("https://github.com/login")

    page.get_by_label("Username or email address").click()
    page.get_by_label("Username or email address").fill(email)

    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(password)

    page.get_by_role("button", name="Sign in", exact=True).click()

    page.wait_for_url("https://github.com/")
    expect(page.get_by_role("heading", name="Home", exact=True))
