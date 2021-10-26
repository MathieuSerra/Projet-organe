'''
File to launch app
'''
# General imports
import sys
sys.path.append("..")
import os
import time
import h5py
from datetime import datetime
from tqdm import tqdm

# Qt imports
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QTableWidgetItem, QAbstractItemView, \
    QMainWindow, QLabel, QProgressBar, QMessageBox, QProgressDialog

# Calculation imports
import math
import numpy as np
from matplotlib import pyplot as plt


class Controller(QMainWindow):
    '''Class for the app's main window'''

    sig_update_progress = QtCore.pyqtSignal(int) #Signal for progress bar in status bar

    def __init__(self):
        QMainWindow.__init__(self)
        
        # Load user interface
        basepath = os.path.join(os.path.dirname(__file__))
        uic.loadUi(os.path.join(basepath,"interface.ui"), self)

        # Create status bar
        self.label_statusBar = QLabel()
        self.progress_statusBar = QProgressBar()
        self.statusbar.addPermanentWidget(self.label_statusBar)
        self.statusbar.addPermanentWidget(self.progress_statusBar)
        self.progress_statusBar.hide()
        self.progress_statusBar.setFixedWidth(250)

        self.sig_update_progress.connect(self.progress_statusBar.setValue)

        # Initiate buttons
    
    def update_status_bar(self, text=''):
        '''Updates the status bar text'''

        self.label_statusBar.setText(text)

    def show_error_popup(self, error=''):
        '''Shows error popup'''
        
        error_popup = QMessageBox()
        error_popup.setWindowTitle('Program Error')
        error_popup.setText('Error while '+error+', please try again')
        error_popup.setIcon(QMessageBox.Warning)
        error_popup.setStandardButtons(QMessageBox.Ok)
        error_popup.setDefaultButton(QMessageBox.Ok)
        error_popup.exec_()

# Launch app
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show()
    app.exec_()