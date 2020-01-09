# 第一次启动
1. docker-compose up --build -d
2. docker ps
3. docker exec -it [thuvplus-docker_web-container-id] bash -c "cd /code/mysite && python3 manage.py createsuperuser"
```
# 在docker exec之后输入superuser的信息 # 为了单元测试，第一个用户的名称和密码都是tester
```
4. docker exec -it [mysql/mysql-server:5.7.27-container-id] bash -c "mysql -u root -p"
```
# 在docker exec之后输入mysql的root用户的密码("123")
# 输入: 
use THUVPlus;
insert into mysite_useridentity (user_id, isTeacher, setuptime, groupname, email , phone,  about, status, members) VALUES (1,1,  '','','','','',True,'[]');
exit
```

