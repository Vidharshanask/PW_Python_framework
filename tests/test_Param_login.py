import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("Username,Password,expectedmessage,status",
    [("standard_user", "secret_sauce","Successful login", True),
     ("locked_out_user", "secret_sauce", "It is a locked out user", False),
     ("Test_data", "secret_sauce", "username is not correct",False)
    ])

def test_login_validation(Username, Password, expectedmessage, status):
 with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill(Username)
    page.get_by_placeholder("Password").fill(Password)
    page.get_by_role("button", name="Login").click()

    page.wait_for_timeout(3000)
    browser.close()
    print("Script finished!")


