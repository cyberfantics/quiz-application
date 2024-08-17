class QuizApp:
    def __init__(self):
        self.username = ''
    
    def startup(self):
        # Print the Greeting Message
        self.gretting()
        self.username = input('What is your Name? ')
        print(f'Welcome, {self.username}')
        print()


    def gretting(self):
        print('''
        -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        ~~~~~~~~~~      Welcome To Quiz      ~~~~~~~~~~~
        -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
''')
        print()

    def menu_header(self):
        print(f'''
        -------------------------------------------
        Please Make A Selection:
        (M): Repeat this Menu
        (L): List quizzes
        (T): Take a Quiz
        (E): Exit a Quiz
               
''')
        
    def menu_error(self):
        print("That's not a valid Sellection, Please Try Again")
        
    def goodbye(self):
        print(f'''
        -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        ~~~ Thank You For Using PyQuiz, {self.username}! ~~~
        -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
''')
        print()

    def menu(self):
        self.menu_header()

        # Run untill the user exit the app
        selection = ''
        
        # Run the Program
        while True:
            selection = input("Selection? ").capitalize()

            if len(selection) == 0:
                self.menu_error()
                continue

            match selection[0]:
                case 'E':
                    self.goodbye()
                    break

                case 'M':
                    self.menu_header()
                    continue
                    
                case 'L':
                    print("\nAvailable Quizes Are")
                    # TODO list the quiz letter
                    print('__________________________')
                    continue

                case 'T':
                    try:
                        quizNum = int(input("Enter the Quiz Num "))
                        print(f"You have selected the quiz {quizNum}")
                    except Exception as e:
                        self.menu_error()
                        print(f'Error Occured: {e}')
                    
                    continue
                
                case _:
                    self.menu_error() 
        # Entry Point of the program
    def run(self):
        self.startup()
        self.menu()

# Implement Question Class
class Question:
    def __init__(self):
    
    # TODO Define the Question Fields
        self.points = 0
        self.correct_answer = ''
        self.text = ''
        self.is_correct = False


# Inherit Question Class Into True False Class
class QuestionTF(Question):
    def __init__(self):
        super().__init__()
    
    # TODO Define The Asking Method

    def ask(self):
        while True:
            print(f'(T)rue or (F)alse: {self.text}')
            response = input("? ")

            # TODO: Check to see if no response was entered
            if len(response) == 0:
                print("Not a valid Response, Continue")
                continue
            
            # TODO: Check to see if either T or F was given
            if response[0].lower() != 't' and response[0].lower()!='f':
                print("Not a valid Response, Continue")
                continue

            # TODO: Mark this question as correct, if answered correctly
            if response[0].lower() == self.correct_answer:
                self.is_correct = True

            break


# Inherit Question Class Into MCQs Class
class QuestionMCQs(Question):
    def __init__(self):
        super().__init__()
        # TODO: Define the answer for asking question
        self.answers = []

    def ask(self):
        while True:
            print(f"{self.text} ")
            for a in self.answer:
                print(f"({a.name}). {a.text}")
            response = input("? ")

            # TODO: Check to see if no response was entered
            if len(response) == 0:
                print("Not a valid Response, Continue")
                continue
            

            # TODO: Mark this question as correct, if answered correctly
            if response[0].lower() == self.correct_answer:
                self.is_correct = True

            break


# Answer Class For Multiple Choice Question
class Answer():
    def __init__(self):
        self.text = ''
        self.name = ''


# Implement Quiz Class
class Quiz():
    def __init__(self):
        # TODO: define the quiz property
        self.name = ''
        self.description = ''
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_point = 0

    def print_header(self):
        print(f'''
        ----------------------------------------------------
               Quiz Name: {self.name}
        Quiz Description: {self.description}
               Questions: {len(self.questions)}
            Total Points: {self.total_point}
        ----------------------------------------------------
    ''')


    def print_result(self):
        print('''
        Print The Result
        ''')
    
    def take_quiz(self):
        # TODO: INITILIZE THE QUIZ STATE
        self.score = 0
        self.correct_count = 0
        for q in self.questions:
            q.is_correct = False
        
        # TODO: PRINT THE HEADER
        self.print_header()

        # TODO: EXECUTE EACH QUESTION AND RECORD THE RESULT
        for q in self.questions:
            q.ask()
            if q.is_correct:
                self.correct_count += 1
                self.score += q.points
        print('-----------------------------------\n')
        # TODO: RETURN THE RESULT

        return (self.score, self.correct_count, self.total_point)
        



if __name__ == "__main__":
    app = QuizApp()
    app.run()