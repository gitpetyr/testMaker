# 移除元素

## 题目描述

$chuck$ 有一个长度为 $n$ 的数组，可以对数组进行如下操作：
- 每次选取数组中两个相等的数，然后把这两个数移除掉。
- 每次选取数组中三个相等的数，然后把这三个数移除掉。

$chuck$ 想知道最少多少次操作可以把整个数组都清空?

## 输入格式

第一行一个正整数 $n$ ，表示数组的长度。

第二行 $n$ 个整数 $a_i$ ，表示数组中的元素。

## 输出格式

一个整数，最少的操作次数，如果不能使得数组为空，则输出 $-1$ 。

## 样例 #1

### 样例输入 #1

```
4
25 1 909167 25
```

### 样例输出 #1

```
-1
```

## 样例 #2

### 样例输入 #2

```
5
3 2 2 3 3
```

### 样例输出 #2

```
2
```

## 样例 #3

### 样例输入 #3

```
5
2 2 2 2 2
```

### 样例输出 #3

```
2
```

## 提示

$1<=n<=10^5$

$1<=a_i<=10^6$
