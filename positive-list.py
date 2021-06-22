# Create a list
list_range = int(input("Enter the length of list:"))
count = 0
list1= []
while count<list_range:
    li = int(input("Enter a number:"))
    list1.append(li)
    count= count+1
print("List:" list1)

#Create a list of positive numbers in list1
pos_list = []
for num in list1:
    if num>=0:
        pos_list.append(num)
pos_list.sort()
print("Sorted list:", pos_list)
