# ch 7.6.2 ctrl.py
# ui에서 입력되는 이벤트 처리나 ui 동작 제어와 관련된 내용 포함
class Control:
    
    def __init__(self, view):
        self.view = view
        self.connectSignals()
    
    def calculate(self): 
          try: # 숫자가 아닌 값이 입력되었을 대도 프로그램이 동작하도록 예외 처리 구문 추가
                num1 = float(self.view.le1.text())
                num2 = float(self.view.le2.text())
                operator = self.view.cb.currentText()
                # 연산자에 따라 각각 다른 함수를 사용하여 결과를 리턴
                if operator == '+':
                      return f'{num1} + {num2} = {self.sum(num1, num2)}'
                elif operator == '-':
                      return f'{num1} - {num2} = {self.sub(num1, num2)}'
                elif operator == '*':
                      return f'{num1} * {num2} = {self.mul(num1, num2)}'
                elif operator == '/':
                      return f'{num1} / {num2} = {self.div(num1, num2)}'
                elif operator == '^':
                      return f'{num1} ^ {num2} = {self.pow(num1, num2)}'
                else:
                      return "Calculation Error"
          except:
                return "Calculation Error"
        
    def connectSignals(self): # btn1을 클릭하면 calculator 결과가 화면에 표시되도록 수정
        self.view.btn1.clicked.connect(lambda:\
                                       self.view.setDisplay(self.calculate())) 
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b): # 예외 처리 제거 : 향후 calculator 함수에서 처리하도록 구현 예정
            return a+b
    
    def sub(self, a, b):
            return a-b
    
    def mul(self, a, b):
            return a*b
    
    def div(self, a, b):
         return a/b
    
    def pow(self, a, b):
         return pow(a, b)
        