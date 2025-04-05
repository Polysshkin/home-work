import csv
from flask import Flask, jsonify

app = Flask(__name__)


def read_csv(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader]

            if not rows:
                raise ValueError("CSV file is empty or has an invalid format")

            # Перевірка на порожні значення в рядках
            for row in rows:
                if any(value == '' for value in row.values()):
                    raise ValueError(f"Row has missing or invalid values: {row}")

            return rows
    except Exception as e:
        app.logger.error(f"Error reading file: {e}")
        raise ValueError(f"Error reading file: {e}")


def get_birthdays_for_month(birthdays, month):
    return [b for b in birthdays if b['Month'].lower() == month.lower()]


@app.route('/birthdays/<month>', methods=['GET'])
def birthdays(month):
    try:
        data = read_csv('birthdays.csv')
        birthdays = [b for b in data if month.lower() in b['Month'].lower()]
        return jsonify(birthdays)
    except Exception as e:
        app.logger.error(f"Error in birthdays route: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)

