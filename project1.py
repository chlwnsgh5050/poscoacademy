import func

# f = open("students.txt", "r")
import sys

args = sys.argv[1]
args = str(args)
if args == None:
    f = open("score.txt", "r")
else:
    f = open(args,"r")
lines = []
for line in f:
    line = line.replace('\n','')
    a = line.split('\t')
    lines.append(a)

avg = []
for x in lines:
    a = (int(x[2])+int(x[3]))/2
    avg.append(a)

def gradescore(grade):
    if grade >= 90:
        return "A"
    elif 90 > grade >= 80:
        return "B"
    elif 80 > grade >= 70:
        return "C"
    elif 70 > grade >= 60:
        return "D"
    else:
        return "F"
grade = []
for y in avg:
    grade.append(gradescore(y))
grade

for i in range(len(avg)):
    lines[i].append(avg[i])
 
for i in range(len(grade)):
    lines[i].append(grade[i])  

stu_dict = {}
for i in range(len(lines)):
    stu_dict[lines[i][0]] = lines[i][1],lines[i][2],lines[i][3],lines[i][4], lines[i][5]

sorted_s1 = sorted(stu_dict.items(), key = lambda a:a[1][3], reverse=True)
sorted_s2 = {}
for i in range(len(sorted_s1)):
    sorted_s2[sorted_s1[i][0]] = sorted_s1[i][1][0], sorted_s1[i][1][1], sorted_s1[i][1][2], sorted_s1[i][1][3], sorted_s1[i][1][4]
student = sorted_s2

sorted_stu = sorted(student.items(), key = lambda a:a[1][3], reverse=True)
sorted_stu2 = {}
for i in range(len(sorted_stu)):
    sorted_stu2[sorted_stu[i][0]] = sorted_stu[i][1][0], sorted_stu[i][1][1], sorted_stu[i][1][2], sorted_stu[i][1][3], sorted_stu[i][1][4]
student = sorted_stu2
strFormat = '%-10s%-15s%-10s%-10s%-10s%-10s\n'
strOut = strFormat % ('sep1','sep2','sep3','sep4','sep5','sep6')
title = ['Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade']
print(strFormat %(title[0],title[1],title[2],title[3],title[4],title[5]))
print("=================================================================")


# 딕셔너리 key, value 출력하기(item)
for key, value in student.items():
    # print(key," ", value[0]," ", value[1]," ", value[2]," ", value[3]," ", value[4])
    print(strFormat %(key,value[0],value[1],value[2],value[3],value[4]))

print("학생 성적 관리 프로그램입니다.")

while True:
    print("show, search, changescore, searchgrade, add, remove, quit")
    a = input("# ")
    select = a.lower()
    if select == "show":
        student = func.show(student)
    elif select == "search":
        student = func.search(student)
    elif select == "changescore":
        student = func.changescore(student)
    elif select == "add":
        student = func.add(student)
    elif select == "searchgrade":
        student = func.searchgrade(student)
    elif select == "remove":
        student = func.remove(student)   
    elif select == "quit":
        student = func.quit(student)   
    else:
        pass
        