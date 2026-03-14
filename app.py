from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Continuous Deployment Berhasil!"

# Penting: Vercel akan mencari variabel 'app' di dalam file ini

if __name__ == "__main__":
    app.run()