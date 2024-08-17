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