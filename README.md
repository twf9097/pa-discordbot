# pa-discordbot

hi

# Development setup
just uhhh
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

for windows it's pretty much the same, just
```
python3 -m venv venv
.\env\Scripts\activate
pip install -r requirements.txt
```

make the database
```
PYTHONPATH=. alembic upgrade head
```

then set the token
```
export PA_DISCORD_TOKEN="blah blah your token lol"
python start.py
```
it is different on windows but i am not going to tell you how to do it :)
