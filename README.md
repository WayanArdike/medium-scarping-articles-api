# medium-scarping-articles-api

---

## 🚀 Medium Feed API

API kecil untuk mengambil feed Medium via RSS, lalu output jadi JSON yang bersih & simple + auto thumbnail pakai BeautifulSoup.

### ✨ Features

* Flask API
* RSS to JSON
* Auto thumbnail parsing
* CORS enabled
* Custom limit
* Custom author RSS via `.env`

---

## 📦 Install & Setup

### 1. Clone repo

```bash
git clone https://github.com/username/mediumapi.git
cd mediumapi
```

### 2. Buat virtual env

```bash
python -m venv venv
```

### 3. Aktifkan venv

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run project

```bash
python main.py
```

Default port:

```
http://localhost:3000
```

---

## 🔧 Config

Set RSS source lewat environment variable:

```
FEED_URL=https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fmedium.com%2Ffeed%2F%40USERNAME
```

Atau langsung edit di main.py

---

## 🌐 API Endpoint

### Get all feed

```
GET /api/feed
```

### Limit article

```
GET /api/feed?limit=5
```

---

## 🔄 Response Example

```json
{
  "success": true,
  "total": 2,
  "articles": [
    {
      "title": "Hello world",
      "pubDate": "2025-01-01",
      "link": "...",
      "author": "...",
      "thumbnail": "https://..."
    }
  ]
}
```

---

## 🎯 Deploy Options

* Render
* Railway
* Fly.io
* VPS
* Local LAN
* Docker (coming soon)

---

## 🧑‍💻 Built with

* Python
* Flask
* BeautifulSoup
* rss2json API

---

## 🤝 License

MIT
