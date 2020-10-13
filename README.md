1. Install MySQL on Local
2. Modify src/config.py file with Host Name, User Name, Password and DB Name of mysql
   - SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://password:user_name@host_name/db_name'<br>
   *** It will be needed to add SMTP informations for Sending Email service. ***
   - MAIL_USERNAME : SMTP account email
   - MAIL_PASSWORD : SMTP account password
   - MAIL_RECIPIENTS : Recipients Email
3. Run App
   1) Install Virtualenv and packages from requirements.txt
    - pip install -r requirements.txt
   2) Database Format
    - python manage.py db init
    - python manage.py db migrate
    - python manage.py db upgrade
   3) Run Server
    - python manage.py runserver