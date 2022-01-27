'''
File to launch app
'''
# General imports
import sys
sys.path.append("..")
import os
import time
#qimport h5py
from datetime import datetime
#from tqdm import tqdm

# Communication with C-ARM
#import serial
#ser = serial.Serial('COM3',9600)

# Qt imports
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle ##

# Calculation imports
#import math
import numpy as np
#from matplotlib import pyplot as plt

import cv2
# imported fluor
img_fluoro=cv2.imread('fluoro_1.jpg')


class Controller(QMainWindow):
    '''Class for the app's main window'''

    sig_update_progress = pyqtSignal(int) #Signal for progress bar in status bar
    sig_update_motor_angle = pyqtSignal(int) ###

    def __init__(self):
        QMainWindow.__init__(self)
        
        # Load user interface
        basepath = os.path.join(os.path.dirname(__file__))
        uic.loadUi(os.path.join(basepath,"interface.ui"), self)
        self.showMaximized()

        # Initialize status variables
        self.camera1Active = True
        self.camera2Active = True
        self.camera3Active = True

        # Initiate buttons
        self.pushButton_camera1.clicked.connect(self.activateDeactivateCam1)
        self.pushButton_cameraTraitee.clicked.connect(self.activateDeactivateCam1)
        self.pushButton_camera2.clicked.connect(self.activateDeactivateCam2)
        self.pushButton_camera3.clicked.connect(self.FocusOnCam3)

        self.pushButton_rotateLeft.clicked.connect(self.rotate_left)
        self.pushButton_rotateRight.clicked.connect(self.rotate_right)
        self.horizontalSlider.valueChanged.connect(self.updateAngle)
        self.horizontalSlider.setMinimum(-45)
        self.horizontalSlider.setMaximum(45)
        self.dial.valueChanged.connect(self.updateAngle2)
        self.dial.setMinimum(-45)
        self.dial.setMaximum(45)

        # Start camera thread
        self.thread1 = Camera1_Thread(self.label_camera1, self.label_cameraTraitee)
        self.startCamera1()

        self.thread2 = Camera2_Thread()
        self.startCamera2()

        # Create status bar
        self.label_statusBar = QLabel()
        self.progress_statusBar = QProgressBar()
        self.statusbar.addPermanentWidget(self.label_statusBar)
        self.statusbar.addPermanentWidget(self.progress_statusBar)
        self.progress_statusBar.hide()
        self.progress_statusBar.setFixedWidth(250)

        self.sig_update_progress.connect(self.progress_statusBar.setValue)

        self.sig_update_motor_angle.connect(self.updateAngle)

    def startCamera1(self):
        '''Start camera 1'''
        try:
            self.thread1.start()
            self.thread1.imageUpdate.connect(self.imageUpdateSlot)
            self.thread1.imageUpdateXray.connect(self.imageUpdateSlotXray)
        except:
            self.showErrorPopup('starting camera 1')

    def startCamera2(self):
        '''Start camera 2'''
        try:
            self.thread2.start()
            self.thread2.imageUpdate2.connect(self.imageUpdateSlot2)
        except:
            self.showErrorPopup('starting camera 2')

    def imageUpdateSlot(self, Image):
        '''Update camera 1 image with the images emitted by the thread'''
        self.label_camera1.setPixmap(QPixmap.fromImage(Image))
        ##width = self.label_camera1.width()
        ##height = self.label_camera1.height()
        ##self.label_camera1.setPixmap(QPixmap.fromImage(Image).scaled(width, height, Qt.KeepAspectRatio))

    def imageUpdateSlotXray(self, Image):
        '''Update camera 1 image with the Xray images emitted by the thread'''
        self.label_cameraTraitee.setPixmap(QPixmap.fromImage(Image))

    def imageUpdateSlot2(self, Image):
        '''Update camera 1 image with the images emitted by the thread'''
        self.label_camera2.setPixmap(QPixmap.fromImage(Image))


    def activateDeactivateCam1(self):
        '''Stop or activate camera 1 feed'''
        if self.camera1Active:
            self.thread1.stop()
            self.pushButton_camera1.setText('Activer')
            self.pushButton_camera1.setIcon(QIcon(os.getcwd()+"\\icones\\icon-play-white.png"))
            self.pushButton_cameraTraitee.setText('Activer')
            self.pushButton_cameraTraitee.setIcon(QIcon(os.getcwd()+"\\icones\\icon-play-white.png"))
            self.camera1Active = False
        else:
            self.startCamera1()
            self.pushButton_camera1.setText('Pauser')
            self.pushButton_camera1.setIcon(QIcon(os.getcwd()+"\\icones\\icon-pause-white.png"))
            self.pushButton_cameraTraitee.setText('Pauser')
            self.pushButton_cameraTraitee.setIcon(QIcon(os.getcwd()+"\\icones\\icon-pause-white.png"))
            self.camera1Active = True

    def activateDeactivateCam2(self):
        '''Stop or activate camera 1 feed'''
        if self.camera2Active:
            self.thread2.stop()
            self.pushButton_camera2.setText('Activer')
            self.pushButton_camera2.setIcon(QIcon(os.getcwd()+"\\icones\\icon-play-white.png"))
            self.camera2Active = False
        else:
            self.startCamera2()
            self.pushButton_camera2.setText('Pauser')
            self.pushButton_camera2.setIcon(QIcon(os.getcwd()+"\\icones\\icon-pause-white.png"))
            self.camera2Active = True

    def FocusOnCam3(self):###
        ''' '''
        self.groupBox_4.setGeometry(100,200,400,500)
    
    def updateAngle(self):
        angle = self.horizontalSlider.value()
        self.label_angle.setText('Angle : '+str(angle)+'°')
        #ser.write(angle)

    def updateAngle2(self):
        angle = self.dial.value()
        self.label_angle.setText('Angle : '+str(angle)+'°')


    def update_status_bar(self, text=''):
        '''Updates the status bar text'''

        self.label_statusBar.setText(text)

    def showErrorPopup(self, error=''):
        '''Shows error popup'''
        
        error_popup = QMessageBox()
        error_popup.setWindowTitle('Program Error')
        error_popup.setText('Error while '+error+', please try again')
        error_popup.setIcon(QMessageBox.Warning)
        error_popup.setStandardButtons(QMessageBox.Ok)
        error_popup.setDefaultButton(QMessageBox.Ok)
        error_popup.exec_()
    
    def rotateMotor(self):
        '''Rotates right the motor'''
        pass

    def rotate_left(self):
        '''Rotates left the motor'''
        pass

    def rotate_right(self):
        '''Rotates right the motor'''
        pass

    def resizeEvent(self, event):
        '''Executes when the main window is resized'''
        pass
        #self.label.resize(self.width(), self.height())

