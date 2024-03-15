import requests
import pandas as pd
from tqdm import tqdm
import threading

# Jira Credentials and URLs
USERNAME = "JIRA USERNAME HERE"
API_TOKEN = "API TOKEN HERE"
#Replace XXXXX with your Jira domain 
FIELD_URL = "https://XXXXX.atlassian.net/rest/api/3/field"
ISSUE_URL = "https://XXXXX.atlassian.net/rest/api/3/search"

#function to retrieve the issue field names and ID from Jira
def getFields():
    auth = (USERNAME, API_TOKEN)
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(FIELD_URL, headers=headers, auth=auth)
    if response.status_code == 200:
        fields_data = response.json()
        custom_fields = [{"ID": field['id'], "Name": field['name']} for field in fields_data]
        return custom_fields
    else:
        print(f'Response code - {response.status_code}')
        return None
    
#function to retrieve issues from Jira
def getIssue(start, max_results, all_issues, auth):
    params = {"jql": "INSERT JQL HERE", "startAt": start, "maxResults": max_results, "fieldsByKeys": "true"}
    response = requests.get(ISSUE_URL, params=params, auth=auth)
    if response.status_code == 200:
        issues = response.json()['issues']
        all_issues.extend(issues)
        return issues
    else:
        print(f'Response code - {response.status_code}')
        return None

#using threading, uses the above function to retrieve all issues from Jira
def getAllIssues():
    auth = (USERNAME, API_TOKEN)
    all_issues = []
    total_issues = requests.get(ISSUE_URL, params={"jql": "INSERT JQL HERE", "maxResults": 0,  "fieldsByKeys": "true"}, auth=auth).json()["total"]
  
    threads = []
    chunk_size = 100  # Number of issues to fetch in each thread
    num_threads = (total_issues + chunk_size - 1) // chunk_size
  
    with tqdm(total=total_issues) as pbar:
        for i in range(num_threads):
            start = i * chunk_size
            thread = threading.Thread(target=getIssue, args=(start, chunk_size, all_issues, auth))
            threads.append(thread)
            thread.start()
  
        for thread in threads:
            thread.join()
            pbar.update(chunk_size)
  
    return all_issues
    
    
#function to clean the issue data by renaming columns
def cleanData(fields,tickets):
    #removes the 'fields.' from the column names
    tickets.rename(columns=lambda x: x[len('fields.'):] if x.startswith('fields.') else x, inplace=True)
    #removes anything trailing after the '.' in the column names
    tickets.rename(columns=lambda x: x.split('.')[0], inplace=True)
    #renames the columns in tickets with the actual field names
    for column in tickets.columns:
        if column in fields['ID'].values:
            new_column_name = fields.loc[fields['ID'] == column, 'Name'].values[0]
            tickets.rename(columns={column: new_column_name}, inplace=True)
    #removes the duplicate columns
    duplicate_columns = tickets.columns[tickets.columns.duplicated()]
    tickets.drop(columns=duplicate_columns[1:], inplace=True)
    
    return tickets
#main 
if __name__ == "__main__":
    fields_list = getFields()
    tickets_list = getAllIssues()

    fields = pd.DataFrame(fields_list)
    tickets = pd.json_normalize(tickets_list)
    
    tickets = cleanData(fields, tickets)
    tickets.to_csv('tickets.csv', index=False)