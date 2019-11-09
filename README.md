# THU-voluntary-plus
### 接口文档



#### 显示活动列表

* 函数名：catalog_grid

* 参数：request

* 返回数据：{"activity_list":rtn_list}

  rtn_list是Activity类的对象列表

#### 显示活动详情

* 函数名：activity_detail

* 参数：request

* 返回数据：{"activity_detail":Activity_recommend_rtn}

  Activity_recommend_rtn是一个包括Activity类的对象和ActivityPic类的对象的类的对象的列表，包括页面上所有没过期的活动的详细信息，可以通过ActivityNumber属性从返回值中筛选活动

#### 根据关键词搜索活动

* 函数名：search

* 参数：request

* 返货数据：{"search_result":rtn_list}

  rtn_list是一堆结果的列表，每个结果包含一个Acticity类的对象，一个ActivityPic类的对象，一个表示活动日期的字符串

