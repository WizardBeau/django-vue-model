# 前言
该文档主要介绍了django项目的搭建,部署以及部分配置,之后代码的更新说明都会跟此文档同时更新</br>
至于为什么我这么热衷于django？？</br>
作为一个后台框架,它可以将model(模型层),view(视图层)分开</br>
在这个基础上,你可以规划自己项目的url访问路径</br>
相较于传统的各类后台框架,django显得更加轻巧,不会那么傻</br>

# 安装以及初始化
## 安装django
pip install django</br>

## 初始化项目
django-admin startproject model_project</br>

之后就可以在对应目录下看到生成了一个model_project的文件夹</br>
文件夹下有一个和项目同名的文件夹和manage.py的文件</br>
项目的大部分配置都在该同名文件夹中的settings.py中,之后会逐渐拓展</br>
这样子,我们的项目就算是初始化完成了</br>

# 项目启动和django的app
## 项目启动
进入项目文件下在命令行中输入 python manage.py runserver</br>
如果不出意外的话,项目启动之后,你访问http://localhost:8000应该是不会报错的</br>

## app
如何去理解django的app呢？？打个比方,django项目就是一个手机,而app则好比手机中的各个应用软件一个django可以添加多个app</br>
也就是说,一个blog的后台和一个购物网站的后台可以是放在同一个django项目下的两个app</br>
当然你也可以把它们放在同一个app中,但我想这并不利于你的维护工作</br>

## 新建app
在项目目录下,django-admin startapp modelapp</br>
然后你可以在项目目录下看到一个名字为modeleapp的文件夹生成</br>
新建app之后,如果要让它在你的项目中运行,那么就必须到model_project目录下的settings.py文件中的INSTALLED_APPS将它添加进去</br>
具体可以参考settings.py文件,内容已做注释</br>

# 连接和配置数据库
当然,作为一个后台框架,django有自带的本地数据库</br>
然而,作为一个系统后台,我想mysql等数据库可能更适合它</br>
在settings.py文件中已经把配置好了三种数据库,mysql,redis和postgre</br>
OK,当然,django可以同时配置多种数据库</br>
举个例子,用户信息可以放在mysql中,而购物商城的商品信息可以丢在redis里</br>
然而,这并不利于维护</br>
再者,配置mysql数据库时,请留意mysql版本和django的版本,一般而言,5.17的mysql适配的django的版本是2.1.2</br>
否则启动时可能会有报错</br>
当你配置好数据库之后,在命令行中输入 python manage.py makemigrations</br>
然后在输入 python manage.py migrate</br>
执行完之后,你应该会在数据库中看到对应的表格被生成</br>

# django rest-framework
## 简介
OK,作为一个后台框架,基本除了接口还是接口</br>
换言之,接口的规范有利于前端的调用和测试的方便</br>
于是乎,django rest-framework就是为此而存在的</br>

## 安装以及运用
pip install djangorestframework</br>
依赖安装之后,我们需要在settings.py文件中将它添加到INSTALLED_APP中</br>
对于restframework的使用,模板中已经有一个实例</br>
只需要在运行项目之后访问http://localhost:8000/test/get_all_test</br>
当然,对于具体的项目代码撰写,后续我会陆续更新,但现在,你只需要考虑如何能让它运行成功就可以了</br>