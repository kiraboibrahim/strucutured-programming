NUM_SEMESTER_CLASSES = 15
REQUIRED_ATTENDANCE = 0.75 # 75%

allowed_for_exam = 'No'

num_attended_classes = int(input("How many classes did you attend?: "))
attendance = num_attended_classes / NUM_SEMESTER_CLASSES
if attendance < REQUIRED_ATTENDANCE:
    has_medical_reason = input("Did you have any medical cause? (Y/N): ")
    if has_medical_reason == 'Y':
        allowed_for_exam = 'Yes'
    else:
        allowed_for_exam = 'No'

else:
    allowed_for_exam = 'Yes' 
    
print(f"Attendance: {attendance * 100}%\nAllowed to sit for exams: {allowed_for_exam}")
