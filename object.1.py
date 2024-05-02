class Greeter:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"Salam {self.name} moshtagh didar!")

user_name = input("Esm shoma chie? ")
greeter = Greeter(user_name)
greeter.greet()
