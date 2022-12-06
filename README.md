# Python Crash Course --- Learning Notes

some shortcuts for terminal typing

|keys|do|
|:-:|:-|
|CTRL K|cut from cursor to end of line|
|CTRL U|cut from cursor to head of line|
|ALT D|cut from cursor to end of word|
|CTRL Y|paste |

---

11/24/2022 11:42pm 复制列表 :)

----

11/25/2022 9:13pm 字典 :)

MOJITO:<br/>

50 ML BACARDÍ CARTA BLANCA RUM<br/>
25 ML LIME JUICE<br/>
12 MINT LEAVES<br/>
2 TSP EXTRA FINE SUGAR<br/>
25 ML SODA WATER<br/>
1 SPRIG OF FRESH MINT<br/>

---

1/12/2022 1:12pm 函数 ：）

2/12/2022 2:44pm 文件与错误处理 ：）


## list, tuple, set, and dictionary

- list is as its name idicated, a list of values
- tuple is similar to list, but its value is not mutatable, you can re-assign the whole tuple
- set is a list with no duplication in values
- dictionary is a "list" of key: value pairs

|syntax|value|notice|
|:-:|:-|:-|
|a = [1,2,3,4,5,6]|1,2,3,4,5,6|| 
|b = (1,2,3,4,5,6)|1,2,3,4,5,6|element inside tuple is not mutatable, but you can re-assign whole tuple| 
|c = {1,1,2,2,3,3,4,4,5,5,6,6}|1,2,3,4,5,6|no duplications of elements inside a set| 
|d = {"a":1, "b":2, "c":3}|"a":1, "b":2, "c":3|use dict.items(), keys(), values() method for loops|

 
### 12.3.1 创建Pygame窗口，响应用户输入。


Sun 04 Dec 2022 04:38:56 PM CST

you can insert date time in Vi by `:r !date`


you can add a shebang line to .py files to excute them in a easier way

```shell
#! /usr/bin/env python3
```
grant permession and run
```shell
sudo chmod 744 hello.py
./hello.py
```
