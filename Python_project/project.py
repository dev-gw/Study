"""
Author : Gwangwon Kim
Version : 1.1
Score management program
"""

import sys

# 표 헤더 출력함수
def print_up():
    print("  Student       Name       Midterm     Final     Average      Grade")
    print("--------------------------------------------------------------------")
    
# 표 내용 출력함수
def print_bottom(key, value0, value1, value2, value3, value4):
    print(" ", key, "  ", value0, " "*(14 - len(value0)), value1, " "*7, value2, " "*7, value3, " "*7, value4)

# calculate_grade
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
    

# show
def show_function(stu_dict):
    sor_dict = dict(sorted(stu_dict.items(), key=lambda x: x[1][3], reverse=True))
    print_up()
    for key, value in sor_dict.items():
        print_bottom(key, value[0], value[1], value[2], value[3], value[4])
        
# search
def search_function(stu_dict):
    target = input("Student ID: ")
    if target not in stu_dict: # 학번이 없는 경우
        print("NO SUCH PERSON")
    else:
        data = stu_dict[target]
        print_up()
        print_bottom(target, data[0], data[1], data[2], data[3], data[4])

# changescore
def changescore_function(stu_dict):
    target = input("Student ID: ")
    
    if target not in stu_dict:
        print("NO SUCH PERSON") # 학번이 없는 경우
        return
    midorfinal = input("Mid/Final? ")
    if (midorfinal != 'mid') and (midorfinal !=' final'):
        print("Wrong Input : Input 'mid' or 'final'")
        return
    new_score = int(input("Input new score: "))
    if (new_score > 100) or (new_score < 0):
        print("Wrong Score : Input between 0 ~ 100")
        return
    ## 수정 전 출력
    data = stu_dict[target]
    print_up()
    print_bottom(target, data[0], data[1], data[2], data[3], data[4])
    ## 수정 후 출력
    print("Score changed.")
    if midorfinal == 'mid':
        stu_dict[target][1] = new_score
    else:
        stu_dict[target][2] = new_score
    data = stu_dict[target]
    stu_dict[target][3] = (stu_dict[target][1] + stu_dict[target][2]) / 2
    stu_dict[target][4] = calculate_grade(stu_dict[target][3])
    print_bottom(target, data[0], data[1], data[2], data[3], data[4])
    

# add
'''
점수 입력 조건 확인 추가
'''
def add_function(stu_dict):
    target = input("Student ID: ") #있는 학번인 경우
    if target in stu_dict:
        print("ALREADY EXISTS.")
        return
    name = input("Name: ")
    mid = int(input("Midterm Score: "))
    if mid > 100 or mid < 0:
        print("Wrong Score : Input between 0 ~ 100")
        return
    final = int(input("Final Score: "))
    if final > 100 or final < 0:
        print("Wrong Score : Input between 0 ~ 100")
        return
    stu_dict[target] = [name, mid, final, (mid+final)/2, calculate_grade((mid+final)/2)]
    print("Student added.")
    

# searchgrade
def searchgrade_function(stu_dict):
    target_grade = input("Grade to Search: ")
    if target_grade not in ['A', 'B', 'C', 'D', 'F']:
        print("Wrong Input")
        return
    target_list = []
    for x in stu_dict.keys():
        if stu_dict[x][4] == target_grade:
            target_list.append(x)
    if not target_list:
        print("NO RESULTS.")
        return
    print_up()
    for x in target_list:
        data = stu_dict[x]
        print_bottom(x, data[0], data[1], data[2], data[3], data[4])
    

# remove
def remove_function(stu_dict):
    if len(stu_dict) == 0: # 목록이 빈 경우
        print("List is empty.")
        return
    target = input("Student ID: ")
    if target not in stu_dict: # 학생이 목록에 없는 경우
        print("NO SUCH PERSON.")
        return
    del stu_dict[target]
    print("Student removed.")
    

# quit
def quit_function(stu_dict):
    save = input("Save data?[yes/no] ")
    if save == 'yes':
        fname = input("File name: ")
        w = open(fname, 'w')
        sor_dict = dict(sorted(stu_dict.items(), key=lambda x: x[1][3], reverse=True)) # 정렬
        for key, value in sor_dict.items():
            w.write(f'{key}\t{value[0]}\t{value[1]}\t{value[2]}\n')
        w.close()


# main
## 파일명 입력 (디폴트 고민)
if len(sys.argv) == 1:
    fname = "students.txt"
else:
    fname = sys.argv[1]


## 데이터 저장
'''
한줄씩 처리할건지
저장할 자료형 정하기
split - t하고 n
데이터 숫자 문자로 되어있음
'''
r = open(fname, 'r')
stu_dict = {} # 딕셔너리
while True:
    line = r.readline()
    if line == '':
        break
    data = line.strip().split('\t')
    # 평균 및 점수 계산
    average = (int(data[2]) + int(data[3])) / 2
    grade = calculate_grade(average)
    # 데이터 저장(1:이름, 2:중간, 3:기말)
    stu_dict[data[0]] = [data[1], int(data[2]), int(data[3]), average, grade]

## 디폴트 출력
show_function(stu_dict)


## 명령어 입력
'''
대소문자 구분하지 않는 방법 - lower로 통일
'''
while True:
    command = input("# ").lower()
    if command == 'show':
        show_function(stu_dict)
    elif command == 'search':
        search_function(stu_dict)
    elif command == 'changescore':
        changescore_function(stu_dict)
    elif command == 'add':
        add_function(stu_dict)
    elif command == 'searchgrade':
        searchgrade_function(stu_dict)
    elif command == 'remove':
        remove_function(stu_dict)
    elif command == 'quit':
        quit_function(stu_dict)
        r.close()
        break
    else:
        print("Wrong Command!")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        