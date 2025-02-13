from flask import Flask, render_template

app = Flask(__name__)

# DB 초기화
def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_name TEXT NOT NULL,
            contact TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")  # HTML 랜딩 페이지 로드

@app.route("/submit", methods=["POST"])
def submit():
    store_name = request.form["store_name"]
    contact = request.form["contact"]

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO submissions (store_name, contact) VALUES (?, ?)", (store_name, contact))
    conn.commit()
    conn.close()

    return "제출되었습니다! 감사합니다."

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
