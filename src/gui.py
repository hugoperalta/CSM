import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from src.converter import convert_to_cms_format

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(400, 300)  # Tamaño fijo de la ventana
        layout = QVBoxLayout()

        self.label = QLabel("Selecciona un archivo PDF o Word")
        layout.addWidget(self.label)

        self.btn_select = QPushButton("Seleccionar Archivo")
        self.btn_select.clicked.connect(self.select_file)
        layout.addWidget(self.btn_select)

        self.btn_convert = QPushButton("Convertir a HTML para CMS")
        self.btn_convert.clicked.connect(self.convert_file)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)
        self.setWindowTitle('Conversor PDF/Word a HTML')
        self.show()

    def select_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo", "", "All Files (*);;PDF Files (*.pdf);;Word Files (*.docx)", options=options)
        if file_path:
            self.file_path = file_path
            self.label.setText(f"Archivo seleccionado: {file_path}")

    def convert_file(self):
        if hasattr(self, 'file_path'):
            output_path, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo HTML", "", "HTML Files (*.html)", options=QFileDialog.Options())
            if output_path:
                convert_to_cms_format(self.file_path, output_path)
                self.label.setText(f"Archivo convertido y guardado en: {output_path}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Establece el estilo Fusion

    # Aplicar una hoja de estilo (QSS) personalizada
    style = """
        QWidget {
            background-color: #f0f0f0;
            font-size: 14px;
        }
        QPushButton {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px;
            font-size: 14px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QLabel {
            font-size: 16px;
            color: #333;
        }
    """
    app.setStyleSheet(style)

    ex = ConverterApp()
    sys.exit(app.exec_())
