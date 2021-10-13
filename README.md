# rememberthee-website
Source code for www.rememberthee.com - the marketing website for Remember Thee.

## Technologies
Backend
-  [Python](https://www.python.org) 3.10.0
-  [Flask](https://flask.palletsprojects.com/en/2.0.x/) 2.0.2

Frontend
-  [Bootstrap](https://getbootstrap.com)

## Installation
Reference Documentation:
- [Flask Installation](https://flask.palletsprojects.com/en/2.0.x/installation/)
- [venv](https://docs.python.org/3/library/venv.html#module-venv)

Clone the git repository into your file system and navigate to the project root:
```
% git clone
```

Make sure you have Python 3 installed on your machine.
```
% which python3
/usr/local/bin/python3
```
or
```
% python
Python 3.10.0 (v3.10.0:b494f5935c, Oct  4 2021, 14:59:20) [Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Create a virtual environment using the python module [venv](https://docs.python.org/3/library/venv.html#module-venv).

If you don't already have a `.venv` directory in your file system, I would recommend creating it in your root directory.
```
% mkdir ~/.venv
```

Then create your virtual environment in that `.venv` folder.
```
% python3 -m venv ~/.venv/rememberthee
```

Then activate your virtual environment:
```
% source ~/.venv/rememberthee/bin/activate
```

Next you need to download Flask and Flask-Mail. Make sure you have [pip](https://pypi.org/project/pip/) installed:
```
% pip install Flask
% pip install Flask-Mail
```

## Development
When you begin development, make sure you're in your virtual environment:
```
% source ~/.venv/rememberthee/bin/activate
```

Turn on debug mode:
```
% export FLASK_ENV=development
```

Then execute `flask run` and navigate to `localhost:5000` in your browser.

## Deployment
https://help.pythonanywhere.com/pages/UploadingAndDownloadingFiles
- Need to automatically detect perform new packages downloads and package updates
