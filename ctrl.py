# ch 6.4.4 ctrl.py
# ui에서 입력되는 이벤트 처리나 ui 동작 제어와 관련된 내용 포함
class Control:
    
    def __init__(self, view):
        self.view = view
        self.connectSignals()
    
    def calculate(self): # calculate 메서드 추가, 내용은 추후에 작성
        pass
        
    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate) # 버튼 1 연결(ui.py에 정의된 버튼 위젯 btn1을 클릭하면 계산하도록 구현)을 변경
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b): # 덧셈 함수 추가
        try:
            return str(a+b)
        except:
            return "Calculation Error"