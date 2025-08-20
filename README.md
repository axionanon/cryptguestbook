# Python Project: Hotel Secret Guestbook

*Working on a web version

Objective

A simple Python project demonstrating encryption, basic file handling, and message encoding/decoding. It mimics a "dead drop" system where users leave encrypted messages in a mysterious hotel guestbook. Only users who know the correct passphrase can decrypt and read the message.

Features

• Uses cryptography.fernet to securely encrypt and store messages.<br>
• Collects user’s name and a secret passphrase to store and decrypt messages.<br>
• Stores encrypted messages in a folder (secrets/) as JSON files, named by user.<br>
• Each message is encrypted with a passphrase, and users need the correct passphrase to decrypt.<br>
• Simulated typing effect using time.sleep. and basic python styling.<br>

Usage

• Download the Python file GUESTBOOK.py <br> <br>
• Run it in your preferred IDE. It should automatically handle dependencies and prompt you for inputs. <br><br>
• Follow the prompts to leave a message or decode one. <br>
** *the files will be stored locally on your computer because this is not a web version*

Requirements <br>

cryptography  <br> 
colorama  <br>
pyfiglet
