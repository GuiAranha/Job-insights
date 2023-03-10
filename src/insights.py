from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types.
    """
    jobs_list = read(path)

    jobs_types = {job["job_type"] for job in jobs_list}

    return jobs_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filter_job_type = [job for job in jobs if job["job_type"] == job_type]

    return filter_job_type


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_list = read(path)

    job_industries = {job["industry"] for job in jobs_list if job["industry"]}

    return job_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filter_job_industry = [job for job in jobs if job["industry"] == industry]

    return filter_job_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_list = read(path)

    job_max_salary = max([
        float(job["max_salary"])
        for job in jobs_list if job["max_salary"].isdigit()
    ])

    return job_max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)

    job_min_salary = min([
        float(job["min_salary"])
        for job in jobs_list if job["min_salary"].isdigit()
    ])

    return job_min_salary


def validate_salary(job, salary):
    if float(job["min_salary"]) >= float(job["max_salary"]):
        raise ValueError
    elif float(job["max_salary"]) >= float(salary) >= float(job["min_salary"]):
        return True
    return False


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        return validate_salary(job, salary)
    except KeyError:
        raise ValueError
    except TypeError:
        raise ValueError


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filter_job_salary = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_job_salary.append(job)
        except ValueError:
            pass

    return filter_job_salary
