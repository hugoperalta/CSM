import unittest
import os
from src.pdf_processor import pdf_to_html

class TestPDFProcessor(unittest.TestCase):

    def setUp(self):
        # Crear un archivo PDF de ejemplo para las pruebas
        self.test_pdf = 'data/input/test.pdf'
        with open(self.test_pdf, 'wb') as f:
            f.write(b'%PDF-1.4 test content')

        self.output_html = 'data/output/test_output.html'

    def tearDown(self):
        # Limpiar archivos generados por las pruebas
        if os.path.exists(self.output_html):
            os.remove(self.output_html)
        if os.path.exists(self.test_pdf):
            os.remove(self.test_pdf)

   
