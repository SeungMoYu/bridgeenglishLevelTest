# ★★꼭 읽어주세요★★
# 학생 처음 올 때 시험치는 레벨 테스트 채점 프로그램입니다.
# 혹시나 시험지가 바뀐다면 각각의 answers(ex. Vanswers, Ganswers, Ranswers)의 정답들을 고쳐주시면 됩니다.
# 단 항상 형식은 ["(정답)", . . . , "(정답)"] 을 지켜주셔야 됩니다.
# 빨간색 글씨는 주석이니 건드리셔도 상관없습니다.
# 비전공자도 알아보기, 찾기 쉽게 주석을 많이 적어놨으니 활용해 주시면 되겠습니다!

def test1():#■■■■■■■■■ Test1■■■■■■■■■■
    print("")
    print("Test1은 직접 매기는게 빨라요!")
    end = input("종료하시려면 enter를 눌러주세요 :)")

#def = define. 함수 정의 명령어입니다

def test2():#■■■■■■■■■ Test2■■■■■■■■■■
    print("테스트2 채점 프로그램")
    print("정답만 입력하시면 됩니다.")
    print("혹시나 학생이 정답을 못 적었다면 1 ~ 5를 제외한 다른 숫자를 하나 적어주세요!\n")
    print("")
    print("test2 서술형 문제 정답")
    print("8번 (1) My name is Amy.  (2) 문장의 시작과 사람이름은 대문자\n10번 b-c-a           | 13번 who/my\n16번 under           | 18번 지우개/자\n19번 You're welcome. | 20번 I am busy\n29번 What a nice boy!")
    print("서술형 정답이 맞을 경우 소문자로 o, 틀릴 경우 x를 입력하세요.\n")
    answers = ["4", "1", "2", "5", "3", "2", "4", "o", "3", "o", "3", "1", "o", "5", "3", "o", "2", "o", "o", "o", "5", "4", "4", "2", "1", "4", "2", "5", "o", "3"]
    score3 = ['4','5','9','10','12','24']
    score4 = ['8','17','18','21','22','23','25','26']
    score5 = ['19','20','27','28','29','30']
    
    inputA = input("정답 입력 : ")
    pa = list(str(inputA))
    waL = []
    score = 100

    while len(answers) != len(pa):
        pa.clear()
        print("정답 개수가 다릅니다. 다시 입력해주세요.")
        inputA = input("정답 입력 : ")
        pa = list(str(inputA))

    for i in range(30):
        if str(answers[i]) != str(pa[i]):
            waL.append(i+1)
            
    for i in range(len(waL)):
        if str(waL[i]) in score3:
            score -= 3
        elif str(waL[i]) in score4:
            score -= 4
        elif str(waL[i]) in score5:
            score -= 5
        else:
            score -=2

    print("점수 : ", score)
    print("틀린 문제 : ",waL)
    end = input("종료하시려면 enter를 눌러주세요 :)")


def test3():#■■■■■■■■■ Test3■■■■■■■■■■
    print("")
    print("테스트3 채점 프로그램")
    print("정답만 입력하시면 됩니다.")
    print("혹시나 학생이 정답을 못 적었다면 1 ~ 5를 제외한 다른 숫자를 하나 적어주세요!\n")
#-------------------- Vcabulary start----------------------------------
    print("Vocabulary")
    Vanswers = ["2", "4", "5", "4", "3", "4", "2", "1", "4", "3", "2", "2", "4", "2", "2", "4", "2", "3", "2", "3", "3", "2", "2", "5", "1", "2", "5", "4", "2", "1"]
    VinputA = input("정답 입력 : ")
    Vpa = list(str(VinputA))
    Vwa=0           #틀린문제 개수
    VwaL=[]         #틀린문제 번호
    Vscore = 100    #총점

    while len(Vanswers) != len(Vpa):
        Vpa.clear()
        print("정답 개수가 다릅니다. 다시 입력해주세요.")
        VinputA = input("정답 입력 : ")
        Vpa = list(str(VinputA))

    for i in range(30):
        if int(Vanswers[i]) != int(Vpa[i]):
            Vwa += 1
            VwaL.append(i+1)    #틀린문제 카운트&번호

    for i in range(len(VwaL)):
        if VwaL[i] < 11:
            Vscore -=2
        elif 10 < VwaL[i] <19:
            Vscore -=3
        elif 18 < VwaL[i] <27:
            Vscore -=4
        else:
            Vscore -=6
            
