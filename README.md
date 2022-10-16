# 知乎爬虫
获取知乎热榜各榜单数据
# 开发者的碎碎念
开始只会解析html，先爬的https://www.zhihu.com/billboard
但是发现这个网页的html不含有链接，就换了https://www.zhihu.com/hot
可是明明print(html)的时候不含有我要的数据，但是用正则表达式又能得到数据，即使现在我也没得到答案，只有零星的猜想。
由于热点分类在这个网页只能点开才能看，我花了很多时间研究如何操作列表来把热点分类和之前的数据连在一起。
这时我很疑惑，题干中说要每个榜单爬100条数据，这个网站却只能得到一百条，无奈先去写了其他的爬虫。
水群时看到任君驰学长发的网站https://www.zhihu.com/creator/hot-question/hot/0/hour
题干要求的所有数据都放在上面，问了一下才知道题干中间更新过。
老实说，我当时有点难受，之前遇到的许多问题在这里都不存在，比如点赞的增量--我一开始是想通过两次数据相减来获得。
不过，我在写这份程序遇到的问题，积累的经验都为我写之后的爬虫提供了便利。
听了任君驰学长的建议，这次我没使用正则表达式，而是使用json来重写程序。
重新学习，重新写程序还是有点爽的，室友都叫我不要发癫。
