my_list=["lucky","funmi","bright"] #a list is mutable because it can be modified
print(my_list)

my_list.append("vero") #this append function adds to the list 
print(my_list)

my_list[0]="ini" #this replaces whatever value at 0 with the new assignment
print(my_list)

my_list.insert(1,"kohol") # this inserts a value at a particular index
print(my_list)

my_list.remove("funmi") #this function removes an item from the list
print(my_list)

print(my_list[len(my_list)-1]) # this is to print out/access last item in a list