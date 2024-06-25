import unittest
import os
from src.converter import convert_to_cms_format

class TestConverter(unittest.TestCase):

    def setUp(self):
        self.test_pdf = 'data/input/test.pdf'
        self.test_docx = 'data/input/test.docx'
        with open(self.test_pdf, 'wb') as f:
            f.write(b'%PDF-1.4 test content')
        with open(self.test_docx, 'wb') as f:
            f.write(b'PK\x03\x04...test content')  # Simula un archivo DOCX

        self.output_html = 'data/output/test_output.html'

    def tearDown(self):
        if os.path.exists(self.output_html):
            os.remove(self.output_html)
        if os.path.exists(self.test_pdf):
            os.remove(self.test_pdf)
        if os.path.exists(self.test_docx):
            os.remove(self.test_docx)

    def test_convert_pdf_to_cms_format(self):
        convert_to_cms_format(self.test_pdf, self.output_html)
        self.assertTrue(os.path.exists(self.output_html))

        with open(self.output_html, 'r', encoding='utf-8') as f:
            html_content = f.read()
            self.assertIn('<html>', html_content)

    def test_convert_docx_to_cms_format(self):
        convert_to_cms_format(self.test_docx, self.output_html)
        self.assertTrue(os.path.exists(self.output_html))

        with open(self.output_html, 'r', encoding='utf-8') as f:
            html_content = f.read()
            self.assertIn('<html>', html_content)

if __name__ == '__main__':
    unittest.main()
