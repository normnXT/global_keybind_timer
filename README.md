# global_keybind_timer
Timer for logging time spent on task(s) without having to tab through windows. 

![Screenshot 2023-12-10 043915](https://github.com/normnXT/global_keybind_timer/assets/119769208/4c678499-5f11-4078-99a2-4a8a5d9e3421)


**Features**
* Starts recording time on keypress (F8) 
* Stops recording time on second keypress (F8) and adds to total
* Able to undo additions (shift+F8) to time
* Able to start a new session (shift+F9) and clear total time
* **Logs time and all user actions to .txt file** (file uses current date naming convention)

**Other info**
* Runs in command prompt window
* Presents time in hours and minutes, but measures in seconds (rounds to nearest minute)
* Need to ```pip install keyboard``` dependency
* Keybinds editable in run() function
* Script can be executed from provided .bat file, path may need updating if not using a PyCharm venv 
* Otherwise run it like any other script, with a basic command in command prompt window (edit path as necessary):
  
```
cd path\to\global_keybind_timer
```
```
python timer.py
```




