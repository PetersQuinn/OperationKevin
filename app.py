import streamlit as st
import json
from filter.eligibility_filter import keyword_filter

with open("data/jobs.json", "r") as f:
    jobs = json.load(f)

st.title("🌍 Internship Finder for International Students")

filter_option = st.selectbox("Filter jobs by eligibility:", ["All", "Likely Accepts", "Likely Rejects", "Unclear"])

for job in jobs:
    label = keyword_filter(job['description'])
    if filter_option != "All" and label != filter_option:
        continue
    st.subheader(job['title'])
    st.caption(f"{job['company']} - {job['location']} - {label}")
    st.markdown(job['url'])
    st.write(job['description'][:300] + "...")
    st.markdown("---")

# Run with: `streamlit run app.py`