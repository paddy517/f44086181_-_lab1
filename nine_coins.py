#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random# 匯入random模組

#創立類別
class Nine_Coins:
     #設定初始參數
    def __init__(self,num):
        self.num =  num
        num=format(num,'b') #轉換二進位(轉型成字串)
        z='0'*(9-len(num))#計算需要加上多少個 0
        num=z+num
        num=list(num)#轉型成串列 並把 0 1 轉換 H T 
        for i in range(len(num)):
            if num[i]=='0':
                num[i]='H'
            else:
                num[i]='T'
        num = "".join(num)#將串列轉型為字串
        print(f'Nine_Coins: {num}') 
    
    def __str__(self):
        #以temp暫存，使其在運算時不會影響self.num
        temp=int(self.num)
        temp=format(temp,'b')
        z='0'*(9-len(temp))
        temp=z+temp
        return f'binary:{temp} and decimal: {self.num}'
    
    #設定函式
    def toss(self):
        #隨機賦予新值
        self.num = random.randint(0,512)
        temp=self.num
        temp=format(temp,'b')
        z='0'*(9-len(temp))
        temp=z+temp
        temp=list(temp)
        for i in range(len(temp)):
            if temp[i]=='0':
                temp[i]='H'
            else:
                temp[i]='T'
        temp= "".join(temp)
        print(f'Nine_Coins: {temp}') 

