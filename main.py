import pandas as pd
import smtplib
import random

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pd.read_csv('birthdays.csv')
print(data)
print("------------------")
names = data['name']
names_list = names.to_list

NAME = "[NAME]"
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.

# creating a variable and storing the text
# that we want to search
search_text = NAME

# creating a variable and storing the text
# that we want to add
replace_text = "replaced"

# Opening our text file in read only
# mode using the open() function
with open(r'letter_1.txt', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data = file.read()

	# Searching and replacing the text
	data = data.replace(search_text, replace_text)

# Opening our text file in write only
# mode to write the replaced content
with open(r'letter_1.txt', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data)

# Printing Text replaced
print("Text replaced")



