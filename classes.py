class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi, I'm {self.name}")


dan = Person("Dan Mwangi")
dan.talk()
bob = Person("Bob Smith")
bob.talk()


