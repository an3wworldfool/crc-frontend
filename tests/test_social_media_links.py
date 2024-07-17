import re
from playwright.sync_api import Page, expect, Playwright


def test_social_media_links(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    base_link = "file:///Users/germansoto/development/portfolio/index.html"
    
    #Create pages to visit each link
    #newpage_in = context.new_page()
    #newpage_in.goto(base_link)
    newpage_gh = context.new_page()
    newpage_gh.goto(base_link)
    newpage_yt = context.new_page()
    newpage_yt.goto(base_link)
    newpage_dt = context.new_page()
    newpage_dt.goto(base_link)
    
    #Github, linkedin, youtube, and dev.to links
    github_link = "https://github.com/an3wworldfool"
    #linkedin test was cancelled because you need to be authenticated, via username or password, not oauth
    #linkedin_link = "https://www.linkedin.com/in/german-soto-bab8ab226/"
    youtube_link = "https://www.youtube.com/@ANewWorldFool"
    devto_link = "https://dev.to/german_soto_d36c725384787"
    
    # Linkedin locator
    #newpage_in.locator('.linkedin-grid').click()
    #newpage_in.wait_for_timeout(10000)
    #expect(newpage_in).to_have_url(re.compile(linkedin_link))
    
    # Github locator
    newpage_gh.locator('.github-grid').click()
    expect(newpage_gh).to_have_url(re.compile(github_link))
    
    # Youtube locator
    newpage_yt.locator('.youtube-grid').click()
    expect(newpage_yt).to_have_url(re.compile(youtube_link))
    
    # Dev.to locator
    newpage_dt.locator('.devto-grid').click()
    expect(newpage_dt).to_have_url(re.compile(devto_link))
    
    
    context.close()
    browser.close()