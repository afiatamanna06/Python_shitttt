student = {
    "ID" : 1163,
    "Name" : "Zahin"
}
print(student["Name"])
student["Name"] = "Jason"
print(student)
print(student.get("Birthdate"))
print(student.get("Birthdate", "August 12"))
student["Birthdate"] = "August 12"
print(student)
#exercise
number = input("Phone: ")
numberlist = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}
output = ""
for item in number:
    output += numberlist.get(item)+" "
print(output)
