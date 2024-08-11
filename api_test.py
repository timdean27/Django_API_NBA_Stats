from playwright.sync_api import sync_playwright

def test_home_page():
    with sync_playwright() as p:
        # Launch a browser
        browser = p.chromium.launch(headless=False)  # Set headless=False to open the browser window
        context = browser.new_context()
        page = context.new_page()  # Open a new browser page

        # Go to the home page URL
        page.goto('http://127.0.0.1:8000/')
        print("Navigated to the home page.")

        # Verify the home page content
        content = page.content()  # Get the content of the page
        expected_text = 'Welcome to NBA Stats API'
        if expected_text in content:
            print(f"Home Page Test Passed: '{expected_text}' found on the page.")
        else:
            print(f"Home Page Test Failed: '{expected_text}' not found on the page.")

        browser.close()

def test_player_list():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # Go to the player list page
        page.goto('http://127.0.0.1:8000/api/players/')
        print("Navigated to the player list page.")

        # Verify the player list content
        content = page.content()
        if 'player' in content:
            print("Player List Test Passed: 'player' found in the content.")
        else:
            print("Player List Test Failed: 'player' not found in the content.")

        browser.close()

def test_player_detail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # Go to the player detail page with a specific player ID
        page.goto('http://127.0.0.1:8000/api/player/1/')
        print("Navigated to the player detail page.")

        # Verify the player detail content
        content = page.content()
        if 'id' in content:
            print("Player Detail Test Passed: 'id' found in the content.")
        else:
            print("Player Detail Test Failed: 'id' not found in the content.")

        browser.close()
        
if __name__ == "__main__":
    test_home_page()
    test_player_list()
    test_player_detail()
