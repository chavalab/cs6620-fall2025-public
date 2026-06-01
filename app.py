from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>Automated CI/CD Pipeline</title>
        </head>
        <body>
            <h1>Hello from Automated CI/CD Pipeline!</h1>
            <p><strong>Version:</strong> 2.0 - Automated Deployment</p>
            <p><strong>Deployed via:</strong> GitHub Actions + AWS SSM</p>
            <p><strong>Build Time:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            <p><strong>Status:</strong> Running on EC2 via Docker</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": "2.0",
        "deployment_method": "automated (GitHub Actions + AWS SSM)",
        "timestamp": datetime.utcnow().isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
