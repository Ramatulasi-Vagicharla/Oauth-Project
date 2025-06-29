// const BASE_URL = "http://localhost:8000"; // Adjust if backend is hosted elsewhere

// export async function authorize(userId, orgId) {
//   const formData = new FormData();
//   formData.append("user_id", userId);
//   formData.append("org_id", orgId);

//   const response = await fetch(`${BASE_URL}/integrations/hubspot/authorize`, {
//     method: "POST",
//     body: formData,
//   });

//   const url = await response.text();
//   window.location.href = url;
// }

// export async function oauth2callback(queryParams) {
//   const url = new URL(`${BASE_URL}/integrations/hubspot/oauth2callback`);
//   queryParams.forEach((value, key) => url.searchParams.append(key, value));

//   const response = await fetch(url.toString());
//   return await response.json();
// }

// export async function getCredentials(userId, orgId) {
//   const formData = new FormData();
//   formData.append("user_id", userId);
//   formData.append("org_id", orgId);

//   const response = await fetch(`${BASE_URL}/integrations/hubspot/credentials`, {
//     method: "POST",
//     body: formData,
//   });

//   return await response.json();
// }

// export async function loadItems(credentials) {
//   const formData = new FormData();
//   formData.append("credentials", JSON.stringify(credentials));

//   const response = await fetch(`${BASE_URL}/integrations/hubspot/load`, {
//     method: "POST",
//     body: formData,
//   });

//   return await response.json();
// }
// src/components/HubSpotIntegration.js

const BASE_URL = "http://localhost:8000"; // Update if backend is hosted elsewhere

// Step 1: Redirect user to HubSpot authorization
export async function authorize(userId, orgId) {
  const formData = new FormData();
  formData.append("user_id", userId);
  formData.append("org_id", orgId);

  const response = await fetch(`${BASE_URL}/integrations/hubspot/authorize`, {
    method: "POST",
    body: formData,
  });

  const url = await response.text();
  window.location.href = url;
}

// Step 2: Handle OAuth2 callback from HubSpot
export async function oauth2callback(queryParams) {
  const url = new URL(`${BASE_URL}/integrations/hubspot/oauth2callback`);
  queryParams.forEach((value, key) => url.searchParams.append(key, value));

  const response = await fetch(url.toString());
  return await response.json();
}

// Step 3: Get stored HubSpot credentials
export async function getCredentials(userId, orgId) {
  const formData = new FormData();
  formData.append("user_id", userId);
  formData.append("org_id", orgId);

  const response = await fetch(`${BASE_URL}/integrations/hubspot/credentials`, {
    method: "POST",
    body: formData,
  });

  return await response.json();
}

// Step 4: Load items (e.g., contacts) from HubSpot
export async function loadItems(credentials) {
  const formData = new FormData();
  formData.append("credentials", JSON.stringify(credentials));

  const response = await fetch(`${BASE_URL}/integrations/hubspot/load`, {
    method: "POST",
    body: formData,
  });

  return await response.json();
}
