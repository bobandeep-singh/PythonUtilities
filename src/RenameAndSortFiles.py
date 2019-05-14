"""
https://docs.python.org/3/library/os.html

You can do various kind of stuffs with this simple script.
You can rename the files and sort them is how ever fasion you like.
This is not a general one but it is like a starting point where you have the basic code to start with.
"""


import os

# os.chdir will get me to the directpry I want.
os.chdir('C:/Users/boban/Desktop/Learning Dariya/AllBooks/SPRING')

# os.getcwd() will give you the Current Working Directory
# print(os.getcwd())

for f in os.listdir():
    # print(f)  ### List of all the items in the directory
    # Now we will split the extension of the file using os.path.splitext() function
    f_name, f_extension = os.path.splitext(f)
    # print(os.path.splitext(f))                    #####tupple is returned
    # print('{}{}'.format(f_name, f_extension))
    
    # print(f_name.replace(' ', ''))

    # print(f_name.split(' #'))
    f_title, f_num = f_name.split(' #')

    # Here I have trimmed all the spaces from the name and then I want to pad my number value with 0
    # If my number is 3 then zfill will make it 03
    f_title = f_title.replace(' ', '')
    f_num = f_num.strip().zfill(2)

    print('{}-{}{}'.format(f_num, f_title,f_extension))
    new_name = '{}-{}{}'.format(f_num, f_title,f_extension)

    # Now rename the file
    os.rename(f, new_name)