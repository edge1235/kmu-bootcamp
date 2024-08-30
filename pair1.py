def add_commas_to_number():
    try:
        user_input = input("숫자를 입력하세요: ")
        negative =0
        if user_input[0]=='-':
            negative=1
            del user_input[0]
        #최대 20자리
        if len(user_input) > 20:
            raise ValueError()
        
        user_input = list(user_input)
        user_input.reverse()
        cnt = 0
        tmp = []
        len_t = len(user_input)
        for i in range(len_t):
            if(cnt%3 == 0 and cnt!=0):
                tmp.append(',')
            cnt+=1
            tmp.append(user_input[i])
                        
        tmp.reverse()
        for i in tmp:
            print(i,end='')
        #user_input=user_input[::-1]
        #if negative==1: '-' + user_input    
        
        #print(user_input)

    except ValueError:
        print("오류: 유효한 숫자가 아닙니다. 숫자만 입력하세요.")


add_commas_to_number()
