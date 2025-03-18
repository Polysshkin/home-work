import requests
import argparse

def fetch_report(month, department):
    url = f'http://127.0.0.1:5000/birthdays?month={month}&department={department}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Report for {department} department for {month.capitalize()} fetched.")
        print(f"Total: {data['total']}")
        print("Employees:")
        for employee in data['employees']:
            print(f"- {employee['birthday']}, {employee['name']}")
    else:
        print(f"Error: {response.json()['error']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch department report.")
    parser.add_argument('month', type=str, help='The month for the report (e.g., april)')
    parser.add_argument('department', type=str, help='The department for the report (e.g., Engineering)')
    
    args = parser.parse_args()
    fetch_report(args.month, args.department)
