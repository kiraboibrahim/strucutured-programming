"""
    Write a program to ask 3 students enter their names and the scores in 3 tests.
    Your program should print the average and total of each student
"""
NUM_TESTS = 3
REPORT_TEMPLATE = """
    Name: %(student_name)s
    Total: %(total)d 
    Average: %(average)0.3f
"""

while True:
    total = 0
    curr_test = 1
    student_name = input("Student name: ")
    while curr_test <= NUM_TESTS:
        test_score = int(input(f"Student's test {curr_test} score: "))
        total += test_score
        curr_test += 1
    average = total/NUM_TESTS
    student_report = REPORT_TEMPLATE %({'student_name':student_name, 'total':total, 'average': average})
    print(f"{student_report}\n")
    
    has_more_students = input("Do you still have more students? (yes/no) ")
    if has_more_students.lower() == 'no':
        break
