# Library for json operations api
import json


class Setting(object):
    # Open json file and get file object
    # Load json data
    with open("setting.json") as f:
        data = json.load(f)

    # Value set for LinkedIn login username
    login_name = data['linkedin_login_name']

    # Value set for LinkedIn login password
    login_password = data['linkedin_login_password']

    # Value set for LinkedIn job search keyword
    search_job_key = data['linkedin_search_job_key']

    # Value set for LinkedIn job search location
    search_job_location = data['linkedin_search_job_location']

    # Value set for csv file path to save search results
    result_csv_file = data['result_csv_file']
