class User():
    first_name =''
    last_name = ''
    email_address = ''
    phone_number = ''
    alergies = ''
    food_diet = ''
    user_type = ''


class MenuItem():
    name = ''
    description = ''
    serving_size = ''
    allergens = ''

class Meal():
  name = ""
  serving_size = ""
  full_description = ""
  ingredients = ""

class Price():
  amount = ""
  quantity = ""
  totalPrice = ""

class Order(Meal, Price):
  orderId = ""
  orderedMeal = Meal.name
  quantity = Meal.serving_size
  short_description = ""
  isPacked = False
  additional_needs = ""
  price = Price.totalPrice


user = User()
user.first_name = 'Ini'
user.last_name = 'Arthur'
user.phone_number = '837727372838'
user.email_address = 'ini.arthur@meltwater.org'
user.alergies = 'watermelon'


