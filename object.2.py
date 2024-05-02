class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def calculate_birth_year(self):
    self.birth_year = 2024 - self.age

  def get_birth_year(self):
    return self.birth_year

person_name = input("Esm shoma chie? ")
person_age = int(input("Sen shoma cheghadr ast? "))
person = Person(person_name, person_age)
person.calculate_birth_year()
print(f"Shoma dar sal {person.get_birth_year()} be donya amdid!")
