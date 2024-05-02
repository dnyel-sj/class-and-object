# برنامه که اسم طرف مقابل گرفته و بهش خوش آمد میگوید

#ایجاد کلاس برای گفتن خوشامد
class Greeter:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print(f"Salam {self.name} moshtagh didar!")

#گرفتن اسم از کاربر
user_name = input("Esm shoma chie? ")
greeter = Greeter(user_name)
greeter.greet()
