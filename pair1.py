def add_commas_to_number():
    e = 0
    while e != 3:
        try: 
            user_input = input("숫자를 입력하세요: ")
            if len(user_input) > 20:raise ValueError()    
            return "{:,}".format(int(user_input))
        except ValueError:
            e += 1
            print("오류: 유효한 숫자가 아닙니다. 숫자만 입력하세요.")
print(add_commas_to_number())
