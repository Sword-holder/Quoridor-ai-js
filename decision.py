from js_linker import JSLinker

def make_decision(board_info):
    linker = JSLinker()
    linker.setBoardState(board_info)
    return str(linker.computeDecision())