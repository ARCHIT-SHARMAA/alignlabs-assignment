# Internal Website Intelligence & Contact Discovery Tool

This project is a lightweight internal research and contact discovery tool designed to analyze public company websites, extract key contact information, and generate structured insights using an LLM. The system includes authentication, protected routes, website scraping, LLM-based structuring, persistent storage, and a simple full-stack interface.

---

## Features

- Login-only authentication (no sign-up)
- JWT-based access token issuance
- Protected frontend routes
- Website scraping (homepage and relevant public pages)
- Extraction of:
  - Emails
  - Phone numbers
  - Social media links
- LLM-based structured JSON generation
- Persistent storage using SQL database
- History view for previously analyzed websites
- REST API built with FastAPI
- Frontend built with Next.js

---

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy ORM
- SQLite
- JWT Authentication
- Google Gemini API (LLM)
- BeautifulSoup (scraping)

### Frontend
- Next.js (App Router)
- TypeScript
- Tailwind CSS
- JWT-based auth handling

---

## Project Structure

alignlabs-assignment/
│
├── backend/
│ ├── api/
│ ├── auth/
│ ├── db/
│ ├── llm/
│ ├── scraping/
│ ├── main.py
│ └── app.db
│
├── frontend/
│ ├── app/
│ ├── components/
│ ├── lib/
│ └── package.json
│
├── .gitignore
└── README.md


---

## Backend Setup

### Prerequisites
- Python 3.10+
- Virtual environment recommended

### Installation

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Environment Variables

Create a .env file inside backend/:

GEMINI_API_KEY=your_gemini_api_key
JWT_SECRET=your_secret_key

Run Backend
uvicorn main:app --reload

Backend will be available at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs


Frontend Setup
Prerequisites

Node.js 18+

Installation

Frontend Setup
Prerequisites

Node.js 18+

Installation

Run Frontend
npm run dev


Frontend will be available at:

http://localhost:3000

Authentication
Login Credentials (Internal)
Email: admin@alignlabs.com
Password: admin123


JWT token is stored in browser localStorage and used for all protected API calls.

Application Flow

User logs in via frontend

Backend issues JWT token

User submits a website URL

Backend verifies authentication

Website is scraped and analyzed

Contact data is extracted

Extracted data is sent to the LLM

LLM returns structured JSON

Data is saved in SQL database

User can view results and history

History Feature

View list of previously researched websites

View detailed structured result per website

Data persists across sessions

Assumptions & Design Choices

Single internal user (no sign-up flow)

SQLite chosen for simplicity

Scraping limited to public pages only

LLM failures handled gracefully

Rate limits not enforced (bonus scope)

Future Improvements

Rate limiting

Multi-user support

Deployment (Docker / Cloud)

Improved scraping depth

UI enhancements

Submission Notes

This project demonstrates:

Full-stack system design

Authentication & authorization

API design

LLM integration

Data persistence

Clean architecture

A video walkthrough is provided separately.


Author

Archit Sharma