# gui
# Graphic User Interface

# Tkinter
import tkinter

window = tkinter.Tk()
# 이름 붙이기
window.title("HK's GUI Program")
# 최소 크기 적용
window.minsize(width=500, height=300)


#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))

# 라벨 생성후 컴포넌트 배치
my_label.pack(expand=True)

# 윈도우가 계속 작동하게 함
window.mainloop()

Arguments with Default Values
def my_function(A=1, b=2, c=3)
입력하지 않은 인수 값의 경우 default values를 가지고 있어 입력하지 않은 인수 값이 있더라도(누락 인수) 사용이 가능하다.