#-------------------- Vacabulary end----------------------------------
#-------------------- Grammer start----------------------------------

    print("Grammer")
    Ganswers = ["5", "2", "3", "5", "2", "4", "1", "5", "4", "3", "2", "1", "3", "5", "5", "3", "2", "5", "2", "3"]
    GinputA = input("정답 입력 : ")
    Gpa = list(str(GinputA))

    Gwa=0           #틀린문제 개수
    GwaL=[]         #틀린문제 번호
    Gscore = 100    #총점

    while len(Ganswers) != len(Gpa):
        Gpa.clear()
        print("정답 개수가 다릅니다. 다시 입력해주세요.")
        GinputA = input("정답 입력 : ")
        Gpa = list(str(GinputA))

    for i in range(20):
        if int(Ganswers[i]) != int(Gpa[i]):
            Gwa += 1
            GwaL.append(i+1)    #틀린문제 카운트&번호

    for i in range(len(GwaL)):
        if GwaL[i] < 7:
            Gscore -=4
        elif 6 < GwaL[i] <15:
            Gscore -=5
        else:
            Gscore -=6

#-------------------- Grammer end----------------------------------
#-------------------- Reading start--------------------------------

    print("Reading")

    Ranswers = ["2", "3", "1", "1", "5", "2", "1", "3", "2", "4", "2", "3", "3", "4", "5", "3", "4", "4", "1", "1"]
    RinputA = input("정답 입력 : ")
    Rpa = list(str(RinputA))

    Rwa=0           #틀린문제 개수
    RwaL=[]         #틀린문제 번호
    Rscore = 100.0    #총점
    while len(Ranswers) != len(Rpa):
        Rpa.clear()
        print("정답 개수가 다릅니다. 다시 입력해주세요.")
        RinputA = input("정답 입력 : ")
        Rpa = list(str(RinputA))

    for i in range(20):
        if int(Ranswers[i]) != int(Rpa[i]):
            Rwa += 1
            RwaL.append(i+1)    #틀린문제 카운트&번호

    for i in range(len(RwaL)):
        if RwaL[i] < 5:
            Rscore -=3
        elif 4 < RwaL[i] <9:
            Rscore -=4
        elif 8 < RwaL[i] <13:
            Rscore -=5.5
        elif 12 < RwaL[i] <17:
            Rscore -=6
        else:
            Rscore -=6.5
  
#----------------------------Reading end-----------------------------
#-------------------------총점 및 레벨 판별 코드---------------------

    lastscore =Vscore + Gscore + Rscore     #테스트3 총점
    studentLevel=""                         #레벨
    if lastscore <= 100:
        studentLevel = "레벨4(50 ~ 100)"
    elif 100 < lastscore <= 150:
        studentLevel = "레벨5(100 ~ 150)"
    elif 150 < lastscore <= 200:
        studentLevel = "레벨6(150 ~ 200)"
    else:
        studentLevel = "레벨7(200 ~ )"

#----------------------------결과도출--------------------------
    print("")
    print("- - - - - - - - - - - - - - - - -")
    print("Vocabulary 점수 :", 30 - Vwa,"개 /", Vscore,"점")
    print("틀린문제", VwaL)
    print("")
    print("Grammer 점수 : ", 20 - Gwa,"개 /", Gscore,"점")
    print("틀린문제", GwaL)
    print("")
    print("Reading 점수 : ", 20 - Rwa,"개 /", Rscore,"점")
    print("틀린문제", RwaL)
    print("- - - - - - - - - - - - - - - - -")

    print("")
    print("---------------------")
    print("총점 : ", lastscore)
    print("Level : ", studentLevel)
    print("---------------------")
    end = input("종료하시려면 enter를 눌러주세요 :)")


def test4():#■■■■■■■■■ Test4■■■■■■■■■■
    print("")
    print("테스트4 채점 프로그램")
    print("정답만 입력하시면 됩니다.")
    print("혹시나 학생이 정답을 못 적었다면1 ~ 5를 제외한 다른 숫자를 하나 적어주세요!★\n")
#-------------------- Vcabulary start----------------------------------
    print("Vocabulary")
    Vanswers = ["1", "3", "4", "5", "2", "5", "3", "5", "5", "1", "5", "5", "3", "1", "3", "5", "2", "4", "5", "2", "1", "1", "4", "3", "5", "5", "2", "3", "2", "1"]
    VinputA = input("정답 입력 : ")
    Vpa = list(str(VinputA))
    
    Vwa=0           #틀린문제 개수
    VwaL=[]         #틀린문제 번호
    Vscore = 100    #총점
    while len(Vanswers) != len(Vpa):
        Vpa.clear()
        print("정답 개수가 다릅니다. 다시 입력해주세요.")
        VinputA = input("정답 입력 : ")
        Vpa = list(str(VinputA))

    for i in range(30):
        if int(Vanswers[i]) != int(Vpa[i]):
            Vwa += 1
            VwaL.append(i+1)    #틀린문제 카운트&번호

    for i in range(len(VwaL)):
        if VwaL[i] < 11:
            Vscore -=2
        elif 10 < VwaL[i] <19:
            Vscore -=3
        elif 18 < VwaL[i] <27:
            Vscore -=4
        else:
            Vscore -=6

