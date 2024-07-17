import re
from playwright.sync_api import Page, expect

def test_counter_not_empty(page: Page):
    page.goto("https://germansp.com")

    locator = page.locator('span.counter')
    # Expect a title "to contain" a substring.
    expect(locator).not_to_be_empty()