Workout planner is a photo app written in python in which the user can select a workout for a specific body part and
the app will show an image with a set of exercise targeting a specific muscle group. To use this app the user will need
to open the app folder in any python supported IDE in this project I used PyCharm. The user will need to be able to
understand how to open a python file on an IDE of their choice, for most IDE the file will automatically open if not, the
user will need to double click on this file "workout_planner.py" inside the project folder "workout_planner".
Once open the user will run the code by clicking on the green triangle or
play sign on the right top corner of PyCharm. After running the code, the PyCharm console will display the home
page of the app. The user will see a welcome message a list of options to choose from. From 1 to 7 the user can select
from the list of exercises available in the app and 0 to exit it. To select an option to user the enter a number within
the list on the menu and press the enter key or return key if it is a mac computer to validate the selection and the
app will display the result of the selection. If the user enters a selection which is not within the list the system
will print a warning message and redirect the user to the home menu.

IMPORTANT NOTE: WHEN RUNNING THIS APP ON YOUR COMPUTER MAKE SURE TO UPDATE THE IMAGE LOCATION ON THE CODE TO REFLECT THE
CORRECT LOCATION OF YOUR IMAGE FOLDER IN YOUR IDE YOU WILL NEED TO UPDATE THIS LINE OF CODE ACCORDINGLY:

"Image.open("/Users/samidollars/Desktop/github_projects/workout_app/"
                                           "/Image/fullbody.jpeg"))"
