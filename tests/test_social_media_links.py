import re
from playwright.sync_api import Page, expect, Playwright


def test_social_media_links(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    base_link = "https://germansp.com"
    
    #Create a page that can visit the links
    mypage = context.new_page()
    mypage.goto(base_link)
    
    #Github, linkedin, youtube, and dev.to links
    github_link = "https://github.com/an3wworldfool"
    #linkedin test was cancelled because you need to be authenticated, via username or password, not oauth
    #linkedin_link = "https://www.linkedin.com/in/german-soto-bab8ab226/"
    youtube_link = "https://www.youtube.com/@ANewWorldFool"
    devto_link = "https://dev.to/german_soto_d36c725384787"
    

    
    # Github locator
    with context.expect_page() as new_page_info:
        mypage.get_by_alt_text("github-logo").click()
    expect(new_page_info.value).to_have_url(re.compile(github_link))
    # Youtube locator
    with context.expect_page() as new_page_info:
        mypage.get_by_alt_text("yt-logo").click()
    expect(new_page_info.value).to_have_url(re.compile(youtube_link))
    
    # Dev.to locator
    with context.expect_page() as new_page_info:
        mypage.get_by_alt_text("devto-logo").click()
    expect(new_page_info.value).to_have_url(re.compile(devto_link))
    
    
    context.close()
    browser.close()