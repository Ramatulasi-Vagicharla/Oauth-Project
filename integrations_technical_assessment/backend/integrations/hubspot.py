# import requests
# from fastapi import Request
# from integrations.integration_item import IntegrationItem

# # Hardcoded credentials (ONLY for testing/development)
# CLIENT_ID = "884fda91-d426-4c97-bf03-97c7b81b0c53"
# CLIENT_SECRET = "e38acd75-fd84-4588-8d99-d2479cbd245b"
# REDIRECT_URI ="http://localhost:3000"

# TOKEN_URL = "https://api.hubapi.com/oauth/v1/token"
# AUTH_URL = (
#     f"https://app.hubspot.com/oauth/authorize"
#     f"?client_id={CLIENT_ID}"
#     f"&redirect_uri={REDIRECT_URI}"
#     f"&scope=contacts"
# )

# # Step 1: Redirect user to HubSpot authorization URL
# def authorize_hubspot():
#     return AUTH_URL

# # Step 2: Handle callback from HubSpot with auth code
# async def oauth2callback_hubspot(request: Request):
#     code = request.query_params.get("code")
#     if not code:
#         raise ValueError("Authorization code not found in the callback URL.")

#     response = requests.post(TOKEN_URL, data={
#         "grant_type": "authorization_code",
#         "client_id": CLIENT_ID,
#         "client_secret": CLIENT_SECRET,
#         "redirect_uri": REDIRECT_URI,
#         "code": code,
#     })
#     response.raise_for_status()
#     return response.json()

# # Step 3: Extract credentials from token response
# def get_hubspot_credentials(token_response: dict):
#     return {
#         "access_token": token_response["access_token"],
#         "refresh_token": token_response.get("refresh_token"),
#     }

# # Step 4: Fetch contacts and return as IntegrationItem list
# def get_items_hubspot(credentials: dict):
#     headers = {
#         "Authorization": f"Bearer {credentials['access_token']}"
#     }

#     items = []
#     response = requests.get("https://api.hubapi.com/crm/v3/objects/contacts", headers=headers)
#     response.raise_for_status()
#     data = response.json()

#     for obj in data.get("results", []):
#         properties = obj.get("properties", {})

#         items.append(IntegrationItem(
#             id=obj.get("id"),
#             type="contact",
#             name=f"{properties.get('firstname', '')} {properties.get('lastname', '')}".strip(),
#             url=f"https://app.hubspot.com/contacts/{obj.get('id')}",
#             creation_time=None,
#             last_modified_time=None
#         ))

#     return items
import requests
from fastapi import Request
from integrations.integration_item import IntegrationItem

# 🔐 Hardcoded credentials (only for development/testing)
CLIENT_ID = "884fda91-d426-4c97-bf03-97c7b81b0c53"
CLIENT_SECRET = "e38acd75-fd84-4588-8d99-d2479cbd245b"
REDIRECT_URI = "http://localhost:3000/callback"
  # ✅ Recommended to use a /callback endpoint

# 🌐 HubSpot OAuth endpoints
TOKEN_URL = "https://api.hubapi.com/oauth/v1/token"
AUTH_URL = (
    f"https://app.hubspot.com/oauth/authorize"
    f"?client_id={CLIENT_ID}"
    f"&redirect_uri={REDIRECT_URI}"
    f"&scope=crm.objects.contacts.read"
    f"&response_type=code"
)


# --- Step 1: Get Authorization URL to start OAuth ---
def authorize_hubspot():
    return AUTH_URL

# --- Step 2 (optional for async callback testing): Exchange code for token ---
async def oauth2callback_hubspot(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise ValueError("Authorization code not found in the callback URL.")

    response = requests.post(TOKEN_URL, data={
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()
    return response.json()

# --- Step 3: Extract access credentials from token response ---
def get_hubspot_credentials(token_response: dict):
    return {
        "access_token": token_response["access_token"],
        "refresh_token": token_response.get("refresh_token"),
        "expires_in": token_response.get("expires_in")
    }

# --- Step 4: Use token to fetch contacts from HubSpot ---
def get_items_hubspot(credentials: dict):
    headers = {
        "Authorization": f"Bearer {credentials['access_token']}"
    }

    url = "https://api.hubapi.com/crm/v3/objects/contacts"
    response = requests.get(url, headers=headers)

    print("Fetching contacts... Status Code:", response.status_code)
    print("Response Text:", response.text)

    response.raise_for_status()
    data = response.json()

    items = []
    for obj in data.get("results", []):
        props = obj.get("properties", {})
        contact_id = obj.get("id", "")
        full_name = f"{props.get('firstname', '')} {props.get('lastname', '')}".strip()

        items.append(IntegrationItem(
            id=contact_id,
            type="contact",
            name=full_name,
            url=f"https://app.hubspot.com/contacts/{contact_id}",
            creation_time=None,
            last_modified_time=None
        ))

    return items
