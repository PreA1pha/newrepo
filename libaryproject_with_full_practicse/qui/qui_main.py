import sys
from PyQt5 import QtWidgets
uygulama= QtWidgets.QApplication(sys.argv)#sistem üzerinde uyguma açmasını sağlar
pencere = QtWidgets.QWidget()#widget ranımladık(açtık)
pencere.setWindowTitle("btk tekrar")#başlık tanımladık
pencere.show()#uygulammızı göstmerttik
sys.exit(uygulama.exec())#pencereyi kapttığımızda uygulamada kapanacak