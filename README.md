# StarshipPasswordManager
This is a repository meant to store a simple password generation and checking program for a programming class.
 
Overview
The purpose of this software is to allow users to create custom semi-random strong passwords that obey to modern password-validation standards. Additionally, users can check their own passwords against those standards to ensure security. This software is known as the Starship Password Manager and is the solution to password security problems. Users are able to run the program from the python terminal or through the installable .exe file. 
Passwords are generated from a combination of a random string and the reversed letters of the user’s name. This gives the password both memorability and strength. The password is then copied to the user’s clipboard for use with online programs.
Passwords are checked by testing them against a series of checks to find lowercase letters, uppercase letters, numbers, and special characters, as well as the total amount of characters in the password being at least 12. If all those cases are met, the program confirms that the password is valid. 
 
Usage
The Starship Password Manager runs in the python shell. It will start with a welcome message and a menu screen, along with the password rules. 
The rules are as follows:
Passwords must:
•Contain uppercase and lowercase letters.
•Contain letters and numbers.
•Contain special characters.
•Contain at least 12 characters.
The three options in the menu screen can be selected by typing the first letter of each available option. A detailed breakdown of each option is presented below.
 
Check Password (C): 
This option is used for checking existing passwords against the password rules. When this option is selected, you will be prompted for a password. The typed password will then be checked against the rules and will either say that the password is valid or that it is invalid, and the rules should be checked. This will continue until a valid password is typed.

Generate Password (G): 
This option is used for generating new and unique passwords. When this option is selected, users will be prompted for their name. This will be used as the middle part of the password. Then, 12 random characters will be generated from a valid character list. These random characters will be split, with the name reversed in the middle. The program will then output the reversed name, the random digits and the complete password. This password will be saved to the user’s clipboard to be pasted wherever needed.

Quit (Q):
This option is used to end the program. If executed in thonny with the .py installation, quit will simply end the program. If used in the .exe installation, the program will stop and the window will automatically close. The program can also be ended in .py by pressing the red end button or in .exe by simply closing the window.
These menu options are looped until quit is used. As many passwords as the user wants can be checked or generated, as long as quit is not used. 
 
Installation and Setup
There are two ways to install the Starship Password Manager on a compatible computer. Windows operating system users will be able to run the program from a python installation or from the exe package. Mac and linux users are limited to running Starship passwords from a python installation for the current build.
This next paragraph will contain instructions for installing and running the .exe file. Mac and Linux users should skip ahead to the python installation steps.
.exe installation (Windows Only)
To start with the .exe file, locate and download the folder labeled MMFinalPasswordProject from github. Once downloaded, unzip the folder and locate the .exe within. It is recommended to make a shortcut to either the desktop or taskbar with the .exe file so it can be found easily again. Upon running, this .exe will open a console window where the program will run and be interacted with. This window will close automatically when quit is selected in the menu.
 
How the .exe method folder will appear, with the exe file selected


.py installation (All OS)
Start by downloading the project off my github page linked in the beginning of this document. Extract the files to any folder you choose. Now you will need a python installation. The easiest way to install and run the password manager without python already installed is to install thonny, the IDE used to create the password manager. The installation can be found here: https://thonny.org/. Once thonny is installed on the user computer, open the python file downloaded from the github using the file->open menu. Simply hit the green run button to start the password manager and it will run in the terminal at the bottom of the window.
Github Link (Used for all install methods):
https://github.com/MaxMcCalla/StarshipPasswordManager
 
Libraries
This project uses two external libraries, random and pyclip. Both libraries can be installed into Thonny by using tools -> manage packages and searching for them in the top search bar. Clicking install on these libraries and letting them install allows Starship to run without returning errors. 
TLDR: install random and pyclip. Tools->manage packages->search.
 
FAQs and Support
Q. Does the password manager run on all major operating systems?
A. Yes, but only for the .py installation
Q. I’m getting something that says “Your imports have not been added correctly.” What does that mean?
A. The starship password manager uses some external libraries. Please review the library page of this document and follow the steps to add each of the libraries to the program.
Q. I accidentally changed some code in the program and it doesn’t run anymore. What should I do?
A. Re-download the .py file from the github and try again.
Q. My antivirus is saying it won’t let the .exe run.
A. Use the .py method to run the code instead. Antivirus programs are known to attack some exe files generated from python.

For any support or unique bugs, please contact Max through the github errors page or at maxwellmccalla@gmail.com. Please include Starship Password Manager in the subject line.
 
License Information
Thonny is used under the MIT open source license. https://opensource.org/licenses/MIT
Pyclip is used with the apache software license. https://www.apache.org/licenses/LICENSE-2.0.txt
Starship Password manager is free to use and modify, and the code is openly posted on github. 
