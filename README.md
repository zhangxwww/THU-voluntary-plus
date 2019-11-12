# THU-voluntary-plus

## API文档

### 1.活动

#### 1.1 显示活动列表

- 函数名：catalog_grid

- GET /api/activities/list

- 参数：无

- 返回值：

  ```json
  {
  	"activity_list":{
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
      }
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

  ```json
  {
  	"search_result":{
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
      }
  }
  ```

  
