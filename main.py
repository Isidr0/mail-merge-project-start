#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# readlines() method to create list of invited_names.txt
with open("Input/Names/invited_names.txt") as data:
    names = data.readlines()

# create the starting_letter and store in sample variable
with open("Input/Letters/starting_letter.txt") as data:
    sample = data.read()

stripped_names = []

# for each name in names strip the new line.
for name in names:
    stripped_names.append(name.strip())

# for name in the stripped names file create a new name.txt file and replace the placeholder with the current name.
for name in stripped_names:
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as data:
        data.write(sample.replace("[name]", name))
    # print(name)


# print(names)

# replace() method to replace name in starting_letter.txt with names from list
# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)

# strip() method to eliminate leading and trailing spaces. I think it gets rid of newline \n as well.
# txt = "     banana    "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")