#    def closeEvent(self, event):
#        '''Making sure that everything is closed when the user exits the software.
#           This function executes automatically when the user closes the UI.
#           This is an intrinsic function name of Qt, don't change the name even 
#           if it doesn't follow the naming convention'''
#
#        if self.camera1Active:
#            self.thread1.stop()
#        if self.camera2Active:
#            self.thread2.stop()
#
#        print('Window closed')

class Camera1_Thread(QThread):
    '''Thread that emits a QT image from camera 1'''

    imageUpdate = pyqtSignal(QImage)
    imageUpdateXray = pyqtSignal(QImage)

    def __init__(self, image_label1, image_label2):
        super().__init__()
        self.image_label1 = image_label1
        self.image_label2 = image_label2
    
    def run(self):
        self.threadActive = True
        VideoDevice1 = 0##2 ##0 ##À changer selon le device # Webcam
        Capture = cv2.VideoCapture(VideoDevice1, cv2.CAP_DSHOW)
        #img=cv2.imread('fluoro_1.jpg')
        
        while self.threadActive:
            ##print(self.image_label1.width())
            ##print(self.image_label1.height())
            ##
            ret, frame = Capture.read()
            if ret: # If there is no issue with the capture
                # Original camera 1 image
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert to RGB
                FlippedImage = cv2.flip(Image, 1)
                
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888) #Size: (640, 480) = (4,3)
                ##Pic = ConvertToQtFormat.scaled(self.image_label1.width(), self.image_label1.height(), Qt.KeepAspectRatio) 
                #Pic = ConvertToQtFormat.scaled(320, 240, Qt.KeepAspectRatio)
                Pic = ConvertToQtFormat.scaled(200, 150, Qt.KeepAspectRatio)
                self.imageUpdate.emit(Pic)

                # Processed camera 1 image (x ray)
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert to RGB
                width=480
                height=480
                sImage=Image[0:width, 0:height]
                simg=img_fluoro[0:width, 0:height]
                img_gray_fluoro=cv2.cvtColor(simg, cv2.COLOR_BGR2GRAY)
                gray=cv2.cvtColor(sImage, cv2.COLOR_BGR2GRAY)
                FlippedImage = cv2.flip(gray, 1)
                _, th1=cv2.threshold(FlippedImage, np.mean(FlippedImage)-20, 255, cv2.THRESH_TOZERO)
                #sum2=cv2.bitwise_and(FlippedImage,FlippedImage,mask=th1)
                #sum2=cv2.bitwise_not(sum2)
                #final=cv2.bitwise_and(th1,img_gray_fluoro)
                final=cv2.addWeighted(th1,0.6,img_gray_fluoro,0.5,0)
                # Convert to QT format
                ConvertToQtFormat = QImage(final.data, final.shape[1], final.shape[0], QImage.Format_Grayscale8) #Size: (640, 480)
                ##Pic = ConvertToQtFormat.scaled(self.image_label2.width(), self.image_label2.height(), Qt.KeepAspectRatio) 
                #Pic = ConvertToQtFormat.scaled(320, 240, Qt.KeepAspectRatio)
                Pic = ConvertToQtFormat.scaled(800, 600, Qt.KeepAspectRatio)
                self.imageUpdateXray.emit(Pic)
    
    def stop(self):
        self.threadActive = False
        self.quit()

class Camera2_Thread(QThread):
    '''Thread that emits a QT image from camera 2'''

    imageUpdate2 = pyqtSignal(QImage)
    
    def run(self):
        self.threadActive = True
        VideoDevice2 = 3
        Capture = cv2.VideoCapture(VideoDevice2, cv2.CAP_DSHOW) ##cv2.VideoCapture(0) # Webcam
        
        while self.threadActive:
            ret, frame = Capture.read()
            if ret: # If there is no issue with the capture
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert to RGB
                FlippedImage = cv2.flip(Image, 1)
                
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(320, 240, Qt.KeepAspectRatio)
                self.imageUpdate2.emit(Pic)
    
    def stop(self):
        self.threadActive = False
        self.quit()

# Launch app
if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) ##
    controller = Controller()
    controller.show()
    sys.exit(app.exec_())