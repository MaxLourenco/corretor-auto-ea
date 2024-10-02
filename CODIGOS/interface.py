import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.setWindowTitle("Corretor de Gabaritos PS Em Ação")
        self.setGeometry(100, 100, 400, 300)

        # Layout de grade
        layout = QGridLayout()

        # Ajustar margens e espaçamento
        layout.setContentsMargins(20, 20, 20, 20)  # (esquerda, topo, direita, fundo)
        layout.setSpacing(10)  # Espaçamento entre os widgets

        # Título
        title_label = QLabel("Seja bem-vindo, voluntário!")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Adiciona o título ao layout (ocupando 2 colunas e 1 linha)
        layout.addWidget(title_label, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)

        # Botões (organizados em uma matriz 2x2)
        button1 = QPushButton("Botão 1")
        button2 = QPushButton("Botão 2")
        button3 = QPushButton("Botão 3")
        button4 = QPushButton("Botão 4")

        # Ajustando o tamanho dos botões
        button_size = (100, 50)  # largura, altura
        for button in [button1, button2, button3, button4]:
            button.setFixedSize(*button_size)

        # Adiciona os botões ao layout com alinhamento centralizado
        layout.addWidget(button1, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)  # Linha 1, Coluna 0
        layout.addWidget(button2, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)  # Linha 1, Coluna 1
        layout.addWidget(button3, 2, 0, alignment=Qt.AlignmentFlag.AlignCenter)  # Linha 2, Coluna 0
        layout.addWidget(button4, 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)  # Linha 2, Coluna 1

        # Define o layout na janela
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
