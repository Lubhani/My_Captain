#Creating a function
def most_frequent():
    #Create a dictionary
    data = input("Please enter a string:")
    count = dict()

    #Inserting values in the dictionary
    for letters in data:
        letters=letters.rstrip()
        for letter in letters:
            if letter not in count:
                count[letter]=1
            else:
                count[letter]+=1

    #Sorting the dictionary in ascending order
    for key,val in sorted(count.items()):
        print(key, "=", val)

most_frequent()
