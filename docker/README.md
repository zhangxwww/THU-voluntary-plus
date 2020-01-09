# mysql配置

docker pull mysql/mysql-server:5.7.27

---

# nginx配置

## 拉取镜像
docker pull nginx:1.14.0
## 启动容器
docker run --name webserver -d -p 80:80 nginx
## 使用 docker exec 命令进入容器
docker exec -it webserver bash
```
```
## 保存下来定制的变化形成新镜像。
docker commit \
    --author "Tao Wang <twang2218@gmail.com>" \
    --message "修改了默认网页" \
    webserver \
    nginx:thuvplus
# 运行新镜像

docker run --name web2 -d -p 80:8000 nginx:v2

这里我们命名为新的服务为 web2，并且映射到 81 端口。如果是 Docker Desktop for Mac/Windows 或 Linux 桌面的话，我们就可以直接访问 http://localhost:80 看到结果，其内容应该和之前修改后的 webserver 一样。


# docker-compose up --build -p thuvplus