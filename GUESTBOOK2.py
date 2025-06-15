#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 26 21:20:54 2025
"""
#importing for style purposes
from colorama import Fore, Style, init
from pyfiglet import figlet_format
from cryptography.fernet import Fernet
import time
import json
import os

init()
# initialising now. thinking of this as turning on a styling engine.
if not os.path.exists("secret.key"):
    with open("secret.key", "wb") as f:
        f.write(Fernet.generate_key())

def load_key():
    return open ("secret.key", "rb").read()
fernet = Fernet(load_key())
    
# TYPING effect function
def type_out(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True) #'' indicates an empty string, meaning no space/newline — nothing. 
        time.sleep(delay)                 #it's telling print() to not add anything after each character.
    print()
    #we end with print to move the cursor to a new line after the typing loop finishes. Otherwise, next output would continue on same line.
#decoding function
def decode_message():
    type_out("Please enter the guest name:")
    name=input("Name: ").strip()
    
    filename = f"secrets/{name.lower().replace(' ', '_')}.json"
    
    #check if file exists
    if not os.path.exists(filename):
        type_out("We do not see that name in the guestbook.")
        return
    #load file and compare secret passphrases
    with open(filename, "r") as file:
        entry = json.load(file)
    #Let the user attempt the passphrase 3 times via a loop   
    attempts = 3
    while attempts > 0:
        code = input("Passphrase: ").strip()
        if code == entry["code"]:
            decrypted_message = fernet.decrypt(entry["message"].encode()).decode()
            type_out(f"\nMessage from {entry['name']}:\n") #use ' instead of quotations because we already used quotation marks
            type_out(decrypted_message)
            return
        else:
            attempts -= 1
            type_out("Incorrect passphrase. Access refused.\n")
    type_out("All attempts at decryption used. This incident will be reported to the concierge.")
        
#welcome message style   
print(Fore.RED + Style.BRIGHT)

# WELCOME MESSAGE 
type_out("🛎️ ding ding\n") 
#end with \n so after the sentence types out, the cursor moves to the next line
type_out("Ah. You've arrived.\n")

type_out("We are terribly pleased...and simultaneously concerned...to welcome you to Hotel Lecarré.")
type_out("Please do not ask about the 13th floor.\n")

type_out("Now then. Before we can assign you a room or ask pointed questions about your past, we must know:\n")

type_out("What name shall we enter into our guestbook?")
name = input("Name: ")
print()

type_out(f"Thank you, {name}. Your check-in is almost complete. But as you may have already guessed - and if you haven't, please begin guessing immediately — Hotel Lecarré is no ordinary hotel.\n")

type_out("Our guestbook is not a guestbook. It is a collection of secret messages disguised as polite remarks, which can only be read if you possess an alarming familiarity with someone else's name.")
type_out("A dead drop, essentially.\n")

type_out("You may leave a secret message...")
type_out("Decrypt one...")
type_out("Or unlock the entire guestbook with a masterkey, which we do NOT recommend.\n")

type_out("Would you like to leave a message?")
type_out("Choose: YES / NO / HOW VERY DARE YOU")

choice = input(">>> ").strip().upper() #input prompts the user and retrieves text
print()    #strip and upper remove spacing and converts input to caps so there's more freedom in answer format.

if choice=="YES":
    type_out("Marvelous. Or at the very least, deeply suspicious.\n")
    type_out("Please type your message below.")
    message=input()
    
# MESSAGE STORAGE - using json for this

#Create folder to hold messages - aka secrets - if it doesn't already exist
    if not os.path.exists("secrets"):
        os.makedirs("secrets")
    type_out("Please enter a secret passphrase to lock your entry (at least 5 characters with no spaces):")
    code=input("Passphrase: ")

#adding something to ensure the above 5 character rule is followed
    while len(code) < 5:
        type_out("Ah, too brief. We insist on five characters, at least.")
        code=input("Passphrase: ")
        
#encrypt message before saving
    encrypted_message = fernet.encrypt(message.encode()).decode()
    
    entry = {
        "name": name,
        "code": code,
        "message": encrypted_message
        }

    filename = f"secrets/{name.lower().replace(' ', '_')}.json"
#make the filename lowercase and replace spaces w/ underscore - neatening up the file
    with open(filename, "w") as file:
        json.dump(entry, file, indent=4)
        print()
        type_out("Your message has been scrambled. Whether it will be decoded is now someone else's unfortunate concern.")
  
    type_out("Would you like to decode an entry in the guestbook now?\n")
    type_out("YES/NO")
    if input(">>> ").strip().upper() == "YES":
        decode_message()
    else:
        type_out("Very well. Perhaps another time. 🕯️")

        
elif choice=="NO":
    type_out("Very well. Silence is, in its own way, a message.\n")
    type_out("...Or did you want to possibly...decode a message instead?")
    type_out("Choose: Indeed / I SAID NO!")
    
    followup = input(">>>").strip().lower()
    #print(f"[DEBUG] followup: {followup}")
    if followup == "indeed":
        decode_message()
    else:
        type_out("Very well. We respect your...discretion.")
    
elif choice=="HOW VERY DARE YOU":
    type_out("Touché.\n")
    type_out("Your indignation has been noted in your file, alongside “refused the mini-bar” and “suspected of knowing too much.”\n")
    type_out("But let it be known: those who do not leave messages are often the most suspicious of all.\n")
    type_out(f"Enjoy your stay, {name}.")
    
else:
    type_out("Hmm. That wasn’t one of the options, but it’s noted in the guestbook anyway.")

