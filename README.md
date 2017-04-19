# so-desktop-notification
* Gives desktop notification every 60 seconds from given tags on
  StackOverflow. Only the first question is shown.

####Installation:
* Create a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtual-environments)
* While creating virtualenv use `--system-site-packages` option
* `pip install -r requirements.txt`
    * _Windows only_: Download TKinter (.whl file) from http://www.lfd.uci.edu/~gohlke/pythonlibs/ , and install it using `pip install tkinter_file.whl`

####Usage:
* `python script.py tag1 tag2 tag3`
* Not all tags might work, tags like - `Python 2.7` have to be checked.
