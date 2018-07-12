# get_status_from_webpage.py
# Prof. Lee (cs1110-prof@cornell.edu)
# Feb 14 2018

""" Allow user to repeatedly query a file to find out the
    open/closed status of a class lecture or section. """


import a1
import urllib.request
import sys

data_name = input('Enter a roster website URL, including the http part: ')
try:
    data_source = urllib.request.urlopen(data_name)
    data_text = data_source.read().decode('utf-8')
except ValueError:
    print("Something is wrong with the web address or webpage.")
    sys.exit()

msg = 'The webpage has been loaded.\n\n'
msg = msg + 'Note that this program does NOT refresh its data;\n'
msg = msg + 'if the webpage gets updated,'
msg = msg + ' you need to restart this program to get the new information.\n'
print(msg)

# Allow repeated queries until the user types 'q'
init_prompt = 'Enter the class number, probably a 5-digit number'
init_prompt = init_prompt + ' (or "q" to quit): '
num=input(init_prompt)
while num != "q":
    try:
        print(a1.label(num, data_text) + " " + a1.open_status(num, data_text))
    except:
        msg = "I couldn't process the input; "
        msg = msg + "try a different number (or fix any bugs in a1.py)."
        print(msg)
    num=input('Enter the class number (or "q" to quit): ')
