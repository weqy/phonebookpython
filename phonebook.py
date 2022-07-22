names = [] # list of names
phone_numbers = [] # list of phone numbers
num = 3 # total of 3 profiles


for i in range(num): # decides where in the phone book individual will go
    name = input("Name: ") # search term 1
    phone_number = input("Phone Number: ") # search term 2

    names.append(name) # adds to list of names
    phone_numbers.append(phone_number) # adds to list of numbers

print("\nName\t\t\tPhone Number\n") # cosmetic - separates name and phone number

for i in range(num): # format for information
    print("{}\t\t\t{}".format(names[i], phone_numbers[i])) # printing names and numbers seperate

search_term = input("\nEnter search term: ") # searching for an individual

print("Search result:") # cosmetic -- separates search result from info

if search_term in names: # search term fits one of the individuals
    index = names.index(search_term) # looks for term in names
    phone_number = phone_numbers[index] # looks for term in numbers
    print("Name: {}, Phone Number: {}".format(search_term, phone_number)) # prints result

else: # search term does not fit
    print("Name Not Found") # prints that it could not find an individual
