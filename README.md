# BTD6-AI

This is code made to run a bot that plays Bloons Tower Defense 6.

Because it uses hotkeys, Windows will think that this is a keylogger virus. To prevent it from deleting the important code:
Go to Virus & Threat Protection -> Manage Settings -> Add or Remove Exclusions -> Yes -> Add an Exclusion -> Folder -> Select the folder where you want to put this code
To use it, go into main.py and replace the githubDir on Line 18 string with the path to where you have unzipped this folder.
Make sure you have Python 3.6 or higher, and all of the imports from Line 1 to Line 8 downloaded, if you do not, use pip3 to install all of them.
I think you will also need java and something on there downloaded, but I cannot remember.
Run main.py after opening the Monkey Meadow map and selecting Easy difficulty, with the game not yet started on Round 1

Please read the functions and assumptions below:

ASSUMPTIONS:
For now, this code only works on Monkey Meadow on Easy difficulty, with Quincy as your selected hero, and Monkey Knowledge disabled
Assumes that your screen is 1980 by 1080
Assumes that it will have read and write permissions in the folder it is placed in

FUNCTIONS:
Can place and upgrade Monkeys
Keeps track of the monkeys and upgrades it has
Will eventually improve and figure out the losing/winning strategies
