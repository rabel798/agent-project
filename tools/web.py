from playwright.sync_api import sync_playwright

def browse(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        title = page.title()
        print("Page Title:", title)
        browser.close()

        #it opens a browser and goes to the url provided by the user, 
        #then it prints the title of the page and closes the browser.
       
