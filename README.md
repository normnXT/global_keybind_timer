# global_keybind_timer
Timer for logging time spent on task(s) without having to tab through windows to click buttons. Plays a beep/alarm after the timer has been inactive for 5 minutes, for productivity reasons, to assist in staying active and keeping track of time while completing tasks or working from home.

**1. Setting custom keybindings, turning the beep timer on/off, and adjusting the time interval is done in settings.json file.**

**2. Logs time and all user actions to .txt file for record keeping**

**3. Script can be executed from provided run.bat file, it checks for a venv and sets one up along with dependencies if it does not already exist.**

![Screenshot 2023-12-10 043915](https://github.com/normnXT/global_keybind_timer/assets/119769208/e67cc037-79ce-413e-940d-6f70e3756507)

**Timer Features**
* Presents time in hours and minutes (rounds to nearest minute), but keeps time in seconds 
* Starts recording time on keypress (F8) 
* Stops recording time on second keypress (F8) and adds it to total
* Able to edit total time (shift+F7)
* Able to undo last addition to time (shift+F8) 
* Able to start a new session and clear total time (shift+F9)


**Other info**
* Need to ```pip install keyboard``` and ```pip install playsound==1.2.2``` dependencies if not using the .bat file.
* If not using .bat, run timer.py like any other script, with a basic command in command prompt window (edit path as necessary):
  
```
cd path\to\global_keybind_timer\src
```
```commandline
python timer.py
```

Install dependencies from requirements.txt file:

```commandline
pip install -r requirements.txt
```




