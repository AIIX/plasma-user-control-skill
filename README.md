# Mycroft plasma-user-control-skill
This skill integrates Plasma 5 Desktop Internals with Mycroft which enables users to Lock Screen, Switch Users, Logout, Control Brightness and Panel Positions of the Desktop.

#### Installation of skill:
* Download or Clone Git (run: git clone https://github.com/AIIX/plasma-user-control-skill inside /opt/mycroft/skills)
* Create /opt/mycroft/skills folder if it does not exist
* Extract Downloaded Skill into a folder. "plasma-user-control-skill". (Clone does not require this step)
* Copy the plasma-user-control-skill folder to /opt/mycroft/skills/ folder

#### Installation of requirements:
##### Fedora: 
- sudo dnf install dbus-python
- From terminal: cp -R /usr/lib64/python2.7/site-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib64/python2.7/site-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

##### Kubuntu / KDE Neon: 
- sudo apt install python-dbus
- From terminal: cp -R /usr/lib/python2.7/dist-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib/python2.7/dist-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

* For other distributions:
- Python Dbus package is required and copying the Python Dbus folder and lib from your system python install over to /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/.

##### How To Use: 
###### Lockscreen
- "Hey Mycroft, lock the screen "
- "Hey Mycroft, lock screen "

###### Switch Users
- "Hey Mycroft, switch current user "
- "Hey Mycroft, switch user "

###### Logout Users
- "Hey Mycroft, logout of the current session "
- "Hey Mycroft, logout session "

###### Increase Brightness
- "Hey Mycroft, increase the brightness "
- "Hey Mycroft, increase brightness "

###### Maximum Brightness
- "Hey Mycroft, increase to maximum brightness "
- "Hey Mycroft, maximum brightness "

###### Decrease Brightness
- "Hey Mycroft, decrease the brightness "
- "Hey Mycroft, decrease brightness "

###### Minimum Brightness
- "Hey Mycroft, decrease to minimum brightness "
- "Hey Mycroft, minimum brightness "

###### Change Location of Default Panel
- "Hey Mycroft, move panel to top/bottom/left/right"
- "Hey Mycroft, move the default panel to top/bottom/left/right"

###### Add Widget To Desktop
- "Hey Mycroft, Add widget to desktop 'widgetname'"

###### Add Widget To Default Panel
- "Hey Mycroft, Add widget to panel 'widgetname'"

## Current state

Working features:
* Add Widgets to Desktop/Panel
* Lock Screen
* Switch Users
* Logout
* Brightness Control
* Moving Default Panel

Known issues:
* None

TODO:
* None
