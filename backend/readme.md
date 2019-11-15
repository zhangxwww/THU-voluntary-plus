# prerequsites
```
pip3 install django-extensions
pip3 install django-werkzeug-debugger-runserver
pip3 install pyOpenSSL
```
```
mysql -u root -p
CREATE DATABASE IF NOT EXISTS THUVPlus;
```

# Start the server
```
sudo python3 manage.py makemigrations
sudo python3 manage.py migrate
sudo python3 manage.py runserver_plus --cert server.crt 0.0.0.0:443
```