'''
Write a program to read through the mbox-short.txt
and figure out who has sent the greatest number of
mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the
person who sent the mail. The program creates a
Python dictionary that maps the sender's mail
address to a count of the number of times they
appear in the file. After the dictionary is
produced, the program reads through the dictionary
using a maximum loop to find the most prolific committer.
'''

name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short.txt"

with open(name) as handle:
    sender_count = dict()

    for line in handle:
        line = line.rstrip()
        if not line.startswith('From '):
            continue

        words = line.split()
        sender = words[1]
        sender_count[sender] = sender_count.get(sender, 0) + 1

    max_sender = None
    max_count = 0
    for sender, count in sender_count.items():
        if count > max_count:
            max_sender = sender
            max_count = count

    print(max_sender, max_count)
