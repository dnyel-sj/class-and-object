# برنامه محیط و مساحت یک دایره را حساب میکند

# کلاس ایجاد شده برای محاسبه محیط و مساحا دایره
class Circle:
  def __init__(self, radius):
    self.radius = radius

  def get_area(self):
    return 3.14 * self.radius * self.radius

  def get_perimeter(self):
    return 2 * 3.14 * self.radius

# گرفتن شعاع مورد نظر از کاربر 
radius_circle = eval(input("Shoa dayere vared konid: "))
circle = Circle(radius_circle)
print("Masahat: ", circle.get_area())
print("Mohit: ", circle.get_perimeter())
