from playwright.sync_api import sync_playwright
import time

def test_home_page():
    with sync_playwright() as p:
        # Launch a browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Go to the home page URL
        # page.goto('http://127.0.0.1:8000/', timeout=3000)
        page.goto('http://127.0.0.1:8000/')
        print("Navigated to the home page.")
        time.sleep(3)

        # Verify the home page content
        content = page.content()
        expected_text = 'Welcome to NBA Stats API'
        assert expected_text in content, f"Home Page Test Failed: '{expected_text}' not found on the page."
        print("Home Page Test Passed.")

        browser.close()

def test_player_list():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Go to the player list page
        page.goto('http://127.0.0.1:8000/api/players/')
        print("Navigated to the player list page.")
        time.sleep(3)

        # Verify the player list content
        content = page.content()
        assert 'player' in content, "Player List Test Failed: 'player' not found in the content."
        print("Player List Test Passed.")

        browser.close()

def test_player_detail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Go to the player detail page with a specific player ID
        page.goto('http://127.0.0.1:8000/api/player/1/')
        print("Navigated to the player detail page.")
        time.sleep(3)
        # Verify the player detail content
        content = page.content()
        assert 'id' in content, "Player Detail Test Failed: 'id' not found in the content."
        print("Player Detail Test Passed.")

        browser.close()

if __name__ == "__main__":
    test_home_page()
    test_player_list()
    test_player_detail()
