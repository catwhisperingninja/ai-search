from datetime import datetime
import logging

# Global store for job results
job_results = {
    'indeed': [],
    'jobright': []
}
def print_job_results(jobright_results, indeed_results):
    try:
        print(f"\n=== Job Search Results - {datetime.now().strftime('%Y-%m-%d')} ===\n")
        if jobright_results or indeed_results:
            if jobright_results:
                print("JobRight Opportunities:")
                print("------------------------")
                for job in jobright_results:
                    print(f"Title: {job.get('jobTitle', 'N/A')}")
                    print(f"Company: {job.get('companyName', 'N/A')}")
    except:
        print("else")
print(f"Location: {job.get('jobLocation', 'N/A')}")
print(f"Salary: {job.get('salaryDesc', 'N/A')}")
