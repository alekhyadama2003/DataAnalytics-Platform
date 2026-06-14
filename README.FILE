# Data Analytics Platform

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A backend analytics platform built with **Python**, **FastAPI**, and **SQLAlchemy** that enables order management, KPI monitoring, and customer revenue analysis through clean REST APIs.

---

## Overview

This platform collects business data and exposes analytics through RESTful endpoints. It is designed for straightforward integration with frontend dashboards or BI tools, and documents all endpoints via Swagger UI.

---

## Features

- Order creation and retrieval
- Revenue and KPI aggregation
- Top customer ranking by revenue
- SQL-based data aggregations via SQLAlchemy
- Interactive API documentation with Swagger UI

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Framework | FastAPI |
| Database & Querying | SQL (SQLite) |
| Data Visualisation | Swagger UI / Analytics Dashboards |
| Testing | Postman |

---

## API Endpoints

### Orders

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/orders` | Create a new order |
| `GET` | `/orders` | Retrieve all orders |

### Analytics

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/analytics/kpi` | Total orders and revenue summary |
| `GET` | `/analytics/top-customers` | Customers ranked by revenue |

---

## Sample Response

**GET** `/analytics/kpi`

```json
{
  "total_orders": 25,
  "total_revenue": 1250000
}
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/data-analytics-platform.git
cd data-analytics-platform

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.  
Swagger docs: `http://localhost:8000/docs`

---

## Project Structure

```
data-analytics-platform/
├── main.py               # FastAPI app entry point
├── models.py             # SQLAlchemy models
├── database.py           # Database connection setup
├── routers/
│   ├── orders.py         # Order endpoints
│   └── analytics.py      # Analytics endpoints
├── schemas.py            # Pydantic schemas
├── requirements.txt
└── README.md
```

---

## Roadmap

- [ ] PostgreSQL migration for production use
- [ ] Data visualization dashboard
- [ ] Natural language to SQL query interface
- [ ] AI-based query assistant
- [ ] Interactive analytics dashboard

---

## Skills Demonstrated

Python · FastAPI · SQL · Data Visualisation · REST API Design · Database Schema Design · Backend Architecture

---

## License

This project is licensed under the [MIT License](LICENSE).
