import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_valid_login(page):
    login_pg = LoginPage(page)
    login_pg.navigate()
    login_pg.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
        ("invalid_user", "secret_sauce", "Username and password do not match"),
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
    ]
)
def test_login_failure_scenarios(page, username, password, expected_error):
    login_pg = LoginPage(page)
    login_pg.navigate()
    login_pg.login(username, password)

    expect(login_pg.error_message).to_contain_text(expected_error)