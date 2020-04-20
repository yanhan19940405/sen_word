# sen_word

##注意##
由于github某些组件最近被墙，导致图片无法正常加载，请按照如下方式处理：

1、更改hosts文件，添加如下信息，刷新网页即可解决此问题：

>> ```
>> 52.74.223.119 github.com
>> 192.30.253.119 gist.github.com
>> 54.169.195.247 api.github.com
>> 185.199.111.153 assets-cdn.github.com
>> 151.101.76.133 raw.githubusercontent.com
>> 151.101.108.133 user-images.githubusercontent.com
>> 151.101.76.133 gist.githubusercontent.com
>> 151.101.76.133 cloud.githubusercontent.com
>> 151.101.76.133 camo.githubusercontent.com
>> 52.74.223.119 github.com
>> 192.30.253.119 gist.github.com
>> 54.169.195.247 api.github.com
>> 185.199.111.153 assets-cdn.github.com
>> 151.101.76.133 raw.githubusercontent.com
>> 151.101.108.133 user-images.githubusercontent.com
>> 151.101.76.133 gist.githubusercontent.com
>> 151.101.76.133 cloud.githubusercontent.com
>> 151.101.76.133 camo.githubusercontent.com
>> ```

2、可以将源码图片文件夹中找到相应图片。

基于trie树的文本关键词提取或者过滤算法

原理将设置的关键词每个字构成相应的trie树。然后设置筛选特征词的长度阈值value，从而将文本中的关键词提取出来。

输入：设置的关键词，关键词长度阈值，待匹配文本

输出：文本中匹配的关键词的列表

运行效果如下：

![图1 demo](https://github.com/yanhan19940405/sen_word/blob/master/image/demo.png)
