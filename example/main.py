import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from config.QtOpenI18n import QtOpenI18n
from config.QtOpenIcon import QtOpenIcon
from config.QtOpenStyle import QtOpenStyle
from config.QtOpenTheme import QtOpenTheme
from example.config.QtOpenTreeModel import QtOpenTreeModel, TreeNode

import qtopenui_rc

def build():
    rootItem = TreeNode("root")
    childItem1 = TreeNode("组件总览", rootItem)
    childItem2 = TreeNode("基础组件", rootItem)
    childItem3 = TreeNode("配置组件", rootItem)
    childItem4 = TreeNode("表单组件", rootItem)
    childItem5 = TreeNode("数据展示", rootItem)
    childItem6 = TreeNode("导航组件", rootItem)
    childItem7 = TreeNode("反馈组件", rootItem)
    childItem8 = TreeNode("其他组件", rootItem)
    subChildItem1 = TreeNode("按钮", childItem2)
    subChildItem2 = TreeNode("边框", childItem2)
    subChildItem3 = TreeNode("色彩", childItem2)
    subChildItem4 = TreeNode("布局", childItem2)
    childItem2.appendChild(subChildItem1)
    childItem2.appendChild(subChildItem2)
    childItem2.appendChild(subChildItem3)
    childItem2.appendChild(subChildItem4)
    rootItem.appendChild(childItem1)
    rootItem.appendChild(childItem2)
    rootItem.appendChild(childItem3)
    rootItem.appendChild(childItem4)
    rootItem.appendChild(childItem5)
    rootItem.appendChild(childItem6)
    rootItem.appendChild(childItem7)
    rootItem.appendChild(childItem8)
    return rootItem

def init():
    i18n = QtOpenI18n("resources/languages")
    theme = QtOpenTheme("resources/themes/theme.json")
    style = QtOpenStyle("resources/styles/style.json")
    icon = QtOpenIcon("resources/icons", "qrc:/icons/resources/icons/")
    treeModel = QtOpenTreeModel(build())
    return i18n, theme, style, icon, treeModel

if __name__ == '__main__':
    i18n, theme, style, icon, treeModel = init()
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    # 国际化
    engine.rootContext().setContextProperty("QtOpenI18n", i18n)
    # 主题设置
    engine.rootContext().setContextProperty("QtOpenTheme", theme)
    # icon
    engine.rootContext().setContextProperty("QtOpenIcon", icon)
    # 样式
    engine.rootContext().setContextProperty("QtOpenStyle", style)
    # 树形菜单数据
    engine.rootContext().setContextProperty("QtOpenTreeModel", treeModel)
    # 添加QML路径
    engine.addImportPath(Path(__file__).parent.parent)
    engine.load(QUrl.fromLocalFile("main.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    ret = app.exec()
    del engine
    sys.exit(ret)