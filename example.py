lst = [1, 2, 3]
str = "I am Data scientist"
list = 5000000

# print(type(lst))
# print(type(str))
# print(type(list))

# lst = lst.index(3)
# print(lst)

from oops_proj import Chartbook
user = Chartbook()
print(user.id)


# using static method directly from rather the object
Chartbook.set_id(10)
user1 = Chartbook()
print(user1.id)

Chartbook.set_id(11)
user2 = Chartbook()
print(user2.id)














# print(user.get_name())

# user.set_name('xyz')
# print(user.get_name())
# #user.send_msg()
# # user = Chartbook()


# fuction vs method 
# lst = [1, 2, 3, 4, 4]
# a1 = len(lst)
# print(a1)

# # method
# user = Chartbook()
# user.send_msg()