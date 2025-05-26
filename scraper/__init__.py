def get_all_jobs():
    from .greenhouse import scrape_greenhouse_board
    from .lever import scrape_lever_board
    from .workday import scrape_workday_board
    from .ashby import scrape_ashby_board

    jobs = []
    jobs += scrape_greenhouse_board("palantir")
    jobs += scrape_lever_board("duolingo")
    jobs += scrape_workday_board("https://careers.microsoft.com")
    jobs += scrape_ashby_board("https://jobs.ashbyhq.com/openai")
    return jobs