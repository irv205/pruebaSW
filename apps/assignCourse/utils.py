from apps.user.models import User
from apps.courses import models
from apps.assignCourse.models import StudentCourse, StudentQuestions
from django.db.models.functions import Lower

def AnswersAndQuestions(user_id, lesson_id, questions, answers):

    if len(questions) == len(answers):

        correct_answers = list(models.Answer.objects.filter(question__in = questions).values_list('answer', flat=True))
        type_questions = list(models.Question.objects.filter(id__in = questions).values_list('type', flat=True))

        correct_student_answers = []

        for i in range(0, len(questions)):
            if type_questions[i] == 1:
                valor = type1(answers[i], correct_answers[i])
                correct_student_answers.append(valor['details'])
                CreateRegisterForQuestion(valor, user_id, questions[i], lesson_id)
            elif type_questions[i] == 2:
                valor = type2(answers[i], correct_answers[i])
                correct_student_answers.append(valor['details'])
                CreateRegisterForQuestion(valor, user_id, questions[i], lesson_id)
            elif type_questions[i] == 3:
                valor = type3(answers[i], correct_answers[i])
                correct_student_answers.append(valor['details'])
                CreateRegisterForQuestion(valor, user_id, questions[i], lesson_id)
            elif type_questions[i] == 4:
                valor = type4(answers[i], correct_answers[i])
                correct_student_answers.append(valor['details'])
                CreateRegisterForQuestion(valor, user_id, questions[i], lesson_id)

        if 'reprobate' in correct_student_answers:
            
            return {'pass': False,'result': correct_student_answers} 

        return {'pass': True,'result': correct_student_answers} 

    else:
        return {'access': False, 'details':'You didnt answer all the questions'}

def type1(answers_student, answers):

    stranswer = ' '.join(map(str, answers))

    if answers_student == stranswer:
        return {'pass': True, 'details': "approved"}
    else:
        return {'pass': False, 'details': "reprobate"}

def type2(answers_student, answers):

    stranswer = ' '.join(map(str, answers)) 

    if answers_student == stranswer:
        return {'pass': True, 'details': "approved"}
    else:
        return {'pass': False, 'details': "reprobate"}

def type3(answers_student, answers):

    arry = answers_student
    arry = arry.split(',')

    validation = set(arry).intersection(answers)

    if validation:
        return {'pass': True, 'details': "approved"}
    else:
        return {'pass': False, 'details': "reprobate"}

def type4(answers_student, answers):

    arry = answers_student
    arry.replace(" ","")
    arry = arry.split(',')

    if arry == answers:
        return {'pass': True, 'details': "approved"}
    else:
        return {'pass': False, 'details': "reprobate"}

def CreateRegisterForQuestion(valor, user_id, question_id, lesson_id):

    user = User.objects.get(id = user_id)
    question = models.Question.objects.get(id = question_id)
    lesson = models.Lesson.objects.get(id = lesson_id)

    question_log = StudentQuestions.objects.create(user = user, question = question, lesson = lesson, correct_question = valor['pass'], owner_id = user_id, is_active = True)

    if valor['pass'] == True:
        score = question.score
        course = StudentCourse.objects.filter(user=user_id, lesson=lesson_id).first()
        course.students_score += score
        course.save()

    return {'details': "Create and Update"}