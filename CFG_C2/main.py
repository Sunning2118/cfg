from pycparser import c_parser
from pycparser.plyparser import ParseError


def getAttribute(attr):
    print(attr)
    return ''


def getAst(node):  # 遍历AST
    nodeName = node.__class__.__name__  # 节点名称
    nodeChildren = node.children()  # 子节点
    nodeAttributes = node.attr_names  # 节点属性

    nodeAttr = [nodeName]  # 节点名称
    for _, n in nodeChildren:
        nodeAttr.extend(getAst(n))  # 节点名称嵌套

    for attr in nodeAttributes:
        attribute = getattr(node, attr)  # 先获取属性值
        nodeAttr.extend(getAttribute(attribute))  # 自定义当前节点属性str样式

    return nodeAttr


filePath = 'D:/cfg/data/test3.c'

try:
    ast = None
    # ast = parse_file(filePath)
    with open(filePath) as f:
        txtList = f.readlines()  # 按行读取
        txt = ''
        for each in txtList:
            if each.find('#include') != -1:  # 如果找到了
                continue
            elif each.find('//') != -1:  # 不把注释加入其中
                txt += each[:each.find('//')]
            else:
                txt += each
            txt += '\n'
    ast = c_parser.CParser().parse(txt)
    ast.show()
    print(getAst(ast))
except ParseError as e:
    print('代码有错：' + str(e))
except Exception as r:
    print('错误：' + str(r))
