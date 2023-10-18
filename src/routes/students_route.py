# routes/students_route.py
from fastapi import APIRouter
from studentModel import StudentModel
from studentsList import studentsList

#import dummyData


import random
for i in range(1, 30):
    random_stars = '*' * random.randint(1, 5)  
    random_sex = random.choice(['male', 'female'])  
    random_castrated = random.choice(['YES', 'NO','MAYBE','SOON'])  
    s = StudentModel(id=str(i), name="student " + str(i), sex=random_sex, castrated=random_castrated, stars=random_stars)
    studentsList.append(s)


router = APIRouter()
# Returned eine reduzierte Liste von students (Name, Rasse, Einlieferungsdatum)
@router.get("/students")
def get_students():
    miniStudentList = []
    
    for student in studentsList:
        miniStudentList.append({"id": student.id,"name": student.name, "castrated":student.castrated, "stars": student.stars })
    
    return miniStudentList
