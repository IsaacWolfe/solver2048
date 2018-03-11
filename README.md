#Solver for 2048
###**Important** make sure Seleniumm is on the computer being used.
To install Selenium on Linux use:
* **pip3 install selenium**
* Make sure to download whatever **geckodriver** so that Firefox can be used
* Add the file path of Geckodriver to the the PATH variable (use **export PATH=$PATH:path/to/directory/** to add to current session, add export command to .bashrc to make it last)

This is a very basic solver using *Python3* and *Selenium 3.10.0* to load 2048 game and keep a basic pattern going until game is complete. It will loop until the page is closed.
