#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2024/8/16 11:33
# @Author : junwen Liu
# @Site :
# @File : pdf3.py
# @Email   : junwenLiu0201@126.com
# @Software: PyCharm

import sys
import fitz  # PyMuPDF
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget,QMainWindow
from PyQt5.QtGui import QPixmap, QImage

class PDFViewerWidget(QWidget):
    def __init__(self, parent=None):
        super(PDFViewerWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def display_pdf_from_stream(self, url):
        response = requests.get(url)
        doc = fitz.open("pdf", response.content)  # 直接从内存中加载 PDF 数据
        page = doc.load_page(0)  # 读取第一页
        pix = page.get_pixmap()  # 渲染页面为图像
        img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(img))

# 示例主窗口类，展示如何在其他 PyQt UI 中使用 PDFViewerWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.pdf_viewer = PDFViewerWidget(self)
        self.layout.addWidget(self.pdf_viewer)

        self.setWindowTitle("PDF Viewer Inside PyQt5")
        self.resize(800, 600)

        # 直接从 URL 流显示 PDF
        self.pdf_viewer.display_pdf_from_stream("https://www.cima.ky/upimages/lawsregulations/SpecialEconomicZonesAct2023Revision_1675093194.PDF")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
