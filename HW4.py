#!/usr/bin/env python
# coding: utf-8

# ## 1. 파일

# 실습1) – PPT 자료  
# 파일에 있는 각각의 단어 수 구하기
# 

# In[4]:


f = open("test.txt", "r")
lines = []
for line in f:
    a = line.split()
    lines.append(a)

dict = {}
for c in lines :
    for d in c :
       if d in dict :
          dict[d] += 1
       else :
          dict[d] = 1
print(dict) 
b = list(dict.items())
for ef,ff in b:
    print(ef,ff)

f.close()


# 실습2) – PPT 자료  
# 파일명을 입력 받아, 해당 파일을 한 줄씩 읽어 파일의 내용을 모두 대문자로 출력하는 프로그램을 작성하시오.
# 단, 파일이 없는 경우 “파일이 존재하지 않는다" 정도의 아래 메시지를 출력할 것!

# In[9]:


import os
name = input("Enter a file name: ")
if os.path.exists(name) == True:
    f = open(name, "r")
    data = f.read()
    data = data.upper()
    print(data)
    f.close()
else:
    print("파일이 존재하지 않는다")


# 실습3) 아래의 실행예시처럼 리눅스 쉘에서 원본파일명(src.txt)과 사본파일(dst.txt)을 입력 받아,   
# 복사하는 프로그램을 작성하시오.
# 

# ![%EC%9D%B4%EB%AF%B8%EC%A7%80%20004.png](attachment:%EC%9D%B4%EB%AF%B8%EC%A7%80%20004.png)

# 실습4) 아래의 score.txt를 읽어서 학생들의 성적을 처리하여 그 결과를 report.txt로 출력하는 프로그램을 작성하시오.

# In[36]:


def grade(a,b):
    g = 0.4*a+0.6*b
    if g >= 90:
        return(g,"(A)")
    elif 90 > g >= 80:
        return(g,"(B)")
    elif 80 > g >= 70:
        return(g,"(C)")
    elif 70 > g >= 60:
        return(g,"(D)")
    else:
        return(g,"(F)")


score = open("score.txt", "r")

sc = []
for line in score:
    c = line.split()
    sc.append(c)
    
sd = sc

w = open("report.txt","w")

for i in range(len(sc)):
    mid = int(sc[i][1])
    final = int(sc[i][2])
    g =list(grade(mid,final))
    sd[i].append(g)
for z in range(len(sd)):
    data = ("%s %s %s %s %s\n"%(sd[z][0],sd[z][1],sd[z][2],sd[z][3][0],sd[z][3][1]))
    w.write(data)                                                                
f.close()
w.close()                                                                     
                                                                    



    


# In[ ]:




