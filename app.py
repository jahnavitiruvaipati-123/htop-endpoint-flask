from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Sample_name"
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Set server time to IST
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    # Run the top command in batch mode to get process data
    top_output = subprocess.getoutput("top -b -n 1 | head -20")  # Adjust to get top 20 processes

    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
