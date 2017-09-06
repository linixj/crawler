#!/usr/bin/env python
#coding:utf-8

#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

##通过selenium打开百度
#driver = webdriver.Chrome('/Applications/chromedriver')
#driver.get('http://www.baidu.com/')

##获取浏览器中name为wd的标签
#elem = driver.find_element_by_name("wd")

##search cxy61
#elem.send_keys("cxy61")
#elem.send_keys(Keys.RETURN)

##打印页面
#print driver.page_source

# dr = webdriver.Chrome('/Applications/chromedriver')
# dr.get('https://www.qiushibaike.com/')

##左边编写笑话区域为conten-left
##获取 id 为 content-left的元素
# main_content = dr.find_element_by_id('content-left')

##获取class为content的元素
# contents = main_content.find_elements_by_class_name('content')

## for loop
# for content in contents:
#     print(content.text)

#设置打印内容，使之易于查看
#定义了一个变量i=1，作为每个段子的编号，打印完就+1，\n表示换行
# i=1
# for content in contents:
#     print(str(i)+'.'+content.text+'\n')
#     i+=1
#
# #退出我们打开的浏览器，否则每次都打开一个浏览器，电脑会卡死
# dr.quit()


#Python 是一门面向对象的语言，所以我们能很轻松的创建一个类，类就是描述具有相同属性和方法的对象的集合
#举个例子，就比如老虎、狮子都属于猫科动物，狼、狐狸都属于犬科动物，这个猫科和犬科就好比我们刚刚说的类
# class ClassName(object):
#     """docstring for ClassName"""
#     #def __init__()初始化方法/构造函数，当这个类有实例被创建时，该方法就会被调用
#     #self代表这个类的实例
#     def __init__(self, arg):
#         #super(ClassName, self).__init__()表示调用父类中的方法，本程序中没有涉及到继承，所以先不用
#         super(ClassName, self).__init__()
#         self.arg = arg


#把此类定义为Qiubai,然后定义了print_content和quit两个函数
#最后通过Qiubai().print_content()来调用类中的方法
class Qiubai:
    def __init__(self):
        self.dr = webdriver.Chrome('/Applications/chromedriver')
        self.dr.get('https://www.qiushibaike.com/')

    def print_content(self):
        main_content = self.dr.find_element_by_id('content-left')
        contents = main_content.find_elements_by_class_name('content')

        i = 1
        for content in contents:
            print(str(i) + "." + content.text + '\n')
            i += 1

        self.quit()

    def quit(self):
        self.dr.quit()

Qiubai().print_content()