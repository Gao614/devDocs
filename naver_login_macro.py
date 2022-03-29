
import pyautogui    
import time


# 메인으로 사용하는 모니터의 해상도 체크하기
# screenWidth, screenHeight = pyautogui.size()
# print(screenWidth, screenHeight)   


# 마우스의 좌표 가져오기
# x,y = pyautogui.position()
# print(x,y)   


# 로그인위치 라는 변수를 만들기
login_location = (1547,572)


# 로그인버튼 좌표로 마우스 이동하기
pyautogui.moveTo(login_location)


# 해당 위치에서 마우스 클릭하기
pyautogui.click()


# id입력 이라는 변수를 만들고, 클릭하기
type_id = (900,479)
pyautogui.click(type_id)

time.sleep(3)


# 아이디, 비밀번호 변수 만들기
my_id = 'lala1234' # (임의로 구성함, 본인 계정으로 변경) 
my_pw = '1234'   # (임의로 구성함, 본인 계정으로 변경)


# 아이디, 비밀번호를 한 스펠당 0.25초 텀을 두고 입력하기
pyautogui.typewrite(my_id, interval=0.25)
pyautogui.press('tab')   # 아이디 입력후 탭이동
pyautogui.typewrite(my_pw, interval=0.25)    


# 로그인버튼 변수 지정하고, 클릭하기
login_btn =  pyautogui.click(1013,686)
login_btn
