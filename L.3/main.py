from PyQt5.QtWidgets import (
    QApplication, QWidget,
QFileDialog, QLabel, QListWidget,
QHBoxLayout, QVBoxLayout,
QPushButton, QInputDialog, QMainWindow
)
import os
from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from ui import Ui_Main_Window

class Widget(QMainWindow):
    def  __init__(self):
        super().__init__()
        self.ui = Ui_Main_Window()
        self.ui.setupUi(self)
          
class ImageProcessor():
    def __init__(self):
        
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
        
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(self.dir, self.filename)
        self.image = Image.open(image_path)
    
    def showImage(self, path):
        ex.ui.label.hide()
        pixmapimage = QPixmap(path)
        w, h = ex.ui.label.width(), ex.ui.label.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        ex.ui.label.setPixmap(pixmapimage)
        ex.ui.label.show()
    
    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.showImage(image_path)
        
    def do_sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.showImage(image_path)
    
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.showImage(image_path)
        
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.showImage(image_path)
    
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.showImage(image_path)

    def do_up(self):
        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        self.saveImage()
        image_path = os.path.join(
            workdir, self.save_dir, self.filename
        )
        self.showImage(image_path)
    
    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def do_resise(self):
        size = QInputDialog.getText(ex, "RESISE IMAGE", "WIDTH, HEIGHT")
        x,y = (size[0].replace("","")).split(",")
        print(x,y)
        self.image = self.image.resize((int(x.strip()), int(y.strip()), ))
        self.saveImage()
        Image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(Image_path)
                   
workdir = ""

def filter(files, extentions):
    result = []
    for filename in files:
        for ext in extentions:
            if filename.endswith(ext):
                result.append(filename)
    return result
    
def chose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    
def show_filenane_list():
    extentions = [".jpg", ".png", ".jpeg",
                  ".gif", ".bmp"]
    chose_workdir()
    filenames = filter(os.listdir(workdir),
                       extentions)
    ex.ui.lw_files.clear()
    for filename in filenames:
        ex.ui.lw_files.addItem(filename)

workimage = ImageProcessor()

def showChosenImage():
    if ex.ui.lw_files.currentRow() >= 0:
        filename = ex.ui.lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir,
                                  workimage.filename)
        workimage.showImage(image_path)

app = QApplication([])
ex = Widget()    
ex.show()
app.exec_()