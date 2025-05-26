import requests

def scrape_lever_board(company_handle):
    url = f"https://api.lever.co/v0/postings/{company_handle}?mode=json"
    r = requests.get(url)
    if r.status_code != 200:
        return []
    data = r.json()
    jobs = []
    for post in data:
        jobs.append({
            'title': post['text'],
            'location': post.get('categories', {}).get('location', ''),
            'description': post.get('description', ''),
            'url': post['hostedUrl'],
            'source': 'lever',
            'company': company_handle
        })
    return jobs