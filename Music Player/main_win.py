from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from mutagen.mp3 import MP3

from theme import looks
from os.path import expanduser
import sys
import mutagen
from mutagen import mp3

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.player = QMediaPlayer()
        self.currentPlaylist = QMediaPlaylist()
        self.player.setPlaylist(self.currentPlaylist)
        self.userAction= 0
        self.winInit()
        self.show()

    def winInit(self):
        self.setWindowTitle("M pLayer")
        self.setGeometry(200, 200, 500, 500)
        self.addControls()
        self.Menu()

    def addControls(self):
        # widgets initialisation
        wid = QWidget(self)
        self.setCentralWidget(wid)
        controls = QVBoxLayout()
        seekSliderLayout = QHBoxLayout()
        volumeSliderLayout = QHBoxLayout()
        nameLayout = QHBoxLayout()
        self.album_image = QLabel()
        self.volume_icon = QLabel()

        self.startLabel=QLabel()
        self.endLabel = QLabel()




        # Adding the currently playing media name to the player
        self.mediaName = " Open some Music Files "
        self.mediaName_label = QLabel(self.mediaName)
        nameLayout.addWidget(self.mediaName_label)

        # Create next buttonself.mediaName = " Open some Music Files "
        self.nextButton = QPushButton()
        self.nextButton.clicked.connect(self.PlayNext)
        self.nextButton.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipForward))

        # Create next button
        self.previousButton = QPushButton()
        self.previousButton.clicked.connect(self.PlayNext)
        self.previousButton.setIcon(self.style().standardIcon(QStyle.SP_MediaSkipBackward))

        # set initial volume icon
        pic = QPixmap('audacity_a.png')
        self.volume_icon.setPixmap(pic)
        # self.volume_icon.resize(100,100)'Naruto_sadness_and_sorrow.mp3

        # To set the Album
        self.default_pic = QPixmap('album.png')
        self.album_image.setPixmap(self.default_pic)
        self.album_image.resize(200, 300)

        hori = QHBoxLayout()
        self.playButton = QPushButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.volumeSlider = QSlider(Qt.Horizontal)

        # creating the seekslider for positioning the media
        self.seekSlider = QSlider(Qt.Horizontal)
        self.seekSlider.setRange(0, 0)
        self.seekSlider.sliderMoved.connect(self.setPlayerPosition)

        # Adding the seekslider to a horizondal layout
        seekSliderLayout.addWidget(self.startLabel)
        seekSliderLayout.addWidget(self.seekSlider)
        seekSliderLayout.addWidget(self.endLabel)

        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.valueChanged[int].connect(self.changeVolume)
        self.volumeSlider.setToolTip(str(self.volumeSlider.value()))

        self.playButton.clicked.connect(self.playButtonTask)
        playlist = QHBoxLayout()
        playlist.addStretch(1)
        playlist.addWidget(self.album_image)
        playlist.addStretch(1)

        # Horizondal layout to add volume slider
        volumeSliderLayout.addWidget(self.volumeSlider)
        volumeSliderLayout.addWidget(self.volume_icon)
        volumeSliderLayout.addStretch(1)

        # Horizondal play and pause Controls
        hori.addStretch(1)
        hori.addWidget(self.previousButton)
        hori.addWidget(self.playButton)
        hori.addWidget(self.nextButton)
        hori.addStretch(1)
        # hori.addStretch()

        controls.addLayout(playlist)
        controls.addStretch(.5)
        controls.addStretch(1)
        controls.addLayout(nameLayout)
        controls.addLayout(seekSliderLayout)
        controls.addLayout(volumeSliderLayout)
        controls.addLayout(hori)
        wid.setLayout(controls)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
