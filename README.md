# global_keybind_timer
Timer for logging time spent on task(s) without having to tab through windows. 

**Features**
* Logs time and all user actions to .txt file that is named the current date  
* Starts recording time on keypress (F8) 
* Stops recording time on second keypress (F8) and adds to total
* Able to undo additions (shift+F9) to time
* Able to start a new session (shift+F8) and clear total time

**Other info**
* Presents time in hours and minutes, but measures in seconds (rounds to nearest minute)
* Need to ```pip install keyboard``` dependency
* Keybinds editable in run() method, simply edit the strings
* Script executed from .bat file 
* Runs in command line window



