# Blog App

A Blogging App for posting and sharing ideas.

## Built with :

- Django 3
- Sqlite3
- HTML, CSS, Materialize

## Installation :

1. Clone the Repository
2. Install required packages :
   ```bash
   pip install requirements.txt
   ```
3. Add SECRET_KEY to .env file in Blogproject directory.

## Run the Server :

1. Navigate to the directory of blogproject.
2. Execute :
   ```python
   python manage.py runserver
   ```

## Functionalities added :

- Posts can be added anonymously or as a logged in User.
- For logged in users, edit or delete blogs can be done.
- Users can view, delete or update their accounts.
- Users can track their posts and comments seperately.
- Comments can be posted anonymously or as logged in user.
- Details of all posts can be read via API.

## Project Structure :

Blogproject Project contains 3 Apps in it.

1. app - Main app from where Blogs are rendered
2. usermanage - app to handle Users.
3. api - app to render API for the project.
