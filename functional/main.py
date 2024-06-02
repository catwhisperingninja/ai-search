# NEEDS SOME WORK


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

# Function to search jobs using JobRight API
def jobright_job_search():
    url = 'https://api.jobright.ai/jobs/search'
    headers = {'Authorization': 'Bearer YOUR_API_KEY'}
    params = {
        'jobTitle': 'Information Security Analyst Level 2, Vulnerability Management',
        'city': 'San Francisco, CA',
        'seniority': [3],
        'companyStages': ['Growth Stage', 'Late Stage', 'Early Stage'],
        'annualSalaryMinimum': 90000,
        'workModel': [1, 2, 3],
        'radiusRange': 50,
        'excludeSkills': ['identity management', 'GRC'],
        'excludeCompanies': ['consulting']
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json().get('results', [])

# Function to search jobs using Indeed API
def indeed_job_search():
    url = 'https://api.indeed.com/ads/apisearch'
    params = {
        'publisher': 'YOUR_INDEED_PUBLISHER_ID',
        'q': 'Information Security Analyst Level 2 OR Vulnerability Management',
        'l': 'San Francisco, CA',
        'radius': 50,
        'salary': '90000',
        'userip': 'YOUR_IP_ADDRESS',
        'useragent': 'YOUR_USER_AGENT',
        'format': 'json',
        'v': '2'
    }
    response = requests.get(url, params=params)
    return response.json().get('results', [])

# Function to send email with job results from both APIs
def send_email(jobright_results, indeed_results):
    sender_email = "your_email@gmail.com"
    receiver_email = "your_email@gmail.com"
    password = "your_email_password"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Daily Job Search Results"

    body = ""
    
    if jobright_results or indeed_results:
        if jobright_results:
            body += "Here are the latest job opportunities from JobRight:\n\n"
            for job in jobright_results:
                body += f"- {job['jobTitle']} at {job['companyName']}\n"
                body += f"  Location: {job['jobLocation']}\n"
                body += f"  Salary: {job['salaryDesc']}\n"
                body += f"  [Apply Here]({job['applyLink']})\n\n"

        if indeed_results:
            body += "Here are the latest job opportunities from Indeed:\n\n"
            for job in indeed_results:
                body += f"- {job['jobtitle']} at {job['company']}\n"
                body += f"  Location: {job['formattedLocation']}\n"
                body += f"  Salary: {job.get('salary', 'N/A')}\n"
                body += f"  [Apply Here]({job['url']})\n\n"
    else:
        body += "No good-fit job opportunities found today. The script is running correctly."

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

# Main function to execute job searches and send email
if __name__ == "__main__":
    jobright_results = jobright_job_search()
    indeed_results = indeed_job_search()
    send_email(jobright_results, indeed_results)