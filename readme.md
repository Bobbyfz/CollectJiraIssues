# Jira Issue Data Extractor

This Python script is built with the following objectives:

1. **Data Extraction:**
    - The script is meticulously crafted to ensure comprehensive extraction of all relevant Jira ticket data.
    - It retrieves various fields associated with each issue, providing a holistic view of the ticket information.
    - Through careful handling of API responses, it ensures that all data is extracted accurately and efficiently.

2. **Integration with Data Analysis Software:**
    - Users can seamlessly import the generated CSV file into popular data analysis tools such as PowerBI.
    - The CSV format ensures compatibility with a wide range of data analysis and visualization software, facilitating further exploration and interpretation of the extracted Jira data.

3. **Solving Integration Challenges:**
    - The script addresses the challenge of bridging the gap between Jira Service Management and PowerBI, which lack a native integration.
    - By providing a reliable method to extract Jira data into a format compatible with PowerBI, it enables organizations to leverage the power of data analysis for their service management workflows.

4. **Learning Experience:**
    - Developing this script has provided a valuable learning opportunity, particularly in the realms of data manipulation and API usage.
    - By leveraging the pandas library, I gained insights into efficient data cleaning, transformation, and structuring for analysis purposes.
    - Implementing best practices in consuming RESTful APIs has enhanced my understanding of web service interactions and data retrieval techniques.

Through these objectives, the script not only serves as a practical tool for extracting Jira data but also represents a significant learning journey in software development and data analytics.

## Table of Contents

- [Jira Issue Data Extractor](#jira-issue-data-extractor)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Usage](#usage)
  - [How to Run](#how-to-run)
  - [Note](#note)

## Prerequisites

Before running the script, ensure you have the following:

- Jira username and API token.
- Python installed on your system.
- Required Python packages installed: `requests`, `pandas`, `tqdm`.

## Setup

1. Replace `"JIRA USERNAME HERE"` and `"API TOKEN HERE"` placeholders with your actual Jira username and API token respectively.
2. Replace `"https://XXXXX.atlassian.net/"` with your Jira domain in the `FIELD_URL` and `ISSUE_URL` variables.
3. Define your JQL query in the `getIssue` and `GetAllIssues` function under the `"jql"` parameter.
4. run `pip install -r requirements.txt`

## Usage

1. Ensure you have filled in your Jira credentials and domain in the appropriate placeholders within the script.
2. Define your JQL query in the `getIssue` function under the `"jql"` parameter to specify the issues you want to retrieve.
3. Run the script using Python.
4. The script will connect to Jira using the provided credentials and fetch issue field names and IDs.
5. It will then fetch all issues matching the specified JQL query.
6. The extracted data will undergo a cleaning process to remove unnecessary prefixes and duplicates.
7. Finally, the cleaned data will be exported to a CSV file named `tickets.csv` in the current directory.

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory where the script `jira_issues.py` is located.
3. Run the script using the following command:

```bash
python jira_issues.py
```

## Note

- This script utilizes threading to improve performance when fetching a large number of issues.
- Ensure your API token has appropriate permissions to access the required Jira resources.

Feel free to customize the script according to your specific requirements or integrate it into your workflow as needed. If you encounter any issues or have suggestions for improvements, please feel free to contribute.

This software is distributed under the terms of the GNU General Public License (GPL) version 3 or later. Please see the LICENSE file for more details.
