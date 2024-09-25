# A small web application to store code (kinda like pastebin)
Me and my team at MISIS University made it so it could, using ML, 
automatically recognise which code language you wrote the submitted code in
and highlight your code accordingly, but my part was to make this version which has only
frontend and basic sqlite data storage.

It's a very small project, which you can run by installing poetry and using the install, then shell commands
```commandline
poetry install --no-root
poetry shell
```
or by using pip
```commandline
pip install -r requirements.txt
```
and then launching code in app.py
```commandline
poetry run python "app.py"
```
or
```commandline
python "app.py"
```


