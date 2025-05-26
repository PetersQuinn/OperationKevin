import json

def save_jobs(jobs, filename="data/jobs.json"):
    with open(filename, "w") as f:
        json.dump(jobs, f, indent=2)

def load_jobs(filename="data/jobs.json"):
    with open(filename, "r") as f:
        return json.load(f)