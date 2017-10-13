# FirPortal #

## Setup Instructions ##
Follow these instructions
```
git clone https://github.com/sairamkolla/FirPortal.git
cd FirPortal
python manage.py migrate
python manage.py runserver
```
visit [127.0.0.1:8000](127.0.0.1:8000) to launch the web application.
## About the project ##
This is a web application made in django and angular js which enables users to register complaints anonymously. The application has 2 views.

- **Submit an FIR** : In this view, the user can register a complaint with all the relevant details
- **View reports** : In this view the admin can view the complaints registered between 2 time frames.

