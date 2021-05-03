import sys
import serial
import struct
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from THWstrainGUI_V3 import Ui_MainWindow
from ArduinoConnect import Ui_ComDialog
from serial.tools.list_ports import comports

#Creates serial port and sets baudrate
ser = serial.Serial(baudrate=4800) #115200 230400


# Code for Main GUI window     
class AppWindow(Ui_MainWindow,QMainWindow):
    
# Initializes Main GUI window       
    def __init__(self):
        super(AppWindow,self).__init__()
        self.setupUi(self)

        self.cw = ComWindow()
        
        # Connects to appropriate functions on button clicks

        self.ComConnect.clicked.connect(self.ComClick)
        # self.manual_spool.clicked.connect(self.ManualSpoolMode)
        # self.manual_slide.sliderMoved.connect(self.ManualSlide)
        # self.rightJog.pressed.connect(self.rightMove);
        # self.leftJog.pressed.connect(self.leftMove);
        # self.Zero.clicked.connect(self.UpdateLCD(self.strain_set));
        self.RightPush.pressed.connect(self.rightMove)
        self.LeftPush.pressed.connect(self.leftMove)
        self.RightPush.released.connect(self.stopMove)
        self.LeftPush.released.connect(self.stopMove)
        # self.EStop.clicked.connect();
    
    def keyPressEvent(self, k):
        if k.key() == Qt.Key_Right:
            self.rightMove()
       
        elif k.key() == Qt.Key_Left:
            
            self.leftMove()
        
    def keyReleaseEvent(self, k):
        
        if k.key() == Qt.Key_Right:
            self.stopMove()
            
        elif k.key() == Qt.Key_Left:
            
            self.stopMove()

    def rightMove(self):
    
        txt = str(self.SlideMode.currentText())
        
        if txt == 'Both':
            ser.write(struct.pack('??c',True,True,b'c'))
            
        elif txt == 'Left':
            ser.write(struct.pack('??c',True,False,b'l'))
        else:
            ser.write(struct.pack('??c',True,True,b'r'))
                
    
    def leftMove(self):
        
        txt = str(self.SlideMode.currentText())
        
        if txt == 'Both':
            ser.write(struct.pack('??c',True,False,b'c'))
            
        elif txt == 'Left':
            ser.write(struct.pack('??c',True,True,b'l'))
        else:
            ser.write(struct.pack('??c',True,False,b'r'))
            
            

        
    def stopMove(self):
        ser.write(struct.pack('??c',False,True,b'c'))
        
        # Opens serial communication dialog box
                   
    def ComClick(self):
        self.cw.show()


# code for Communcation Setup Dialog Box        
class ComWindow(Ui_ComDialog, QDialog):
    
    # Initializes Communication Setup Dialog Box
    def __init__(self):
        super(ComWindow,self).__init__() 
        self.setupUi(self)
        self.Com_Refresh.clicked.connect(self.ComList)
        self.ComConnect.clicked.connect(self.SetCom)

    # Finds available Com Ports on Computer (Might need to be modified for Mac)
    def ComList(self):
        ports = [p.device for p in comports()]
        self.ComPort.clear()
        for i in ports:
            self.ComPort.addItem(i)
        self.ComConnect.setEnabled(True)  
    
    # Connects to Com Port     
    def SetCom(self):
        try:
            ser.close()
            ser.port= str(self.ComPort.currentText())
            print('Connected to',ser.port)
            ser.open()
            # w.FailButton.setEnabled(True)
            # ser.write((struct.pack('c?',b's',False)))
        except: 
            print('Could Not Connect. Please Retry')  
   
        
        
        
if __name__ =='__main__':      
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    app.exec_()
    ser.close() #closes serial port
