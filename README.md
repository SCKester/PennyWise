# PennyWise

A personal finance web application designed to help users take control of their money — track expenses, manage budgets, and visualize spending habits through an intuitive dashboard.

## Features

- **Expense Tracking** — Log and categorize transactions to monitor where your money is going
- **Budget Management** — Set monthly budgets and track progress in real time
- **Data Visualizations** — Dynamic charts and graphs to analyze spending patterns and budget performance

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 19, TypeScript, React Router |
| Backend | Python, Flask, SQLAlchemy |
| Database | PostgreSQL |
| Infrastructure | Docker, Docker Compose |

## Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/)
- [Python 3.x](https://www.python.org/)
- [Docker & Docker Compose](https://www.docker.com/) *(recommended)*

---

### Option 1 — Run with Docker (Recommended)

This will spin up the frontend, backend, and PostgreSQL database together:

```bash
docker-compose up --build
```

Then open your browser and go to:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5001

---

### Option 2 — Run Manually

#### 1. Start the Database
Make sure PostgreSQL is running and create a database called `pennywise`.

#### 2. Backend
```bash
cd backend
pip install -r requirements.txt
flask db upgrade
python app.py
```

#### 3. Frontend
```bash
cd frontend
npm install
npm start
```

Then open http://localhost:3000 in your browser.

---

##  License

This project is open source and available under the [MIT License](LICENSE).
