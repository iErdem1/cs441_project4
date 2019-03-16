# Project 4 -Cross Platform Image Viewer w/ Kivy&Python-
- Binghamton University Spring 2019 CS441 Gaming for Mobile Platform class "Image Viewer" project.

## LICENCE

```
Copyright 2019 A. Ihsan Erdem <ihsan@itugnu.org>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```

## Installation for Debian Based GNU/Linux Distros
- Clone project from Git
- Use Python version 3.6.x
- Run <code>pip install -r requirements.txt</code> or install **virtualenv** manually
- Setup virtualenv <code>virtualenv venv -p python3.6</code>
- Activate virtualenv <code>source venv/bin/activate</code>
- To install Kivy:
```bash
    $ sudo add-apt-repository ppa:kivy-team/kivy
    $ sudo apt-get update
    $ sudo apt-get install python3-kivy
```
- On project directory create a <code>img</code> subdirectory and add some images.
- To run the program you may use <code>python3 main.py</code> command on terminal.
 

## Project Description
- Project based on Kivy Framework which is Python's cross platform application builder.
- After couple of Objective C and Swift hacks I've decided to learn new technologies. 
I choose Python related framework because I am familiar Python programming language so Kivy
was easy to adapt. But still I need to learn too much specifications.
- Kivy is basically a cross platform graphical interface library of Python.
You can develop desktop applications and also you can build your app to Android and
iOS via Buildozer. Kivy use pygame as an engine. Also, render window tools via SDL and OpenGL
so Kivy apps do not look like native iOS and Android applications.
- Kivy is a Free Software and licenced under MIT. So if you want to check source code you can
go <https://github.com/kivy/kivy>

- Project basically displays images in specified path. Now it supported only 4 format types
which are <code>png, jpeg, jpg, gif</code>
- If you want to add some new formats you can fork the project.
- If you have any questions or curiosities do not hesitate a sending a note via `ihsan@itugnu.org`
