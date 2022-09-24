#I learned how to parse a nested list and dictionary

contacts = {
    "number":4,
    "students":
    [
        {"name":"Jerome","email":"jerome@example.com"},
        {"name":"Harry","email":"Harry@example.com"},
        {"name":"Hermione","email":"hermione@example.com"},
        {"name":"Ron","email":"ron@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])