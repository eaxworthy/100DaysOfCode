#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt', 'r') as file:
    names_list = [line.rstrip('\n') for line in file.readlines()]

letter_text = open('./Input/Letters/starting_letter.txt', 'r').read()

for name in names_list:
    file_name = './Output/ReadyToSend/letter_for_'+ name + '.txt'
    open(file_name, 'w').write(letter_text.replace('[name]', name))
