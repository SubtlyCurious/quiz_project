
from unittest import result
import quiz_classes
import json


def helloScreen():
    print(f'Welcome to Quiz Generator 9000')
    cred = input("Student or Teacher: ")

    return cred

def teacher():
    create_quiz = input('Would you like to create a quiz? (Y/N): ').lower()
    continue_quiz = True
    while continue_quiz:
        if(create_quiz == 'y'):
            quiz_name = input('What will be your quiz name?: ')
            total_questions = int(input('How many questions?: '))

            question_list = []
            i = 0
            
            while i < total_questions:
                question_prompt = input('Question Prompt: ')
                question_answer = input('Question Answer: ')
            

                theQuestion =  quiz_classes.create_question().add_question(question_prompt, question_answer)
                question_list.append(theQuestion)
                
                i += 1
            
            quiz_classes.create_quiz().add_quiz(quiz_name, question_list)

            create_quiz = input('Would you like to create another quiz? (Y/N): ').lower()
            if create_quiz == 'n':
                continue_quiz = False
            

        elif(create_quiz == 'n'):
            continue_quiz = False


def student(quiz):
    open_quiz_json = json.load(open('quiz_list.json'))
    x = 0

    for x in open_quiz_json['quizzes']:
        for i in x:
            if quiz == i:
                return x[i]

def display_quiz(question_list):
    student_answer = []
    for data in question_list:
        for question in data:
            if question == 'question':
                print(data[question])
                student_answer.append(input("Your Answer: "))
    print("Thank you for taking the quiz!")
    return student_answer
                
    


def main():

  
    cred = helloScreen().lower()
    if(cred == 'teacher'):
        teacher()
        view_quiz = input('Would you like to view your quizzes? (Y/N): ').lower()

        if(view_quiz == 'y'):
            data = json.load(open('quiz_list.json'))
            
            for quiz in data['quizzes']:
                print(quiz)

        else:
            print("Thank you for using Quiz Generator 9000!")
            
    elif(cred == 'student'):
        what_quiz = input("What Quiz will you be taking?: ")
        student_name= input("What is your name: ")

        quiz_classes.student(student_name=student_name, student_answer=display_quiz(student(what_quiz))).add_student()

main()