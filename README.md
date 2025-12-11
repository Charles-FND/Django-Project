# WebStore Django Example

This project demonstrates a minimal Django app that uses a custom management command to populate sample `Post` data into a MySQL database and displays posts in a responsive Bootstrap UI.

## Requirements
- Python 3.10+
- MySQL server running with a database named `storedb`
- The DB user configured in `webstore/settings.py` (defaults to `root` / `Charles@90250`)

## Setup

1. Create virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Ensure MySQL database `storedb` exists and credentials in `webstore/settings.py` are correct.

3. Run migrations:

```powershell
python manage.py migrate
```

4. Populate sample posts:

```powershell
python manage.py populate_posts
```

5. Run the dev server:

```powershell
python manage.py runserver
```

Open `http://127.0.0.1:8000/` to view the posts.

Notes:
- On Windows, installing `mysqlclient` may require Visual C++ Build Tools or using `pip install mysqlclient‑<version>‑cpXX‑win_amd64.whl` from Christoph Gohlke's wheels.
- For production, update `SECRET_KEY`, set `DEBUG=False`, and configure allowed hosts and static files.
