from apps.user.models import User
from apps.courses import models
from apps.assignCourse.models import StudentCourse, StudentQuestions
from django.db.models.functions import Lower

#Verificar tipo de usuario
def UserAuth(id):

    user = User.objects.get(id = id)

    if user.type == 3:
        return {'access': False, 'details': 'You do not have permission to do this'}
    else:
        return {'access': True}

#Verificar que solo se le asignen cursos a estudiantes
def VerificationStudent(id):

    user = User.objects.get(id = id)

    if user.type == 3:
        return {'access': True}
    else:
        return {'access': False, 'details': 'You can only assign courses to students'} 

#Verificar que no se agregue el mismo curso a un estudiante
def CheckCourseForStudent(course, student):

    validation = StudentCourse.objects.filter(course = course, user = student).first()

    if validation:
        return {'access': False, 'details': 'The student has already assigned this course'}
    else:
        return {'access': True}

#Verificar que la leccion sea acorde al curso seleccionado
def CheckLessonsForCuourses(lesson, Course):

    validation = models.Lesson.objects.filter(id = lesson, course = Course).first()

    if validation:
        return {'access': True}
    else:
        return {'access': False, 'details': 'You cannot assign a lesson that does not belong to the course'}

def CheckLessonForStudent(lesson, student):

    validation = StudentCourse.objects.filter(lesson = lesson, user = student).first

    if validation:
        return {'access': True}
    else:
        return {'access': False, 'details': 'This lesson does not belong to this student'}
