# FastAPI Authentication Project

This project demonstrates a full-stack **authentication system** built with **FastAPI** for the backend and **React (Vite + Tailwind CSS)** for the frontend.  

The app allows users to **sign up, log in**, and access a **protected dashboard**.

---

## Project Features

### Backend (FastAPI)
- REST API endpoints for authentication: `/auth/signup`, `/auth/login`
- Password hashing using **PassLib (bcrypt)**
- Token-based authentication with **JWT**
- CORS enabled for frontend integration
- SQLite / MySQL support (configured in `app/database.py`)
- Fully documented API available at `/docs`

### Frontend (React + Vite + Tailwind)
- Responsive login and signup pages
- Dashboard page for logged-in users
- Full-screen layout with consistent color scheme
- State management using **React Hooks**
- Fetches protected data from FastAPI backend
- Navbar hidden on the dashboard for focus

---

## Folder Structure

```

fastapi_auth_project/
│
├── app/                     # Backend
│   ├── main.py              # FastAPI app entry
│   ├── routers/             # API routes
│   ├── services/            # Business logic
│   ├── core/                # Security, config
│   ├── models.py            # Database models
│   ├── database.py          # DB connection
│   └── ...
│
├── frontend/                # React frontend
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   ├── Signup.jsx
│   │   │   └── Dashboard.jsx
│   │   └── components/
│   │       └── Navbar.jsx
│   └── ...
│
├── requirements.txt         # Backend dependencies
├── README.md
└── .gitignore

````

---

## Installation

### Backend

1. Create a virtual environment:

```bash
python -m venv venv
````

2. Activate it:

* Windows: `venv\Scripts\activate`
* Mac/Linux: `source venv/bin/activate`

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the backend:

```bash
uvicorn app.main:app --reload
```

### Frontend

1. Move to frontend folder:

```bash
cd frontend
```

2. Install Node dependencies:

```bash
npm install
```

3. Start development server:

```bash
npm run dev
```

The frontend will run on `http://localhost:5173`.

---

## Usage

1. Open `http://localhost:5173` in your browser.
2. Sign up a new user.
3. Log in with your credentials.
4. Access the dashboard with full-screen layout.
5. Logout to return to the login page.

---

## Technologies Used

* **Backend:** FastAPI, SQLAlchemy, PassLib, JWT
* **Frontend:** React, Vite, Tailwind CSS
* **Database:** SQLite / MySQL (configurable)
* **Other:** CORS, Environment variables

---

## Author

**Abi Waqas** – Full-stack Developer
This project is made for learning and demonstrating **FastAPI authentication with a React frontend**.


