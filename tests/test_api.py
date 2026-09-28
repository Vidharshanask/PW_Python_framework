import pytest
from playwright.sync_api import Playwright, expect

BASE_URL = "https://reqres.in"

HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": "free_user_3Jlv9kNa39NX6CdTPegSCNK4BNn"
}

@pytest.fixture(scope="module")
def api_context(playwright: Playwright):
    """Playwright fixture that sets up an isolated API request context."""
    request_context = playwright.request.new_context(
        base_url=BASE_URL,
        extra_http_headers=HEADERS
    )
    yield request_context
    request_context.dispose()

def test_get_single_user(api_context):
    """GET: Read user details and assert fields."""
    response = api_context.get("/api/users/2")

    # 1. Assert Status Code (200 OK)
    expect(response).to_be_ok()
    assert response.status == 200

    # 2. Assert Response Body Content
    body = response.json()
    assert body["data"]["id"] == 2
    assert "email" in body["data"]
    assert body["data"]["first_name"] == "Janet"


def test_create_user(api_context):
    """POST: Create a new user with payload."""
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = api_context.post("/api/users", data=payload)

    # 1. Assert Status Code (201 Created)
    assert response.status == 201

    # 2. Assert Response Body Content
    body = response.json()
    assert body["name"] == "morpheus"
    assert body["job"] == "leader"
    assert "id" in body
    assert "createdAt" in body


def test_update_user(api_context):
    """PUT: Update existing user data."""
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = api_context.put("/api/users/2", data=payload)

    # 1. Assert Status Code (200 OK)
    assert response.status == 200

    # 2. Assert Response Body Content
    body = response.json()
    assert body["name"] == "morpheus"
    assert body["job"] == "zion resident"
    assert "updatedAt" in body


