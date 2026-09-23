from flask import Flask
from flask  import jsonify
from flask import request
app = Flask(__name__)

@app.route('/')
def home():
    return "Student API is running"

students=[{"name": "Alex","grade": 90},{"name": "Sam","grade": 85}]

@app.route("/students")
def list_of_students():
    return jsonify(students)

@app.route("/students/count")
def students_count():
    return jsonify({"count": len(students)})

@app.route("/students/average")
def students_average():
    if len(students)==0:
        return jsonify({"average": 0})
    total=sum(student["grade"] for student in students)
    avg=total/len(students)        
    return jsonify({"average": avg})
@app.route("/students/<name>",methods=["GET","DELETE"])
def search_student(name):
    if request.method=="DELETE":
       for student in students:
           if student["name"]==name:
               students.remove(student)
               return jsonify({"message": f"{name} deleted"})
       return jsonify({"error": "Student not found"}),404   
    else:
         for student in students:
             if student["name"]==name:
                return jsonify(student)
         return jsonify({"error": "Student not found"}), 404 

@app.route("/greet/<name>")
def greet(name):
    return jsonify({"message": f"Welcome, {name}!"})           

@app.route("/add_student",methods=["POST"])
def add_student():
    data=request.get_json()
    if not data.get("name") or not data.get("grade"):
        return jsonify({"error": "Missing name or grade"}),400
    students.append(data)
    return jsonify(data),201

@app.route("/students/above/<int:min_grade>")
def above_mingrade_students(min_grade):
    grade_list=[]
    for student in students:
        if student["grade"]>min_grade:
            grade_list.append(student)
    return jsonify(grade_list)  
          
if __name__ == "__main__":
    app.run(debug=True)
