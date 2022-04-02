import json

def write_json(existing_data, filename='quiz_list.json'):
    with open(filename, 'w') as f:
        json.dump(existing_data,f,indent=4)


class create_quiz:

    def __init__(self) -> None:
        self.file = open('quiz_list.json', 'a')

    def add_quiz(self, quiz, quiz_questions):

        with open('quiz_list.json') as json_file:
            existing_data = json.load(json_file)
            temp = existing_data["quizzes"]
            new_data = {
            '{}'.format(quiz): quiz_questions,
            }
            temp.append(new_data)
        
        write_json(existing_data)


class create_question:
        
    def add_question(self, question, answer):
        question_oop = {
            'question': question,
            'answer': answer,
        }

        return question_oop

class student:

    def __init__(self, student_name, student_answer) -> None:
        self.student_answer = student_answer
        self.student_name = student_name
    
    def add_student(self):

        with open('student_answer.json') as json_file:
            existing_data = json.load(json_file)
            temp = existing_data["student_answers"]
            student_oop = {
            'name': self.student_name,
            'student_answer': self.student_answer
            }
            temp.append(student_oop)
        
        write_json(existing_data, 'student_answer.json')

        

        


    

        
        

    
    
    
    