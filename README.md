# OAuth Integration Project

This project is a Python-based web application that integrates with third-party services using **OAuth 2.0 authentication**. It securely authorizes users and enables access to external APIs (e.g., HubSpot) using access tokens.

## 🚀 Features

- OAuth 2.0 Authorization Code Flow
- Secure access token exchange and storage
- RESTful API endpoints
- Integration with third-party APIs
- Environment variable configuration
- Error handling and validation
- Local server with FastAPI (or Flask)

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** FastAPI / Flask
- **API Testing:** Postman, curl
- **Database:** PostgreSQL (optional)
- **Version Control:** Git, GitHub
- **Auth Protocol:** OAuth 2.0

## 📁 Project Structure
/oauth-project
│
├── main.py # Main application file
├── .env # Environment variables (not committed)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── ...



## 🔐 Environment Setup

Create a `.env` file and add the following:

CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://localhost:3000/callback
BASE_URL=https://api.hubapi.com



## 💻 How to Run

1. **Clone the repository**

git clone https://github.com/your-username/oauth-project.git
cd oauth-project
Create and activate a virtual environment


python -m venv venv
source venv/bin/activate      # For Windows: venv\Scripts\activate
Install dependencies


pip install -r requirements.txt
Run the app


uvicorn main:app --reload
🔍 API Testing
Use Postman or your browser to test endpoints.

Initiate OAuth flow via /authorize endpoint.

### On successful authentication, access tokens are returned for further API requests.

📬 Contact
Author: Rama Tulasi
GitHub: github.com/Ramatulasi-Vagicharla
Email: (vagicharlaramatulasi@gmail.com)


