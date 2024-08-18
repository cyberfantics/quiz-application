from quizManager import QuizManager

class QuizApp:
    QUIZ_FOLDER = "Quizzes"
    def __init__(self):
        self.username = ''
        self.qm = QuizManager(QuizApp.QUIZ_FOLDER)
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
                    self.qm.list_quizzes()  
                    print('__________________________')
                    continue

                case 'T':
                    try:
                        quizNum = int(input("Enter the Quiz Num "))
                        print(f"You have selected the quiz {quizNum}")
                    
                        # TODO: Start the quiz
                        self.qm.take_quiz(quizNum,self.username)
                        self.qm.print_results()
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


if __name__ == "__main__":
    app = QuizApp()
    app.run()