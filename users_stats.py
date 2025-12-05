import csv

def analyze_salaries(filepath='users.csv'):
    salaries = []
    with open(filepath, mode='r') as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip header row
        for row in reader:
            try:
                salaries.append(int(row[5]))
            except (ValueError, IndexError):
                pass  # Ignore rows with invalid salary data

    if not salaries:
        print("No valid salary data found.")
        return

    min_salary = min(salaries)
    max_salary = max(salaries)
    sum_salary = sum(salaries)
    avg_salary = sum_salary / len(salaries)

    print(f"Salary Statistics:")
    print(f"  Minimum Salary: ${min_salary:,.2f}")
    print(f"  Maximum Salary: ${max_salary:,.2f}")
    print(f"  Total Salary: ${sum_salary:,.2f}")
    print(f"  Average Salary: ${avg_salary:,.2f}")

if __name__ == "__main__":
    analyze_salaries()
