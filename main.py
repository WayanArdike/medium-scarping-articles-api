import feedparser
from flask import Flask, jsonify, request
from flask_cors import CORS
from bs4 import BeautifulSoup
import html

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Medium RSS API",
        "endpoint": "/api/feed"
    })


@app.route("/api/feed")
def get_feed():
    try:
        limit = request.args.get("limit", type=int)

        FEED_URL = "https://medium.com/feed/@wayanardike"

        feed = feedparser.parse(FEED_URL)

        entries = feed.entries or []
        if limit:
            entries = entries[:limit]

        articles = []

        for e in entries:
            content = e.get("content", [{}])[0].get("value", "")
            soup = BeautifulSoup(content, "html.parser")

            img = soup.find("img")
            thumbnail = img["src"] if img else ""

            # clean title
            raw_title = e.get("title", "")
            title = html.unescape(raw_title).replace("\u00a0", " ")
            title = " ".join(title.split())

            # pick published date
            pub_date = e.get("published", "")

            articles.append({
                "id": e.get("id"),
                "title": title,
                "link": e.get("link"),
                "thumbnail": thumbnail,
                "pubDate": pub_date,
            })

        return jsonify({
            "success": True,
            "total": len(articles),
            "articles": articles
        })

    except Exception as err:
        return jsonify({
            "success": False,
            "message": str(err)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=3000,
        debug=True
    )
