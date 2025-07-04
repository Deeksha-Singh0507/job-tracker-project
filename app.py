from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "👋 Welcome to the Job Tracker API! Go to /jobs to see listings."

@app.route('/jobs')
def get_jobs():
    try:
        df = pd.read_csv("output/remoteok_jobs.csv")
        jobs = df.fillna("").to_dict(orient="records")  # list of dicts
        return jsonify(jobs)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
