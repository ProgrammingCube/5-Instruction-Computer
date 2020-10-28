import sys, os, time, math
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, pyqtSlot

form_class = uic.loadUiType("main.ui")[0]
register_set = set('abcdefxy')
registers = 'abcdefgxy'

err = False

def parseCode(self):
    instCount = 0
    self.codeStatus.setText("Running...")
    pc = 0
    lines = self.codeEdit.document().blockCount()
    boxList = []
    regText = []
    regText.append(self.registerAValue)
    regText.append(self.registerBValue)
    regText.append(self.registerCValue)
    regText.append(self.registerDValue)
    regText.append(self.registerEValue)
    regText.append(self.registerFValue)
    regText.append(self.registerXValue)
    regText.append(self.registerYValue)

    boxList.append(self.incBox)
    boxList.append(self.decBox)
    boxList.append(self.iszBox)
    boxList.append(self.jmpBox)
    boxList.append(self.stpBox)

    boxCounter = 0

    while (pc < lines):
        currentLine = self.codeEdit.document().findBlockByLineNumber(pc).text()
        currentLine = currentLine.lstrip()  #remove leading whitespaces
        if currentLine[0] == ';':
            pc += 1
            continue
        tokens = currentLine.split()
        #print(currentLine)
        #parse the opcode.
        #because it is like only 5 instructions,
        #I'm not sweating good coding practice here.
        boxList[boxCounter].setStyleSheet(
            "QCheckBox::indicator"
                               "{"
                               "background-color : white;"
                               "}"
        )
        QApplication.processEvents()
        if tokens[0] ==  "inc":
            try:
                reg = registers.index(tokens[1])
            except:
                self.codeStatus.setText('NONEXISTANT REGISTER')
                err = True
                break
            tempreg = regText[reg].text()
            try:
                tempreg = int(tempreg)
            except:
                self.codeStatus.setText('NONINT IN REGISTER')
                err = True
                break
            tempreg = tempreg + 1
            regText[reg].setText(str(tempreg))
            boxCounter = 0
            pc += 1

        elif tokens[0] ==  "dec":
            try:
                reg = registers.index(tokens[1])
            except:
                self.codeStatus.setText('NONEXISTANT REGISTER')
                err = True
                break
            tempreg = regText[reg].text()
            try:
                tempreg = int(tempreg)
            except:
                self.codeStatus.setText('NONINT IN REGISTER')
                err = True
                break
            tempreg = tempreg - 1
            if tempreg < 0:
                self.codeStatus.setText('NEGATIVE REGISTER')
                err = True
                self.stop = True
            regText[reg].setText(str(tempreg))
            boxCounter = 1
            pc += 1
        
        elif tokens[0] ==  "jmp":
            try:
                pc = int(tokens[1])
            except:
                self.codeStatus.setText('NONINT PC')
                err = True
                break
            boxCounter = 3

        elif tokens[0] ==  "isz":
            try:
                reg = registers.index(tokens[1])
            except:
                self.codeStatus.setText('NONEXISTANT REGISTER')
                err = True
                break
            regTest = regText[reg].text()
            try:
                testReg = int(regTest)
            except:
                self.codeStatus.setText('NONINT IN REGISTER')
                err = True
                break
            if testReg == 0:
                pc += 2
            else:
                pc += 1
            boxCounter = 2

        elif tokens[0] ==  "stp":
            boxCounter = 4
            self.codeStatus.setText("Done!")
            self.stop = True
        
        if tokens[0] == 'stp':
            tokens.append('')
        self.instructionBox.setText(tokens[0] + ' ' + tokens[1])
        boxList[boxCounter].setStyleSheet(
            "QCheckBox::indicator"
                               "{"
                               "background-color : lightgreen;"
                               "}"
        )

        instCount += 1
        self.instructionCounter.setText("Step counter:" + str(instCount))
        QApplication.processEvents()
        if self.stop:
            self.stop = False
            break
        time.sleep(int(self.currentSpeed.text())/1000)

class mainWindow(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.instructionCounter.setText("Step counter: 0")
        #can possibly put this into a stylesheet somehow...
        self.incBox.setStyleSheet(
            "QCheckBox::indicator"
                               "{"
                               "background-color : white;"
                               "}"
        )
        self.decBox.setStyleSheet(
            "QCheckBox::indicator"
                               "{"
                               "background-color : white;"
                               "}"
        )
        self.iszBox.setStyleSheet(
            "QCheckBox::indicator"
                               "{"
                               "background-color : white;"
                               "}"
        )
        self.jmpBox.setStyleSheet(
            "QCheckBox::indicator"
                               "{"
                               "background-color : white;"
                               "}"
        )
        self.stpBox.setStyleSheet(
            "QCheckBox::indicator"
                               "{"
                               "background-color : white;"
                               "}"
        )

        self.runButton.clicked.connect(self.start_clicked)
        self.stopButton.clicked.connect(self.stop_clicked)
        self.stepButton.clicked.connect(self.step_clicked)
        self.speedSlider.setSingleStep(10)
        self.speedSlider.valueChanged[int].connect(self.speedChange)

        self.stop = False

        self.initUI()
    
    def initUI(self):
        #self.statusBar().showMessage('When you : bottom text')
        self.show()
    
    @pyqtSlot()
    def start_clicked(self):
        print('Running...')
        self.stop = False
        parseCode(self)
        if err == True:
            self.codeStatus.setText("Done!")
    
    def stop_clicked(self):
        print('stopping code...')
        self.codeStatus.setText("Stopped!")
        self.stop = True
    
    def step_clicked(self):
        print('Stepping...')
    
    def speedChange(self, value):
        self.currentSpeed.setText(str(value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex  = mainWindow()
    sys.exit(app.exec_())