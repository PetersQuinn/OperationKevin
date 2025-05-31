from scraper import get_all_jobs
from utils import save_jobs

jobs = get_all_jobs()
save_jobs(jobs)  # This will create data/jobs.json
