# recruitment

### Installing
Before run application

1. Run this command in catalog of your choice: 
```bash
git clone https://github.com/dawiddd95/recruitment.git
```
2. Go to settings.py and configure PostgreSQL database
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'YOUR_DATABASE_NAME', 
        'USER': 'YOUR_POSTGRES_USER', 
        'PASSWORD': 'YOUR_POSTGRES_PASSWORD',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
```
3. Create PostgreSQL database named same as in settings.py
4. Run in your project path
```bash
python manage.py migrate
```

### Running

1. In terminal go to project folder and run command
```bash
python manage.py runserver
```

