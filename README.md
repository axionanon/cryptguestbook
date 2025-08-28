# Python Project: Hotel Secret Guestbook

Objective

A simple Python project demonstrating encryption, basic file handling, and message encoding/decoding. It mimics a "dead drop" system where users leave encrypted messages in a mysterious hotel guestbook. Only users who know the correct passphrase can decrypt and read the message.

Features

• Uses cryptography.fernet to securely encrypt and store messages.<br>
• Collects user’s name and a secret passphrase to store and decrypt messages.<br>
• Stores encrypted messages in a folder (secrets/) as JSON files, named by user.<br>
• Each message is encrypted with a passphrase, and users need the correct passphrase to decrypt.<br>
• Simulated typing effect using time.sleep. and basic python styling.<br>

Usage

• Download the Python file GUESTBOOK.py <br> 
• Run it in your preferred IDE. It should automatically handle dependencies and prompt you for inputs. <br>
• Follow the prompts to leave a message or decode one. <br>
** *the files will be stored locally on your computer because this is not a web version. <br>
you won't be able to see any entries other than your own.*

Requirements <br>

cryptography  
colorama  
pyfiglet


If you would like to play an interactive web version, begin here: 

<i>Two words in one — a single name <br>
Point to a user, let’s start the game. <br>

The first arrives when hands align, No sun remains, no church bells chime. The world is still, the hour late—<br>
A time which strikes long after eight.<br>

The second wears a cap, he works the floor, He guides the guests, guards lobby door.<br>
With a ding and he jumps near— Who stands in uniform right here?<br>

Where pictures linger and stories fade,<br>
Search where many squares are laid.</i> <br>

(Don't worry—your inputs are encrypted. Even I can't see them.)
