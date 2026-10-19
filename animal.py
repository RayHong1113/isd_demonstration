class Duck():

    def speak(self):
        return "Quack"

class Dog():

    def bark(self):
        return("Bark")

def generic_method(speaker):
    print(speaker.speak())

generic_method(Duck())
generic_method(Dog())



