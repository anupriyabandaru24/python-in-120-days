import requests

# Test POST - valid
response = requests.post("http://127.0.0.1:5000/add_student", json={"name": "Jordan", "grade": 88})
print("Add valid:", response.status_code, response.json())

# Test POST - invalid (missing grade)
response2 = requests.post("http://127.0.0.1:5000/add_student", json={"name": "Taylor"})
print("Add invalid:", response2.status_code, response2.json())

# Test DELETE
delete_response = requests.delete("http://127.0.0.1:5000/students/Jordan")
print("Delete:", delete_response.status_code, delete_response.json())

# Confirm final state
check_response = requests.get("http://127.0.0.1:5000/students")
print("Final list:", check_response.json())