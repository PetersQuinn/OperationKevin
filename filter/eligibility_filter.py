import openai

def keyword_filter(description):
    text = description.lower()
    if any(kw in text for kw in ['cpt', 'opt', 'visa sponsorship']):
        return 'Likely Accepts'
    elif any(kw in text for kw in ['us citizen', 'no sponsorship', 'green card only']):
        return 'Likely Rejects'
    return 'Unclear'

def gpt_filter(description):
    prompt = f"""
You are an AI assistant. Classify this job as one of the following:
(1) Accepts international students
(2) Rejects international students
(3) Unclear

Job description:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt + description}],
        temperature=0
    )
    return response.choices[0].message['content'].strip()