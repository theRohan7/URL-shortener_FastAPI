# 🔗 URL Shortener Backend Service

This is a simple, production-level **URL Shortener** built with **FastAPI** and **PostgreSQL**.

It has two primary endpoints:

- `POST /shorten`: Accepts a long URL and returns a shortened one.
- `GET /{short_code}`: Redirects to the original URL when a shortened URL is visited.

---

## 🛠 Requirements

- Python 3.8+
- PostgreSQL installed and running
- A PostgreSQL database created (e.g., `url_shortener`)

---

## 📦 Installation & Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/theRohan7/URL-shortener_FastAPI
cd url-shortener
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
TO ACTIVATE THE VIRTUAL ENVIRONMENT:     .venv\Scripts\activate (Windows)     source .venv/bin/activate (Mac)
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
DATABASE_URL=postgresql://postgres:yourpassword@localhost/url_shortener   
BASE_URL=http://localhost:8000
```

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```
Tables will be auto-generated locally into your machine when you start the app

*Your app will be available* at http://localhost:8000




### Reach out to me!

Mail: therohansahu7@gmail.com
Portfolio: https://portfolio-five-alpha-31.vercel.app/




