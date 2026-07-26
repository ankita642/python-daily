class Greeting:
    def say_hello(self):
        return "Hello!"

class Spanish(Greeting):
    def say_hola(self):
        return "¡Hola!"

class French(Greeting):
    def say_bonjour(self):
        return "Bonjour!"

def greet_all(languages):
    for lang in languages:
        print(lang.say_hello())

greet_all([Spanish(), French()])
