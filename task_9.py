#task 9
report_sheet={'Alice':45, 'Peter':77, 'John':98, 'William':87}
key=input("Enter the student's name: ")
if key in report_sheet:
    print("{}'s marks: {}".format(key,report_sheet[key]))
else:
    print("Student not found")