#        self.player.volumeChanged(self.seekSlider.setValue(int(self.player.)))
        self.player.durationChanged.connect(self.durationChange)
        self.player.positionChanged.connect(self.seeksliderPosChange)
        media = self.currentPlaylist.mediaObject()
        self.currentPlaylist.currentMediaChanged.connect(self.songChanged)
        self.player.positionChanged.connect(self.set_Time)

    def set_Time(self,duration):
        self.startLabel.setText('%d:%02d' % (int(duration / 60000), int((duration / 1000) % 60)))

    def songChanged(self):
        media=self.currentPlaylist.currentMedia()
        url=media.canonicalUrl()
        #print(url.Path())
       # file='/home/meliodas/PycharmProjects/project1/04. 18 (1).mp3'
        file2=str(url)
        file2=file2[26:-2]
        #file2=file2[:17]
        #QUrl.to
        pixmap = QPixmap()
        if file2!='' and file2!=None:
            print(file2)
            metadata = mutagen.File(file2)
            for tag in metadata.tags.values():
                if tag.FrameID == 'APIC':
                    pixmap.loadFromData(tag.data)
                    pixmap=pixmap.scaled(512,512,Qt.KeepAspectRatio)
                    self.album_image.setPixmap(pixmap)
                    break
                else:
                    self.album_image.setPixmap(self.default_pic)
                    self.album_image.resize(100, 100)



        name=str(url.fileName())
        name=name[:-4]
        self.mediaName_label.setText(name)



    def changeVolume(self, value):
        self.player.setVolume(value)
        self.status.showMessage('Playing at ' + str(value) + "% volume ")
        self.volumeSlider.setToolTip(str(self.volumeSlider.value()))
        if value >= 80:
            pic = QPixmap('audacity_a.png')
            self.volume_icon.setPixmap(pic)
        elif value < 80 and value > 30:
            pic = QPixmap('volume_medium.re.png')
            self.volume_icon.setPixmap(pic)
        else:
            pic = QPixmap('volume_mute.re.png')
            self.volume_icon.setPixmap(pic)

    def playButtonTask(self):
        if (self.currentPlaylist.mediaCount() == 0):
            self.fileOpen()
            self.player.play()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

        elif (self.player.state() == self.player.PlayingState):
            self.player.pause()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        else:
            self.player.play()
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

    def PlayPrevious(self):
        self.player.playlist().previous()

    def PlayNext(self):
        if (self.currentPlaylist.mediaCount() != 0):
            self.player.playlist().next()

    def setPlayerPosition(self, position):
        if (self.currentPlaylist.mediaCount() != 0):
            self.player.setPosition(position)

    def seeksliderPosChange(self, position):
        self.seekSlider.setValue(position)

    def durationChange(self, position):
        self.seekSlider.setRange(0, position)
        durationT=position

        self.endLabel.setText('%d:%02d' % (int(durationT / 60000), int((durationT / 1000) % 60)))

    def Menu(self):
        menu = self.menuBar()
        filemenu = menu.addMenu('File')
        filemenu.addAction(self.returnFileOpen())
        filemenu.addAction(self.returnFolderOpen())
        filemenu.addAction(self.closeWindow())

        editmenu=menu.addMenu('Edit')
        look=editmenu.addMenu('Look')
        look.addAction(self.retunLightMode())
        look.addAction(self.returnDarkMode())

    def retunLightMode(self):
        light=QAction('Light Mode',self)
        light.setStatusTip('Click to enable light mode')
        light.triggered.connect(self.setlight)
        return light
    def returnDarkMode(self):
        dark=QAction('Dark Mode',self)
        dark.setStatusTip('Click to enable light mode')
        dark.triggered.connect(self.setdark)
        return dark

    def setdark(self):
        palette = looks('dark')
        self.setPalette(palette)

    def setlight(self):
        palette = looks('light')
        self.setPalette(palette)

    def returnFileOpen(self):
        fileop = QAction('Open File', self)
        fileop.setShortcut('Ctrl+O')
        fileop.setStatusTip('To open a music file .')
        fileop.triggered.connect(self.fileOpen)
        return fileop

    def closeWindow(self):
        close = QAction('Close', self)
        close.setStatusTip("Close the player")
        close.setShortcut('Ctrl+Q')
        close.triggered.connect(self.close)
        return close

    def returnFolderOpen(self):
        Folder = QAction('Open Folder', self)
        Folder.setShortcut('Ctrl+F')
        Folder.setStatusTip('Open a folder containing multiple music files')
        Folder.triggered.connect(self.FolderOpen)
        return Folder

    def FolderOpen(self):
        folderChoosen = QFileDialog.getExistingDirectory(self, 'Open Music Folder', expanduser('~'))
        if folderChoosen != None:
            it = QDirIterator(folderChoosen)
            it.next()
            while it.hasNext():
                if it.fileInfo().isDir() == False and it.filePath() != '.':
                    fInfo = it.fileInfo()
                    #print(it.filePath(), fInfo.suffix())
                    if fInfo.suffix() in ('mp3', 'ogg', 'wav'):
                       # print('added file ', fInfo.fileName())
                        self.currentPlaylist.addMedia(QMediaContent(QUrl.fromLocalFile(it.filePath())))
                it.next()
        if (self.currentPlaylist.mediaCount() != 0):
            print('Not empty')
            self.userAction=1
            self.playButtonChange()
            self.Play()


    def fileOpen(self):
        fileChosen = QFileDialog.getOpenFileUrl(self, 'Open Music File', QUrl(""),
                                                "Sound Files (*.mp3 *.ogg *.wav *.m4a)")
        # print(str(fileChosen))
        if fileChosen != None:
            self.player.setPlaylist(self.currentPlaylist)
            self.currentPlaylist.addMedia(QMediaContent(fileChosen[0]))
            self.userAction=1
            self.playButtonChange()
            self.Play()

    def Play(self):
        self.player.setPlaylist(self.currentPlaylist)
        self.player.setVolume(70)
        self.player.play()

    def playButtonChange(self):
        if self.userAction==1:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))




if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Fusion dark palette from https://gist.github.com/QuantumCD/6245215.
    # app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    win = Window()
    palette = looks('dark')
    win.setPalette(palette)
    win.setWindowIcon(QIcon('music.png'))
    # win.show()

sys.exit(app.exec_())
