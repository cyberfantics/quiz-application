class QuizApp:
    def __init__(self):
        self.username = ''
    
    def startup(self):
        # Print the Greeting Message
        self.gretting()
    
    def gretting(self):
        print('''
        -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
        ~~~~~~~~~~      Welcome To Quiz      ~~~~~~~~~~~
        -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
''')
        print()

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

        # Entry Point of the program
    def run(self):
        self.startup()
        self.menu()


if __name__ == "__main__":
    app = QuizApp()
    app.run()