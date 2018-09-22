# -*- coding: utf-8 -*-
"""
操作系统：Microsoft Windows 10 家庭中文版 (BUILD:17134) (64 位)
CPU信息：Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz
步进：3 型号：E 系列：6 扩展型号：5E 扩展系列：6
主板信息：Dell (戴尔) 0H0CC0
内存信息：8.0 GB (8.0 GB / )
显卡信息：NVIDIA GeForce GTX 960M
Intel(R) HD Graphics 530

硬盘信息：ST1000LM014-1EJ164 (1.0 TB)
SanDisk SD8SNAT256G1122 (256.0 GB)

网卡信息：Realtek PCIe GBE Family Controller (以太网)
Intel(R) Dual Band Wireless-AC 3165 (WLAN)
Microsoft Wi-Fi Direct Virtual Adapter #3
Microsoft Wi-Fi Direct Virtual Adapter #4
WAN Miniport (IP)
WAN Miniport (IPv6)
WAN Miniport (Network Monitor)

声卡信息：Realtek High Definition Audio
英特尔(R) 显示器音频

显示设备：LG [LGD04B9] 15.3英寸
"""
# 遗传算法
# 最大进化代数：10000
# 种群数目：1000
# 染色体长度（城市数目）：106
# 运行时间：35秒
import core
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QPen, QPixmap, QBrush, QPalette
from PyQt5.QtCore import Qt
import time


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(50, 50, 900, 900)  
        self.setWindowTitle('数据可视化')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()  
        qp.begin(self)
        self.insert_png(qp)
        self.draw_points(qp)
        self.draw_lines(qp)
        qp.end()

    @staticmethod
    def insert_png(qp):
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        # (253,81),(1173,740)
        # (192,81),(862,608)
        qp.drawPixmap(192-253-90, 81-81-90, 1173+120, 740+120, QPixmap("海南地图.png"))

    @staticmethod
    def draw_points(qp):
        qp.setPen(Qt.red)
#        size = self.size()
        for i in range(core.getRow()):  
            x = core.getPoint(i)[1]-30
            y = core.getPoint(i)[2]
            qp.drawRect(x, y, 4, 4)

    @staticmethod
    def draw_lines(qp):
        pen = QPen(Qt.green, 1, Qt.SolidLine)
        for i1 in range(core.getRow()):
            for i2 in range(core.getRow()):
                qp.setPen(pen)
                x1 = core.getPoint(i1)[1]-30
                y1 = core.getPoint(i1)[2]
                x2 = core.getPoint(i2)[1]-30
                y2 = core.getPoint(i2)[2]
                if core.getSide(i1, i2) == 1:
                    qp.drawLine(x1+2, y1+2, x2+2, y2+2)


if __name__ == '__main__':
    start = time.clock()
    core.initGraph()
    app = QApplication(sys.argv)  
    window = Window()  
    end = time.clock()
    print(end-start)
    sys.exit(app.exec_())
