class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")
sergio = Person("Sergio")
sergio.talk()