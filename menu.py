def open_menu(title, options):
    menu = Menu(title, options)
    menu.display()
    return menu.get_response()

class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def display(self):
        print(f"---- {self.title} ----")
        for i in range(len(self.options)):
            print(f"{i+1}. {self.options[i]}")
    
    def get_response(self):
        MESSAGE = "Votre réponse : "
        response = input(MESSAGE)
        while not response.isdigit() or int(response) > len(self.options) or int(response) <= 0 :
            response = input(MESSAGE)
        index = int(response)-1
        return index, self.options[index]

def ask(questions):
    return [input(question) for question in questions]