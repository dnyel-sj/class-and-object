#برنامه یک عدد را گرفته و در خروجی نشان میدهد عدد زوج است یا فرد

# کلاس ایجاد شده برای تشخیص زوج یا فرد بودن عدد
class NumberChecker:
  def __init__(self, number):
    self.number = number

  def is_even(self):
    return self.number % 2 == 0

  def is_odd(self):
    return not self.is_even()

#گرفتن یک عدد از کاربر
user_number = int(input("Yek add vared konid: "))
number_checker = NumberChecker(user_number)

# ایجاد شرط برای زوج یا فرد بودن عدد
if number_checker.is_even():
  print(f"{user_number} Yek addd zoj ast!")
else:
  print(f"{user_number} Yek add fard ast!")
