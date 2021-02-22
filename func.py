f = open("students.txt", "r")
lines = []
for line in f:
    line = line.replace('\n','')
    a = line.split('\t')
    lines.append(a)

avg = []
for x in lines:
    a = round((int(x[2])+int(x[3]))/2,1)
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



def show(student):
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
    
    return student

def search(sorted_s2):
    search_num = input('Stude ID : ')
    
    # 검색한 이름이 딕셔너리내의 Key값과 일치하는 경우
    if(search_num in student) == True:
        strFormat = '%-10s%-15s%-10s%-10s%-10s%-10s\n'
        strOut = strFormat % ('sep1','sep2','sep3','sep4','sep5','sep6')
        title = ['Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade']
        search_value = student.get(search_num)
        print(strFormat %(title[0],title[1],title[2],title[3],title[4],title[5]))
        print("===============================================================")
        # print(search_num, sorted_s2.get(search_num)[0],' ')
        print(strFormat %(search_num,search_value[0],search_value[1],search_value[2],search_value[3],search_value[4]))                   # 딕셔너리에서 키의 값을 가져옴 => dic.get(key)
        

    else:
        print('NO SUCH PERSON')
        # num = int(input('번호 입력 : '))
        # if num ==1:
        #     Search(student)
        # else:
        #     main()

    return student

# ----- 성적 수정 -----
def changescore(student):
    update_num = input('Student ID: ')
    strFormat = '%-10s%-15s%-10s%-10s%-10s%-10s\n'
    strOut = strFormat % ('sep1','sep2','sep3','sep4','sep5','sep6')
    title = ['Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade']
    search_value = student.get(update_num)

    # 검색한 이름이 딕셔너리내의 Key값과 일치하는 경우
    if(update_num in student) == True:
        test_type = input('Mid or Final: ')
        if test_type == 'mid':
            newscore_mid = int(input('Input new score: ') )
            if 100 >= newscore_mid >= 0:
                print(strFormat %(title[0],title[1],title[2],title[3],title[4],title[5]))
                print("===============================================================")
                print(strFormat %(update_num,search_value[0],search_value[1],search_value[2],search_value[3],search_value[4]))
                print("Score changed")
                stu_update_mid = list(student[update_num])
                stu_update_mid[1] = newscore_mid
                stu_update_mid_avg = round(int((stu_update_mid[1]) + int(stu_update_mid[2]))/2, 1)
                stu_update_mid[3] = stu_update_mid_avg
                stu_update_mid[4] = gradescore(stu_update_mid[3])
                student[update_num] = stu_update_mid
                print(strFormat %(update_num,student[update_num][0],student[update_num][1],student[update_num][2],student[update_num][3],student[update_num][4]))
            else:
                changescore(student)

                

        elif test_type == 'final':
            newscore_final = int(input('Input new score: ') )
            if 100 >= newscore_final >= 0:
                print(strFormat %(title[0],title[1],title[2],title[3],title[4],title[5]))
                print("===============================================================")
                print(strFormat %(update_num,search_value[0],search_value[1],search_value[2],search_value[3],search_value[4]))
                print("Score changed")
                stu_update_final = list(student[update_num])
                stu_update_final[1] = newscore_final
                stu_update_final_avg = round(int((stu_update_final[1]) + int(stu_update_final[2]))/2, 1)
                stu_update_final[3] = stu_update_final_avg
                stu_update_final[4] = gradescore(stu_update_final[3])
                student[update_num] = stu_update_final
                print(strFormat %(update_num,student[update_num][0],student[update_num][1],student[update_num][2],student[update_num][3],student[update_num][4]))
        
        else:
            changescore(student)
                   
            
            
            
            # print('국어 영어 수학 성적 입력 :')

            # #국, 영, 수 성적 입력(덮어씀)
            # kor, eng, math = map(int, input().split())

            # score = kor+eng+math
            # avg = round(score/3, 1)

            # #딕셔너리내의 Key = Value
            # student[update_name] = [kor, eng, math, score, avg]
            # person = student[update_name]

    else:
        print('NO SUCH PERSON')
        changescore(student)
        # num = int(input('번호 입력 : '))
        # if num ==1:
        #     Update(student)
        # else:
        #     main()

    return student

# ----- 성적 추가 -----
def add(student):
    add_num = input('Student ID: ')
    if (add_num in student) == True:
        print("ALREADY EXISTS.")
    else:
        add_name = input('Name: ')
        add_mid = int(input('Midterm Score: '))
        add_final = int(input('Final Score: '))
        add_avg = round((add_mid+add_final)/2,1)
        add_grade = gradescore(add_avg)
        student[add_num] = add_name, add_mid, add_final, add_avg, add_grade
        print("Student ADDED.")
    
    return student
# ----- Grade 검색 -----
def searchgrade(student):
    search_grade = input('Grade to search: ')
    search_grade = search_grade.upper()
    if search_grade == 'A' or 'B' or 'C' or 'D' or 'F':
        gradelist = []
        for i in range(len(student)):
            if search_grade in list(list(student.values())[i])[4]:
                gradelist.append(list(student)[i])
            else:
                continue
        if gradelist == []:
            print("NO RESULTS.")
        else:
            strFormat = '%-10s%-15s%-10s%-10s%-10s%-10s\n'
            strOut = strFormat % ('sep1','sep2','sep3','sep4','sep5','sep6')
            title = ['Student', 'Name', 'Midterm', 'Final', 'Average', 'Grade']
            print(strFormat %(title[0],title[1],title[2],title[3],title[4],title[5]))
            print("===============================================================")
            gradelist_dict = {}
            for s in gradelist:
                s_value = student.get(s)
                gradelist_dict[s] = s_value[0],s_value[1],s_value[2],s_value[3],s_value[4]
            gradelist_dict_sorted = sorted(gradelist_dict.items(), key = lambda a: a[1][3], reverse=True)
            gradelist_dict_sorted2 = {}
            for i in range(len(gradelist_dict_sorted)):
                gradelist_dict_sorted2[gradelist_dict_sorted[i][0]] = gradelist_dict_sorted[i][1][0], gradelist_dict_sorted[i][1][1], gradelist_dict_sorted[i][1][2], gradelist_dict_sorted[i][1][3], gradelist_dict_sorted[i][1][4]
            student1 = gradelist_dict_sorted2
            for key, value in student1.items():
                print(strFormat %(key,value[0],value[1],value[2],value[3],value[4]))
    
    else:
        pass
        
    return student

# ----- 학생 삭제 -----
def remove(student):
    if student == {}:
        print("List is empty.")
    else:
        remove_id = input('Student ID: ')
        if (remove_id in student) == True:
            del student[remove_id]
            print("Student removed.")
        else:
            print("NO SUCH PERSON")
    
    return student


def quit(student):
    savedata = input("Save data?[yes/no] ")
    if savedata == 'yes':
        filename = input("File name: ")
        newfile = open(filename, 'w')
        a = list(student.items())
        for i in range(len(student)):
            data = "%s\t%s\t%s\t%s\n"% (a[i][0],a[i][1][0], a[i][1][1], a[i][1][2])
            newfile.write(data)
        newfile.close()
    
    return student


