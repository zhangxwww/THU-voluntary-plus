# prerequsites
```
pip3 install django-extensions
pip3 install django-werkzeug-debugger-runserver
pip3 install pyOpenSSL
```
```
mysql -u root -p
#drop database THUVPlus;
CREATE DATABASE IF NOT EXISTS THUVPlus;
exit
```
```
python3 manage.py makemigrations
python3 manage.py makemigrations mysite
python3 manage.py makemigrations showactivity
python3 manage.py migrate
```

---

# HTTPS配置
目前的证书放在了/etc/letsencrypt/live/thuvplus.iterator-traits.com/fullchain.pem和/etc/letsencrypt/live/thuvplus.iterator-traits.com/privkey.pem，如果我没弄错有效期是三个月。。。基于letsencrypt和certbot，**请勿修改这两个文件**

---

# Start the server

<font color=#0099ff>下面的配置都是默认django项目放在了/home/ubuntu/jxq_tmp/THU-voluntary-plus/backend/mysite/目录下，如果项目不是放在这个目录，需要修改这些命令和mysite_nginx.conf里的一些和项目目录相关的配置</font>

#### 步骤一（第一次启动时运行，之后正常情况下不用手动执行）
```
sudo ln -s /home/ubuntu/jxq_tmp/THU-voluntary-plus/backend/mysite/mysite_nginx.conf /etc/nginx/sites-enabled/
sudo service nginx start
```

#### 步骤二（第一次启动时运行，之后正常情况下不用手动执行）
<font color=#0099ff>启动uwsgi时不要使用sudo或root身份操作，否则可能会引发502 Bad Gateway的错误</font>
```
cd /home/ubuntu/jxq_tmp/THU-voluntary-plus/backend/mysite
uwsgi --socket mysite.sock --wsgi-file mysite/wsgi.py
```

---
 
# 创建志愿老师账号

```
insert into mysite_useridentity (user_id, isTeacher, setuptime, groupname, email , phone, membersname, subjects, about, status) VALUES (1, True,'', '','','','','','',True);
```
