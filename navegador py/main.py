import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
   def __init__(self):
       super(MainWindow, self).__init__()
       self.browser = QWebEngineView()
       self.browser.setUrl(QUrl('https://google.com/'))
       self.setCentralWidget(self.browser)
       self.showMaximized()

       navbar = QToolBar()
       self.addToolBar(navbar)

       back_btn = QAction('Voltar', self)
       back_btn.triggered.connect(self.browser.back)
       navbar.addAction(back_btn)

       forward_btn = QAction('Avançar', self)
       forward_btn.triggered.connect(self.browser.forward)
       navbar.addAction(forward_btn)

       reload_btn = QAction('Recarregar', self)
       reload_btn.triggered.connect(self.browser.reload)
       navbar.addAction(reload_btn)

       home_btn = QAction('Home', self)
       home_btn.triggered.connect(self.navigate_home)
       navbar.addAction(home_btn)

       self.url_bar = QLineEdit()
       self.url_bar.returnPressed.connect(self.navigate_to_url)
       navbar.addWidget(self.url_bar)

       netflix_btn = QAction('Netflix', self)
       netflix_btn.triggered.connect(self.navigate_netflix)
       navbar.addAction(netflix_btn)

       youtube_btn = QAction('YouTube', self)
       youtube_btn.triggered.connect(self.navigate_yt)
       navbar.addAction(youtube_btn)

       alura_btn = QAction('Alura', self)
       alura_btn.triggered.connect(self.navigate_alura)
       navbar.addAction(alura_btn)

       self.browser.urlChanged.connect(self.update_url)

   def navigate_home(self):
       self.browser.setUrl(QUrl('https://google.com/'))

   def navigate_alura(self):
       self.browser.setUrl(QUrl('https://alura.com.br/'))

   def navigate_yt(self):
       self.browser.setUrl(QUrl('https://youtube.com/'))

   def navigate_netflix(self):
       self.browser.setUrl(QUrl('https://netflix.com/br/'))

   def navigate_to_url(self):
       url = f'https://{self.url_bar.text()}'
       self.browser.setUrl(QUrl(url))

   def update_url(self, q):
       self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('Navegador muito legal')
window = MainWindow()
app.exec_()
