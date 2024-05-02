#برنامه درجه را به فارانهایت گرفته و به سانتی گراد تبدیل میکند

#کلاس ایجاد شده برای محاسبات تبدیل
class TemperatureConverter:
  def __init__(self):
    self.conversion_factor = 5 / 9

  def convert_fahrenheit_to_celsius(self, fahrenheit):
    celsius = (fahrenheit - 32) * self.conversion_factor
    return celsius

# نشان دادن درجه تبدیل شده به کاربر در خروجی
converter = TemperatureConverter()
fahrenheit_value = float(input("Damaye hava be faranhait chand daraje ast? "))
celsius_value = converter.convert_fahrenheit_to_celsius(fahrenheit_value)
print(f"Damaye hava be cantigrad {celsius_value:.2f} daraje ast!")
