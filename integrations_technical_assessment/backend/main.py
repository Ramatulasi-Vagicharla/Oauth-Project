from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import requests
from integrations.hubspot import (
    authorize_hubspot,
    get_hubspot_credentials,
    get_items_hubspot,
    CLIENT_ID,
    CLIENT_SECRET,
    TOKEN_URL
)

app = FastAPI()

# CORS setup to allow frontend access
origins = [
    "http://localhost:3000",  # ✅ Add frontend URL if deployed elsewhere
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- HubSpot Routes ---

# Step 1: Get Authorization URL
@app.post('/integrations/hubspot/authorize')
def authorize_hubspot_integration(user_id: str = Form(...), org_id: str = Form(...)):
    return {"url": authorize_hubspot()}


# Step 2: Exchange code for token
@app.post('/integrations/hubspot/credentials')
def get_hubspot_credentials_integration(code: str = Form(...), redirect_url: str = Form(...)):
    token_request_data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": redirect_url,  # ✅ Correct key
        "code": code,
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(TOKEN_URL, data=token_request_data, headers=headers)

    # Debugging output
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    # Raise error if request failed
    response.raise_for_status()

    return get_hubspot_credentials(response.json())


# Step 3: Load items from HubSpot using access token
@app.post('/integrations/hubspot/load')
def get_hubspot_items_integration(credentials: str = Form(...)):
    credentials_dict = json.loads(credentials)
    return get_items_hubspot(credentials_dict)
