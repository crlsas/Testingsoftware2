from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Continuous Deployment Berhasil! Aplikasi berjalan di Vercel."

if __name__ == "__main__":
    app.run()