from linker import Linker
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

class JSLinker(Linker):

    def __init__(self):
        pass
    
    def setBoardState(self, board_info):
        '''
            设置棋盘状态，输入是一个迭代的线性数据结构，不返回任何数据
        '''
        driver.get('file:///Users/nikoyou/Desktop/quoridor/quoridor-ai-7-7/display.html')
        js_code = 'setAIPlace(' + str(board_info[0]) + ', ' + str(board_info[1]) + ');\n'
        js_code += 'setOpponentPlace(' + str(board_info[2]) + ', ' + str(board_info[3]) + ');\n'
        js_code += 'setAIWallNumbers(' + str(board_info[4]) + ');\n'
        js_code += 'setOpponentWallNumbers(' + str(board_info[5]) + ');\n'
        for i in range(6, len(board_info)):
            order = i - 6
            if board_info[i] == 1: # 放置横向挡板
                js_code += 'setHorizontalWall(' + str(order // 6) + ', ' + str(order % 6) + ');\n'
            elif  board_info[i] == 2: # 放置竖直挡板
                js_code += 'setVerticalWall(' + str(order // 6) + ', ' + str(order % 6) + ');\n'
        # print(js_code)
        driver.execute_script(js_code)

    def computeDecision(self):
        '''
            计算最佳移动步骤
            返回一个动作编号
        '''
        pass

if __name__ == '__main__':
    linker = JSLinker()
    linker.setBoardState([
    1, 2, 
    3, 4, 
    6, 7, 
    0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 
    0, 0, 2, 0, 0, 0, 
    0, 0, 0, 1, 0, 0, 
    0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 1, 0 ])