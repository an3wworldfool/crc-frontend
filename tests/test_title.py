import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://germansp.com")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("German Portfolio"))