# VoyagerNotes - (Personal Note-Keeper)
A pretty easy django notes app. Have a note save it!

### Built with :heart: and :coffee: by [`Kaushal Patel`](http://www.kaushalpatel.info)

## Features

- CRUD notes
- Copies selected text automatically
- Easily share
- Download note as PDF
- Beautiful yet simple UI
- Encrypted Data so that no one can phish it! ([using django-cryptography](https://github.com/georgemarshall/django-cryptography))

# Installation

- Clone the repository

```bash
git clone https://github.com/mrkaushal/VoyagerNotes.git
```

- Install Dependencies

```bash
cd VoyagerNotes
pip install -r requirements.txt
```

- Create a file names `.env` in the folder where your `settings.py` file is present. Enter following information in your .env file

```
SECRET_KEY=env('SECRET_KEY')
```

- Run django migrations

```bash
python manage.py migrate
```

- Run django server

```bash
python manage.py runserver
```