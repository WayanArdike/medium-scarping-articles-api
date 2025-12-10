import os
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from bs4 import BeautifulSoup

app = Flask(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def home():
    return jsonify({
        'message': 'Medium Feed API',
        'endpoint': '/api/feed'
    })

@app.route("/api/feed")
def get_feed():
    try:
        limit = request.args.get('limit', type=int)

        FEED_URL = os.getenv(
            "FEED_URL",
            "https://rssjson.com/api/v1/convert/https%3A%2F%2Fmedium.com%2Ffeed%2F%40wayanardike"
        )

        response = requests.get(FEED_URL, timeout=10)
        data = response.json()

        items = data.get('items', [])
        if limit:
            items = items[:limit]

        results = []
        for item in items:
            soup = BeautifulSoup(item.get('description', ''), 'html.parser')
            h4 = soup.find('h4')
            img = h4.find_next('img') if h4 else soup.find('img')
            thumbnail = img.get('src') if img else ''

            results.append({
                'title': item.get('title', ''),
                'pubDate': item.get('pubDate', ''),
                'link': item.get('link', ''),
                'author': item.get('author', ''),
                'thumbnail': thumbnail
            })

        return jsonify({
            'success': True,
            'total': len(results),
            'articles': results
        })

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == "__main__":
    debug = os.environ.get("FLASK_ENV") != "production"
    app.run(
        debug=debug,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 3000))
    )