#-------------------- Vacabulary end----------------------------------
#-------------------- Grammer start----------------------------------
    print("Grammer")

    Ganswers = ["1", "2", "5", "5", "1", "4", "5", "3", "5", "3", "3", "2", "2", "5", "3", "5", "1", "3", "4", "4"]
    GinputA = input("정답 입력 : ")
    Gpa = list(str(GinputA))

    Gwa=0           #틀린문제 개수
    GwaL=[]         #틀린문제 번호
    Gscore = 100    #총점

    while len(Ganswers) != len(Gpa):
        Gpa.clear()
        print("정답개수가 다릅니다. 다시 입력해주세요.")
        GinputA = input("정답 입력 : ")
        Gpa = list(str(GinputA))

    for i in range(20):
        if int(Ganswers[i]) != int(Gpa[i]):
            Gwa += 1
            GwaL.append(i+1)    #틀린문제 카운트&번호

    for i in range(len(GwaL)):
        if GwaL[i] < 9:
            Gscore -=4
        elif 8 < GwaL[i] <15:
            Gscore -=5
        elif 14 < GwaL[i] <19:
            Gscore -=6
        else:
            Gscore -=7

#-------------------- Grammer end----------------------------------
#-------------------- Reading start----------------------------------
    print("Reading")

    Ranswers = ["2", "5", "2", "3", "2", "1", "4", "2", "4", "4", "2", "2", "1", "1", "2", "1", "2", "4", "2", "2"]
    RinputA = input("정답 입력 : ")
    Rpa = list(str(RinputA))
    
    Rwa=0           #틀린문제 개수
    RwaL=[]         #틀린문제 번호
    Rscore = 100.0    #총점

    while len(Ranswers) != len(Rpa):
        Rpa.clear()
        print("정답개수가 다릅니다. 다시 입력해주세요.")
        RinputA = input("정답 입력 : ")
        Rpa = list(str(RinputA))

    for i in range(20):
        if int(Ranswers[i]) != int(Rpa[i]):
            Rwa += 1
            RwaL.append(i+1)    #틀린문제 카운트&번호

    for i in range(len(RwaL)):
        if RwaL[i] < 3:
            Rscore -=3.5
        elif 2 < RwaL[i] <7:
            Rscore -=4.5
        elif 6 < RwaL[i] <16:
            Rscore -=5
        else:
            Rscore -=6

#----------------------------Reading end-----------------------------
#-------------------------총점 및 레벨 판별 코드---------------------

    lastscore =Vscore + Gscore + Rscore     #테스트4 총점
    studentLevel=""                         #레벨
    if lastscore <= 80:
        studentLevel = "레벨5(45 ~ 80)"
    elif 80 < lastscore <= 120:
        studentLevel = "레벨6(80 ~ 120)"
    elif 120 < lastscore <= 160:
        studentLevel = "레벨7(120 ~ 160)"
    elif 160 < lastscore <= 210:
        studentLevel = "레벨8(160 ~ 210)"
    elif 210 < lastscore <= 250:
        studentLevel = "레벨9(210 ~ 250)"
    else:
        studentLevel = "레벨10(250 ~ )"
#----------------------------결과도출--------------------------
    print("")
    print("- - - - - - - - - - - - - - - - -")
    print("Vocabulary 점수 :", 30 - Vwa,"개 /", Vscore,"점")
    print("틀린문제", VwaL)
    print("")
    print("Grammer 점수 : ", 20 - Gwa,"개 /", Gscore,"점")
    print("틀린문제", GwaL)
    print("")
    print("Reading 점수 : ", 20 - Rwa,"개 /", Rscore,"점")
    print("틀린문제", RwaL)
    print("- - - - - - - - - - - - - - - - -")

    print("")
    print("---------------------")
    print("총점 : ", lastscore)
    print("Level : ", studentLevel)
    print("---------------------")
    end = input("종료하시려면 enter를 눌러주세요 :)")



# ★★★이 위의 코드들은 전부 사용자지정함수이고, 이 밑으로가 main함수의 역할을 합니다.★★★
TestNumber = int(input("1 : Test1 / 2 : Test2 / 3 : Test3 / 4 : Test4\n채점할 테스트에 맞는 번호를 선택해주세요 : "))

if TestNumber == 1:
    test1()
elif TestNumber == 2:
    test2()
elif TestNumber == 3:
    test3()
elif TestNumber == 4:
    test4()
else:
    print("그런 테스트는 없는 것 같아요 8 ^ 8")
    end = input("enter를 누르면 종료됩니다.")
