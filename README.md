<!--
 * @Author: xioacd99
 * @Date: 2021-07-22 23:46:42
 * @LastEditTime: 2021-07-29 15:43:20
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \.vscode\Github\EnhancedNotePad\README.md
-->

# EnhancedNotePad

## 项目简介

本项目基于算法综合设计课程的一个课设设计扩充而来，提供了处理文本文件的多种功能

## 功能介绍

注：每个功能都有多种算法可供选择，具体可查看 ENotePadAlgorithm 下的具体算法

1. 单文件多操作处理
2. 文本相似性检测
3. 单词计数
4. 字符串加密
5. 字符串匹配
6. 文本文件朗读
7. 字符串语法检查
8.  数据压缩

## 环境配置

注：如果不需要使用相关功能，可以不需要安装对应的库

1. pyttsx3, pywin32: 文字转语音库（文本文件朗读）
2. PyQt5，pyQtWebEngine：图形库
3. imageio：存取图片，图片解析操作（词云图）
4. jieba：分词库（词云图）
5. qtawesome：图标库
6. wordcloud：词云图处理
7. docx，docxcompose：python-word
8. MyQR：QR处理库（url转二维码）
9. requests：处理、解析请求（爬虫爬取对应图片）

## 如何参与项目？

### 提建议

Issues 部分新建一个 Issue，填写对应的标题、描述、Labels、（Assignees）

### 完善文档

#### 规范

1. 所有文档使用 markdown 编写，放在 documents 文件夹下，文档中引用的图片放在 image 文件夹下（相对路径）。

#### 流程

将项目 clone 到本地进行修改，pull 时选择 pull merge 而不是直接 commit to master。您的贡献将经过审核判断是否接受。

### 贡献代码

#### 规范

代码格式细节不做要求，如 if else 是否换行等。下面所说的是**使用 PyCharm ctrl + alt + L 格式化代码后**需要注意的

1. 每一个算法都单独写成一个类，成员函数的命名不需要再包含类的名字，如
   ```python
   class KMP:
      ...
      def strSearch:
         ...
      def filesearch:
         ...
      ...
   ```
2. 写好的类文件放到对应的文件夹下，如`KMP字符串匹配`算法我们放在了`ENotePadAlgorithm/strFind`文件夹下（这里你也可以看出，如果你扩展的算法不再这些文件夹的范围内，你可以按照`typeOperation`的格式新建文件夹，如`imgGenerate、videoEncode`等）
3. 当你写好一个算法后，你需要在对应的 test 文件夹下加上对应算法的测试文件
4. 使用单一驼峰命名法，但是类名和算法文件名首字母可以大写，举例如

   正确的：BruteFoce.py, insert, badCharOffset

   错误的：BF_word_count.py, Insert, BadCharOffset

5. 每个函数和类都需要添加相应的注释（`vscode koroFileHeader`插件可以帮助你更快地写好注释）
   ```python
   # 这是这个插件利用 ctrl + alt + t 快捷键生成的函数注释
   /**
    * @description:
    * @param {*}
    * @return {*}
    */
   ```
6. 确保你提交的每一个版本都是完全的，不要提交半成品算法

#### 流程

将项目 clone 到本地进行修改，pull 时选择 pull merge 而不是直接 commit to master。您的贡献将经过审核判断是否接受。

## 历史 Error

### 字符串匹配

1. 简单的匹配算法只能做到非全字匹配，全字匹配还要考虑单行没有统计完的情况，如being be

## 更新日志

1. 2021/07/23
   1. 需求分析，项目搭建，明确分工
   2. 实现 BF 字符串匹配、KMP 字符串匹配
   3. 实现 BF 计数、BST 计数、Trie 计数、hashTable 计数
2. 2021/07/24
   1. 实现 BM 字符串匹配、Sunday 字符串匹配
   2. 项目文件结构更改
   3. Ui 基本框架
3. 2021/07/25
   1. 实现 10 种加密算法
   2. 实现几种字符串距离度量函数
   3. 文本相似性算法设计
4. 2021/07/26
   1. 实现 8 种数据压缩算法
   2. 添加 5 种字符串匹配算法
   3. 实现括号匹配
   4. 实现语音朗读
   5. 实现基于树的文本相似性算法
   6. 实现code IDE自动补全和在线编译
5. 2021/07/27
   1. 实现几个功能
6. 2021/07/28
   1. 底层算法优化
7. 2021/07/29
   1. 代码重构
