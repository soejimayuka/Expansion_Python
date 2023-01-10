# print("こんにちはPython!")

# for i in range(10):
#  print(i)

# for item in ["a", "b", "c"]:
#   print(item)

# my_life = 5
# while my_life:
#   my_life -= 1
#   print(my_life)


# idx = 0
# while True:
#   if idx > 5:
#     break
#   idx += 1
#   print(idx)

users = [
  "Yo", "Ken","Nao","Shin","Lee"
]
# users.append("Miu")
# users.remove("Nao")

# print(users[0])
# print(users[0:2])
# print(users[1:])
# print(users[::2])
# print(users[::-1])


# リスト内包表記
users = [u.lower() for u in users if u.find("e") != -1]
# print(users)


# dictionary
user_dict = {
  "Yohei": 30, "John": 35
}
# print(user_dict["Yohei"])

# for k, v in user_dict.items():
#   print(k, v)

del user_dict["John"]
user_dict["Yohei"] = 31

# set
set_ = {
  "Tennis", "Ramen", "Programming"
}
# for s in set_:
#   print(s)

#tuple
nums = "One", "Two", "Three"
# for n in nums:
#   print(n)

# function
# def add(a,b):
#   return a + b
# result = add(10, 20)



# def pow(a, b=2):
#   return a ** b
# result = pow(10)



def create_date(
  year=0, month=0, date=0):
  return "..."
result = create_date(year=2017, date=10)


def get_user():
  return "Yohei", 30
result = name, age = get_user()

# print(result)

def get_genius():
  return ["Yamazaki", "Kosuge"]

get_genius()
