import unittest
import os
from src.word_processor import docx_to_html

class TestWordProcessor(unittest.TestCase):

    def setUp(self):
        # Crear un archivo DOCX de ejemplo para las pruebas
        self.test_docx = 'data/input/test.docx'
        with open(self.test_docx, 'wb') as f:
            f.write(b'PK\x03\x04...test content')  # Esto solo simula un archivo DOCX

        self.output_html = 'data/output/test_output.html'

    def tearDown(self):
        # Limpiar archivos generados por las pruebas
        if os.path.exists(self.output_html):
            os.remove(self.output_html)
        if os.path.exists(self.test_docx):
            os.remove(self.test_docx)

    def test_docx_to_html(self):
        docx_to_html(self.test_docx, self.output_html)
        self.assertTrue(os.path.exists(self.output_html))

        with open(self.output_html, 'r', encoding='utf-8') as f:
            html_content = f.read()
            self.assertIn('<html>', html_content)

if __name__ == '__main__':
    unittest.main()
