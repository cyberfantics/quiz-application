from quizManager import QuizManager

class QuizApp:
    QUIZ_FOLDER = "Quizzes"

    # ANSI escape codes for colors
    COLORS = {
        'header': '\033[95m',  # Magenta
        'info': '\033[94m',    # Blue
        'success': '\033[92m', # Green
        'warning': '\033[93m', # Yellow
        'error': '\033[91m',   # Red
        'endc': '\033[0m'      # End color
    }

    def __init__(self):
        self.username = ''
        self.qm = QuizManager(QuizApp.QUIZ_FOLDER)

    def startup(self):
        # Print the Greeting Message
        self.greeting()
        self.username = input(f'{self.COLORS["info"]}What is your Name? {self.COLORS["endc"]}')
        print(f'{self.COLORS["success"]}Welcome, {self.username}{self.COLORS["endc"]}')
        print()

    def greeting(self):
        print(f'''
        {self.COLORS["header"]}
        -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        ~~~~~~~~~~      Welcome To Quiz      ~~~~~~~~~~~
        -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        {self.COLORS["endc"]}
        ''')

    def menu_header(self):
        print(f'''
        {self.COLORS["header"]}
        -------------------------------------------
        Please Make A Selection:
        (M): Repeat this Menu
        (L): List quizzes
        (T): Take a Quiz
        (E): Exit a Quiz
        {self.COLORS["endc"]}
        ''')

    def menu_error(self):
        print(f'{self.COLORS["error"]}That\'s not a valid Selection, Please Try Again{self.COLORS["endc"]}')

    def goodbye(self):
        print(f'''
        {self.COLORS["header"]}
        ~~~ Thank You For Using PyQuiz, {self.username}! ~~~
        {self.COLORS["endc"]}
        ''')

    def menu(self):
        self.menu_header()

        # Run until the user exits the app
        while True:
            selection = input(f"{self.COLORS['info']}Selection? {self.COLORS['endc']}").capitalize()

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
                    print(f'{self.COLORS["info"]}\nAvailable Quizzes Are{self.COLORS["endc"]}')
                    # TODO: list the quiz letter
                    self.qm.list_quizzes()
                    print('__________________________')
                    continue

                case 'T':
                    try:
                        quizNum = int(input(f"{self.COLORS['info']}Enter the Quiz Number: {self.COLORS['endc']}"))
                        print(f"{self.COLORS['info']}You have selected the quiz {quizNum}{self.COLORS['endc']}")

                        # TODO: Start the quiz
                        self.qm.take_quiz(quizNum, self.username)
                        self.qm.print_results()

                        # TODO: Ask user if they want to save the result
                        dosave = input(f'{self.COLORS["info"]}Save the result? (y/n): {self.COLORS["endc"]}')
                        dosave = dosave.capitalize()

                        if dosave[0] == 'Y' and len(dosave) > 0:
                            self.qm.save_result()
                    except Exception as e:
                        self.menu_error()
                        print(f'{self.COLORS["error"]}Error Occurred: {e}{self.COLORS["endc"]}')

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
