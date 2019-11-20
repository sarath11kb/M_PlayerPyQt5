from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import *


class looks(QPalette):
    def __init__(self, choice):
        super(looks, self).__init__()
        if choice == 'dark':

            self.setColor(QPalette.Window, QColor(27, 35, 38))
            self.setColor(QPalette.WindowText, QColor(234, 234, 234))
            self.setColor(QPalette.Base, QColor(27, 35, 38))
            self.setColor(QPalette.AlternateBase, QColor(12, 15, 16))
            self.setColor(QPalette.ToolTipBase, QColor(27, 35, 38))
            self.setColor(QPalette.ToolTipText, Qt.white)
            self.setColor(QPalette.Text, QColor(234, 234, 234))
            self.setColor(QPalette.Button, QColor(27, 35, 38))
            self.setColor(QPalette.ButtonText, Qt.white)
            self.setColor(QPalette.BrightText, QColor(100, 215, 222))
            self.setColor(QPalette.Link, QColor(126, 71, 130))
            self.setColor(QPalette.Highlight, QColor(126, 71, 130))
            self.setColor(QPalette.HighlightedText, Qt.white)
            self.setColor(QPalette.Disabled, QPalette.Light, Qt.black)
          #  self.setColor(QPalette.Disabled, QPalette.shadow, QColor(12, 15, 16))
        if choice == 'light':
            self.setColor(QPalette.Window, QColor(239, 240, 241))
            self.setColor(QPalette.WindowText, QColor(49, 54, 59))
            self.setColor(QPalette.Base, QColor(252, 252, 252))
            self.setColor(QPalette.AlternateBase, QColor(239, 240, 241))
            self.setColor(QPalette.ToolTipBase, QColor(239, 240, 241))
            self.setColor(QPalette.ToolTipText, QColor(49, 54, 59))
            self.setColor(QPalette.Text, QColor(49, 54, 59))
            self.setColor(QPalette.Button, Qt.black)
            self.setColor(QPalette.ButtonText, QColor(49, 54, 59))
            self.setColor(QPalette.BrightText, QColor(255, 255, 255))
            self.setColor(QPalette.Link, QColor(41, 128, 185))
            self.setColor(QPalette.Highlight, QColor(136, 136, 136))
            self.setColor(QPalette.HighlightedText, QColor(239, 240, 241))
            self.setColor(QPalette.Disabled, QPalette.Light, Qt.white)
            self.setColor(QPalette.Disabled, QPalette.Shadow, QColor(234, 234, 234))
    
