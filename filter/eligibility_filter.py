def keyword_filter(description):
    text = description.lower()
    if any(kw in text for kw in ['cpt', 'opt', 'visa sponsorship']):
        return 'Likely Accepts'
    elif any(kw in text for kw in ['us citizen', 'no sponsorship', 'green card only']):
        return 'Likely Rejects'
    return 'Unclear'