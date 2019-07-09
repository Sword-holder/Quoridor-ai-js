from linker import Linker
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('file:///Users/nikoyou/Desktop/quoridor/quoridor-ai-7-7/display.html')

class JSLinker(Linker):

    def __init__(self):
        pass
    
    def setBoardState(self, board_info):
        '''
            设置棋盘状态，输入是一个迭代的线性数据结构，不返回任何数据
        '''
        pass

    def computeDecision(self):
        '''
            计算最佳移动步骤
            返回一个动作编号
        '''
        pass
