from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

def load_students_from_excel():
    file_path = 'student.xlsx' 
    if os.path.exists(file_path):
        try:
            df = pd.read_excel(file_path)
            
            # Headings ko clean kar rahe hain
            df.columns = df.columns.str.strip()
            
            # Rollno ko roll_no mein badalna
            if 'Rollno' in df.columns:
                df.rename(columns={'Rollno': 'roll_no'}, inplace=True)
            
            # Saari headings ko small letters mein karna (name, class, status, marks)
            df.columns = df.columns.str.lower()
            
            # Roll number ko text banana
            df['roll_no'] = df['roll_no'].astype(str).str.strip()
            
            # Poore data ko dictionary mein convert karna
            return df.set_index('roll_no').to_dict('index')
        except Exception as e:
            print(f"Error: {e}")
            return {}
    return {}

@app.route('/')
def home():
    return render_template('index.html')

# Baaki routes (about, gallery, etc.) waise hi rahenge
@app.route('/about')
def about(): return render_template('about.html')

@app.route('/gallery')
def gallery(): return render_template('gallery.html')

@app.route('/academic')
def academic(): return render_template('academic.html')

@app.route('/contact')
def contact(): return render_template('contact.html')

@app.route('/get_result', methods=['POST'])
def get_result():
    roll = request.form.get('roll_no').strip()
    students_db = load_students_from_excel()
    
    # Excel se us bache ka poora data uthayega (including status)
    student = students_db.get(str(roll))
    
    return render_template('index.html', result=student, roll_no=roll)

if __name__ == '__main__':
    app.run(debug=True)
