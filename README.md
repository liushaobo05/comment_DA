#### 说明
该项目主要用来爬取淘宝网的评论内容，然后通过分词，统计出高频词汇，客观的反应了客户的需求情况

#### 目录结构
```
├── README.md
├── inputData          // 数据输入
│   └── inputData.txt
├── outputData         // 数据输出
│   ├── getData.txt    // 爬取的数据，用于和最终的统计数据做验证
│   └── outputData.txt // 最终统计数据
├── requirements.txt   // python 安装包
└── taobaoDa.py        // 程序代码
```

#### 用法
- 1. 打开淘宝商品链接
- 2. 开发工具中网络中选中js，显示在js中找到请求链接
https://rate.tmall.com/list_detail_rate.htm
- 3. 赋值
数据的入口文件中，按照demo的格式，写入要爬取的链接
https://rate.tmall.com/list_detail_rate.htm?itemId=532496031656&spuId=575420997&sellerId=2424477833&order=3&callback=jsonp3196
