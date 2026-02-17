from flask import Flask, render_template, request

app = Flask(__name__)

# Aapke students ka data
students_db = {
    "101": {"name": "Hemant", "marks": "85%", "status": "Pass"},
    "102": {"name": "Priya Verma", "marks": "92%", "status": "Pass"},
    "103": {"name": "Amit Kumar", "marks": "35%", "status": "Supplementary"}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_result', methods=['POST'])
def get_result():
    roll = request.form.get('roll_no')
    student = students_db.get(roll)
    return render_template('index.html', result=student, roll_no=roll)

if __name__ == '__main__':
    app.run(debug=True)