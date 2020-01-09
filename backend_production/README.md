# 第一次启动
1. docker-compose up --build
2. docker ps
3. docker exec -it [thuvplus-docker_web-container-id] bash -c "cd /code/mysite && python3 manage.py createsuperuser"
```
# 在docker exec之后输入superuser的信息
```
4. docker exec -it [thuvplus-docker_web-container-id] bash -c "mysql -u root -p"
```
# 在docker exec之后输入mysql的root用户的密码
# 输入: 
use THUVPlus;
insert into mysite_useridentity (user_id, isTeacher, setuptime, groupname, email , phone,  about, status, members) VALUES (1,1,  '','','','','',True,'');
exit
```

