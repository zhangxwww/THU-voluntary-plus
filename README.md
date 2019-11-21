# THU-voluntary-plus

## API文档

### 1.活动

#### 1.1 显示活动列表

* 函数名：catalog_grid

- GET /api/activities/list

- 参数：无

- 返回值：

  ```json5
  {
  	"activity_list":[
          {
              "id":id(char)
              "name":name(char)
              "date":date(char)
              "pic":ActivityPic对象
          },
  		    {
              "id":id(char)
              "name":name(char)
              "date":date(char)
              "pic":ActivityPic对象
          },
  		...
      ]
  }
  ```

#### 1.2 显示活动详情

- 函数名：activity_detail

- GET /api/activities/detail

- 参数：activity_id(char)

- 返回值：

  ```json
  {
      "activity_detail":Recommend(activity,pic)
  }
  ```

  activity是Activity类的对象，pic是ActivityPic类的对象

#### 根据关键词搜索活动

- 函数名：search

- GET /api/activities/search

- 参数：无

- 返回值：

  ```json5
  {
  	"search_result":[
          {
              "id":id(char)
              "name":name(char)
              "date":date(char)
              "pic":ActivityPic对象
          },
  		  {
              "id":id(char)
              "name":name(char)
              "date":date(char)
              "pic":ActivityPic对象
          },
  		...
      ]
  }
  ```

### 2.消息

#### 2.1 显示消息列表

- 函数名：message_catalog_grid

- GET /api/messages/list

- 参数：无

- 返回值：

  ```json5
  {
  	"message_list":[
          {
              "ReadOrNot":ReadOrNot(int)
              "Title":Title(char)
              "BriefContent":content(char)
          },
  		  {
             "ReadOrNot":ReadOrNot(int)
              "Title":Title(char)
              "BriefContent":BriefContent(char)
          },
  		...
     ]
  }
  ```

#### 2.2 显示消息详情

- 函数名：activity_detail

- GET /api/messages/detail

- 参数：message_id(char)

- 返回值：

  ```json5
  {
  	  "message_detail":{       
          "ReadOrNot":ReadOrNot(int)
          "Title":Title(char)
          "DetailContent":DetailContent(char)
      }
  }
  ```
