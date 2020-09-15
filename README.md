# OCALS - Online Class Automatic Login System #
### Automatic Login System for Google Meet Classes ###
**Completed on:** 15 September 2020 05:03 PM

**Coded By:**     Sagar Dev Achar
# #
### Introduction ###

To all the lazy ones out there, here's something for you. Attend your Online Classes automatically at the click of a button.

Launch OCALS in the morning and just watch it do it's work. Automatically Join and Exit classes without moving a finger with OCALS
# #

### Quickstart Guide to using OCALS ###

1. Download and Extract the contents of this Repository
1. Double Click on the *OCALS.exe* file inside the *Distributable* folder
1. Enter your Username and Password when asked
1. Enjoy!

**NOTE:** 
- Do NOT close the new Google Chrome Window opened by the program
- Do NOT close the running application
- Do NOT move any files in the OCALS Folder
# #

### Description ###

**Selenium** + **ChromeDriver** based script which simulates a student's visit and actions on *Google Meet* and automatically waits, enters and exits Google Meet classes on the basis of their start times. Microphone and Video access are disabled by default before joining a Session

Works on the following assumptions:
- Google Meet is the medium for the classes
- Duration of classes is 1 hour each
- The classes schedule is updated in the Student's Google Calendar
- The user holds an average and stable internet connection

An **Automated Chrome** instance is used as the operating browser.

The Python Script is packaged into an executable with the help of the **pyinstaller** module
# #
### Respository Contents ###
- #### /Distributable: 
	Contains the Packaged Executable *([OCALS.exe](https://github.com/SagarDevAchar/OCALS/blob/master/Distributable/OCALS.exe))* and ChromeDriver *([chromedriver.exe](https://github.com/SagarDevAchar/OCALS/blob/master/Distributable/chromedriver.exe))*
- #### /Source Code:
	Contains the working Python Code *([OCALS.py](https://github.com/SagarDevAchar/OCALS/blob/master/Source%20Code/OCALS.py))* for the project. Accessible to all coders via the *MIT Licence*
- #### LICENSE:
	MIT License for this project *(C) 2020 Sagar Dev Achar*. Click *[here](https://choosealicense.com/licenses/mit/)* to learn more about the permissions offered by this license
- #### README.md:
	Here you are!
- #### SECURITY.md:
	Security Declaration for the code and executables
# #
### System Requirements ###

- OS: Windows 10 / 8.1 / 8 / 7
- Google Chrome (v85.0 or above)
- A few MB of RAM and Storage
