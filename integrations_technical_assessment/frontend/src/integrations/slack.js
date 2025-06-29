// slack.js

const BASE_URL = "http://localhost:8000"; // Make sure your backend is running on this

// Step 1: Redirect to Slack authorization
export async function authorize(userId, orgId) {
  const formData = new FormData();
  formData.append("user_id", userId);
  formData.append("org_id", orgId);

  try {
    const response = await fetch(`${BASE_URL}/integrations/slack/authorize`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Authorization failed: ${response.statusText}`);
    }

    const url = await response.text();
    window.location.href = url;
  } catch (error) {
    console.error("Slack authorization error:", error);
    alert("Slack authorization failed.");
  }
}

// Step 2: Handle OAuth2 callback from Slack
export async function oauth2callback(queryParams) {
  try {
    const url = new URL(`${BASE_URL}/integrations/slack/oauth2callback`);
    queryParams.forEach((value, key) => url.searchParams.append(key, value));

    const response = await fetch(url.toString());

    if (!response.ok) {
      throw new Error(`OAuth2 callback failed: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error("Slack OAuth callback error:", error);
    alert("Slack OAuth2 callback failed.");
    return null;
  }
}

// Step 3: Get stored Slack credentials
export async function getCredentials(userId, orgId) {
  const formData = new FormData();
  formData.append("user_id", userId);
  formData.append("org_id", orgId);

  try {
    const response = await fetch(`${BASE_URL}/integrations/slack/credentials`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Get credentials failed: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error("Slack getCredentials error:", error);
    alert("Failed to get Slack credentials.");
    return null;
  }
}

// Step 4: Load Slack items (like channels, users, messages)
export async function loadItems(credentials) {
  const formData = new FormData();
  formData.append("credentials", JSON.stringify(credentials));

  try {
    const response = await fetch(`${BASE_URL}/integrations/slack/load`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Load items failed: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error("Slack loadItems error:", error);
    alert("Failed to load Slack data.");
    return [];
  }
}
