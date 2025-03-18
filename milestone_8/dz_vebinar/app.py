from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for birthdays and anniversaries
data = {
    "HR": {
        "birthdays": {
            "april": [
                {"id": 1, "name": "John Doe", "birthday": "Apr 18"}
            ]
        },
        "anniversaries": {
            "april": [
                {"id": 2, "name": "Jane Smith", "anniversary": "Apr 25"}
            ]
        }
    },
    "IT": {
        "birthdays": {
            "april": [
                {"id": 3, "name": "Alice Johnson", "birthday": "Apr 10"}
            ]
        },
        "anniversaries": {
            "april": [
                {"id": 4, "name": "Bob Brown", "anniversary": "Apr 15"}
            ]
        }
    }
}

@app.route('/birthdays', methods=['GET'])
def get_birthdays():
    month = request.args.get('month')
    department = request.args.get('department')
    
    if department in data and month in data[department]['birthdays']:
        employees = data[department]["birthdays"][month]
        return jsonify({
            "total": len(employees),
            "employees": employees
        })
    else:
        return jsonify({"error": "No data found for the given month and department"}), 404

@app.route('/anniversaries', methods=['GET'])
def get_anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')
    
    if department in data and month in data[department]['anniversaries']:
        employees = data[department]["anniversaries"][month]
        return jsonify({
            "total": len(employees),
            "employees": employees
        })
    else:
        return jsonify({"error": "No data found for the given month and department"}), 404

if __name__ == '__main__':
    app.run(debug=True)
