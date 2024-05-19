# ch 5.2.1 main.py
# 애플리케이션 실행과 관련된 부분을 main 함수로 정의
# main 함수 호출 시 view, control 인스턴스를 생성하고 프로그램 실행ㄴ
import sys
from ui import View # ui.py의 View 클래스 추가
from ctrl import Control # ctrl.py의 Control 클래스 추가
from PyQt5.QtWidgets import QApplication

def main(): # 프로그램 실행(Application) 관련 내용 함수화
    calc = QApplication(sys.argv)
    app = QApplication(sys.argv)
    view = View() # View 인스턴스 선언
    Control(view=view) # Control 인스턴스 선언
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()