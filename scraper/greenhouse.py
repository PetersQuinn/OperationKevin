import requests

def scrape_greenhouse_board(board_name):
    url = f"https://boards.greenhouse.io/embed/job_board?for={board_name}&content=json"
    r = requests.get(url)
    if r.status_code != 200:
        return []
    data = r.json()
    jobs = []
    for post in data.get('jobs', []):
        jobs.append({
            'title': post['title'],
            'location': post.get('location', ''),
            'description': post.get('content', ''),
            'url': post['absolute_url'],
            'source': 'greenhouse',
            'company': board_name
        })
    return jobs