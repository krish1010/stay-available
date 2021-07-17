# stay-available

Recent changes in many office communication application (like MS Teams) policies makes you go from 'Available' or 'Busy' to 'Away' if the mouse is not moved or clicked for sometime. 

This simple python script takes care of this issue.

Usage:
- Clone the project: `https://github.com/krish1010/stay-available.git`
- Change to the project directory: `cd stay-available`
- Create a virtual environment: `python -m venv venv`
- Activate the virtual environment: `venv\Scripts\activate.bat`
- Install requirements: `pip install -r requirements.txt`
- Make a copy of `move_mouse_example.bat`
- Rename the file to `move_mouse.bat`
- Edit `move_mouse.bat` in the following manner: `"path\to\python.exe" "path\to\driver.py" %1 %2 %3 %4`
- Run the file (optionally with arguments): $1, $2, $3, $4


        $1: total_time
            Total time the function will run in hours.
        $2: wait_time
            Time to wait between completion check in seconds.
        $3: pixels
            Pixels to move the mouse.
        $4: duration
            Duration to animate the mouse movement.
