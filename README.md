<!--
 * @Author: xioacd99
 * @Date: 2021-07-22 23:46:42
 * @LastEditTime: 2021-07-26 20:40:29
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \.vscode\Github\EnhancedNotePad\README.md
-->

# EnhancedNotePad

## 项目简介

本项目基于算法综合设计课程的一个课设设计扩充而来，提供了处理文本文件的多种功能

## 功能介绍

注：每个功能都有多种算法可供选择，具体可查看 ENotePadAlgorithm 下的具体算法

1. 文本文件批处理（单操作、多操作）[未实现]
2. 字符串计算[未实现]
3. 文本相似性检测[还需要增加一些算法]
4. 单词计数
5. 字符串加密
6. 字符串匹配
7. 文件索引[未实现]
8. 文本文件朗读
9. 字符串语法检查[还需要增加一些算法]
10. 数据压缩

## 环境配置

注：如果不需要使用相关功能，可以不需要安装对应的库

1. pyttsx3, pywin32: 文字转语音库（文本文件朗读）

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

[history error](documents/historyError.md)

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
