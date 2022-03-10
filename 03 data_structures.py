#List
# my_list=["lucky","funmi","bright"] #a list is mutable because it can be modified
# print(my_list)

# my_list.append("vero") #this append function adds to the list 
# print(my_list)

# my_list[0]="ini" #this replaces whatever value at 0 with the new assignment
# print(my_list)

# my_list.insert(1,"kohol") # this inserts a value at a particular index
# print(my_list)

# my_list.remove("funmi") #this function removes an item from the list
# print(my_list)

# print(my_list[len(my_list)-1]) # this is to print out/access last item in a list

#Dictionary
# my_dict={"id":1,
#  "name":"lucky",
#  "is_programmer":True,
#  "salary":200,
#  "loans":[{"package":"student loan","amount":1000},
#           {"package":"car loan","amount":10000},
#           {"package":"marriage loan","amount":0}],
#  "languages":["french","english","spanish"], # a dictionary can contain a list
#  "exam":[{"lang":"eng","proficiency":100}]   #a dictinary can contain a list that contains a dictioary
#  }
# # print(my_dict.get("salary")) #how to retrieve a particular value
# # print(my_dict["salary"]) #how to retrieve a particular value

# print(my_dict.get("loans")[0].get("amount")) #retrieving amount from the student loan from the loans value

# #Sets
# my_set={"lucky","funmi","lucky","caleb","caleb"}
# my_set.add("mush")
# print(my_set)

#Tuples
my_tuple=("Hello","world","world")
# print(type(my_tuple)) #this is to find out what type of structure it is
print(my_tuple)

