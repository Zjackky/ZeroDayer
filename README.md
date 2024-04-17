# ZeroDayer

`ZeroDayer` , 0Day挖掘者,是为了在已有的0day库中快速找到靶标资产来进行打点


## 功能

+ 对单一备案资产进行0day的匹配
+ 对url中的备案资产进行0day的匹配


## 使用方法

### Bash
```bash
python3 ZeroDayer.py -h # 使用帮助
python3 ZeroDayer.py -f Icpnames.txt # 使用文件
python3 ZeroDayer.py -n "北京企业"# 使用单个名字
```

### config.txt
这个文件一般就是从hunter上拉的ICP的集合
```xml
[apache]
广州企业
深圳企业

[nginx]
北京企业
上海企业
```

### Icpnames.txt
这个文件就是拿到靶标信息后进行的整理
```xml
广州企业
深圳企业
北京企业
上海企业
```

### 效果展示

##### 输入名字
![](https://zjacky-blog.oss-cn-beijing.aliyuncs.com/blog/202404172046040.png)

##### 输入文件
![](https://zjacky-blog.oss-cn-beijing.aliyuncs.com/blog/202404172046728.png)

## Tips
+ 本来想用go写的,但是发现压根没必要,而且go可能编译起来还麻烦点(如果您的0day超万个的话当我没说毕竟go自带并发还是舒服点)
+ 您可能会问: "0day在哪呢?" --> "我也不知道我就突发奇想写一下罢了"
+ 开发的根源是因为0day太多不知道用哪个也不知道哪些资产用的上0day于是写了本项目来为各位安全大Die服务下(不是我)

## 彩蛋

+ 最近受某位师傅启发正在开发一个Java Net PHP的代码审计工具，名字都想好了叫 `CodeScan` 简单易懂, 测试阶段让我捡了无数个1/0day 等再测试一段时间就开源咯
