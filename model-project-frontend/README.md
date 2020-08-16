# 初始化vue项目和启动

## 初始化
vue init webpack model-project-frontend</br>
然后, 你只需要一直回车, 一些基础的项目设置之后等待项目创建完成</br>

## 项目启动
npm run dev</br>
当命令行出现Complied successfully的字眼就说明成功了</br>
此时， 你可以尝试访问'http://localhost:8080'</br>

# vuetify

OK, vuetify是个什么东西？？？</br>
vuetify于vue, 就好比bootstrap于html的意义</br>
vuetify已经定义好各种样式供你在使用vue时进行选择</br>

## 关于vue的一些小问题
如果你开始使用vue</br>
那么我必须告诉你</br>
它很"麻烦"</br>
因为它代码规范很多</br>
例如[]中的最后一个{}或者最后一项后面并不需要逗号</br>
例如每个文件的最后一行代码之后都必须有敲一下回车键</br>
又例如.vue文件中<template>和</script>之间一定要空一行</br>
是的, 它就是这么一个磨人的小妖精</br>
如果你不遵守以上这些代码规范</br>
当你启动项目的时候, 就会有一堆的报错</br>
当然这些只是部分规范</br>
可这并不是坏处</br>
整齐简介的代码有利于身心愉悦</br>
哦对了, vue和python不太一样</br>
python的缩进是4个空格而vue的缩进是两个空格</br>
记得在编辑器中做好设置</br>

## 如何在vue中配置vuetify

### 安装
在项目目录下安装vuetify</br>
npm install vuetify</br>
你以为这样子就可以了？？？</br>
答案是不可能的</br>
还需要安装其他的依赖</br>
npm install sass sass-loader fibers deepmerge -D</br>

### 配置
你只需要在项目目录下的build文件夹中找到webpack.base.conf.js文件</br>
然后在module下的rules添加配置, 具体配置请参考模板相对应的文件</br>

### 创建插件文件
对于vuetify的使用, 可能会有教程告诉你直接在main.js文件下导入即可</br>
但我仍建议给vuetify单独建一个文件</br>
具体操作: </br>
在src下新建一个plugins的文件夹然后创建一个vuetify.js的文件</br>
具体代码请参考对应目录下的文件</br>
然后在src/main.js中将vuetify实例化</br>

## babel-polyfill
为了确保兼容性, 你必须使用babel-polyfill</br>
当然也很简单</br>
npm install babel-polyfill --save</br>
然后在src/main.js中</br>
import 'babel-polyfill'

## mdi/font
vuetify中有许多图标</br>
要使用它们并不难</br>
安装依赖 </br>
npm install @mdi/font -D</br>
然后在src/main.js中将其导入</br>
import '@mdi/font/css/materialdesignicons.css'</br>

## axios和vue-axios
axios其实就是js里面的ajax</br>
怎么使用嘛</br>
安装两个依赖</br>
npm install axios</br>
npm install vue-axios</br>
至于在哪里使用它们？？？</br>
参考http.js文件

## http.js
这是一个前后端分离的项目</br>
所以我想, 其实你并不想在发送ajax请求的时候写上那么一长串的后台接口url</br>
这个时候, http.js的意义就体现出来了</br>
具体代码请参考http.js</br>

## 后话
到这里为止, 其实这个项目就是一个空壳</br>
具体的使用, 可以自行查找官网或者等我更新</br>