# Usage Instructions #

1. Enter the login credentials (G-Mail ID and Password) when input is requested

1. Please wait for Login to be authorised by Google OAuth (via StackOverflow). If login is unsuccessful, the program will be exited on command after 10 seconds

1. If the login is successful, the program will redirect you to Google Meet and handle the rest of the process

1. The Script will automatically launch Google Meet Sessions, mute audio and turn off video and join the class with a maximum delay of a few seconds from the start time

1. The Script will automatically close the session after an hour and wait for the next session or exit depending on the day's schedule

# Alerts #

- Do **not** terminate the Automated Chrome Window. This will lead to the program crashing
- Do **not** terminate any chromedriver instance running in the background. This will lead to the program crashing
- Do **not** perform any clicks or keystrokes on the Automated Chrome Session until you are in a class
- Do **not** exit a class prematurely as this will lead to the program crashing
