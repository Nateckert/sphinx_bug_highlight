from PySide6 import QtWidgets

# if you don't inherit from QtWidgets.QMainWindow
# the bug disappears
class MainWindow(QtWidgets.QMainWindow):
    pass

