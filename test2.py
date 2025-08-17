"""
#conda command
conda env list
conda create -n myenv python=3.12
conda activate myenv
conda deactivate 

#python command or skills
print("hello, world")
数据类型：整型，字符串，浮点型
数据结构：list，dict, tuple
常用函数:print(), type(), range(1, 100, 1) 1是起点，100是终点， 1是步长
常用语法: if else条件判断, elif, for循环
python的一个习惯：包头不包尾
常用的库：numpy： slice(切片)
如何自定义一个函数：sin(). cos(), print()； pdb.set_trace()
数学运算
概念：常量，变量

pdb.set_trace() # l (list); n (next)执行下一行代码; s(setp into) 进入函数; 
c(continue) 执行的下一个断点; p (print); b 行号，添加断点

#Linux command
ls or ls -l ----list
cd folder_name ---enter folder
cd ~ ---enter user root folder
cd / ----enter system root folder
cd .. ----enter previous folder
cd - ----enter last folder
cat file_name ----print file content to terminal
mkdir folder_name ----create folder
touch file_name ----create file
pwd ----print current path (print work directory)


#github, numpy, pdb.set_trace, os, define function
"""

import pdb

print(12.0*12)
print('hello, world' + ' 1234')

my_list = [1, 2, 3, 4]
my_list = [100, 200] #my_list是一个变量，100， 200是一个常量
print(my_list)
#print(type(my_dict))

#遍历
for element in my_list:
    print(element)

#包头不包尾
sum = 0
for i in range(1, 101): # range(1, 101)
    print('i =', i)
    sum = sum + i
print(sum)
# print(range(1, 101))

def cal_sum_of_continours_numbers(begin_number, end_number):

    pdb.set_trace()

    sum = 0
    for i in range(begin_number, end_number):
        sum = sum + i
    return sum


pdb.set_trace() # l (list); n (next); s(setp into); c(continue); p (print)
result = cal_sum_of_continours_numbers(1, 101) #sum :1 to 100
print(result)


score = 90
if score < 60:
    print('fail')
elif score >= 60 and score < 90:
    print('good')
else: # score >= 90
    print('excellent')

product = 1
for i in range(1, 4):
    print('i =', i)
    product = product * i
print(product)