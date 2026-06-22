# 📰 Quantex News API

A resurrected news API project — originally broken, now fully functional with PostgreSQL, async support, and a clean modular structure.

---

## 🚀 What this project does

- Provides a REST API for news articles
- Stores data in PostgreSQL (or SQLite for local testing)
- Uses async drivers for better performance
- Includes authentication via `x-secret` header

---

## 🛠️ What was fixed

- ✅ Database connection issues resolved
- ✅ Async driver support added
- ✅ Tables created via Alembic migrations
- ✅ GET and POST endpoints tested and working
- ✅ Authentication via `x-secret` header validated
- ✅ Modular project structure organized

---

## 📁 Project Structure
quantex/
├── quantex/ # Main application package
│ ├── web/ # API routes and dependencies
│ ├── database/ # Models and DAOs
│ └── settings.py # Configuration
├── requirements.txt # Dependencies
├── alembic.ini # Migration config
└── README.md # This file

---

## 🧩 Technologies Used

- Python 3.10+
- FastAPI
- SQLAlchemy (async)
- PostgreSQL / SQLite
- Alembic
- Uvicorn
- Pydantic

---

## 📦 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/alictech7-oss/quantex-news-api.git
cd quantex-news-api

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
alembic upgrade head

# 5. Start the server
python -m quantex

🔑 Authentication
All endpoints require the x-secret header: x-secret: secret

📡 API Endpoints
Method	Endpoint	Description
GET	/api/news/	List all news
POST	/api/news/	Create a new news entry
GET	/api/news/{id}	Get news by ID

📌 Notes
The original project was broken and abandoned.

This version was fully restored, tested, and documented.

Runs with PostgreSQL or SQLite (for local testing).

🙏 Credits & Original Work
This project is based on the original quantex-news-api repository.

The original code was broken and abandoned.
This version includes:

Full restoration of functionality

Database and async support fixes

Updated dependencies and structure

Clean documentation and organization

All improvements were made with respect to the original authors.

👨‍💻 Maintained by
alictech7-oss

📄 License
MIT — use, modify, and share freely.

---

## 🚀 **How to apply:**

1. Access: `https://github.com/alictech7-oss/quantex-news-api`
2. Click on the `README.md` file
3. Click the pencil (✏️) to edit
4. Replace with the content above
5. Commit directly to the `main` branch or make a PR

---









