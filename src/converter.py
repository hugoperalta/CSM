# Modifica el proceso de conversión para aplicar el formato del CMS.

from src.pdf_processor import pdf_to_html
from src.word_processor import docx_to_html
from src.cms_formatter import format_for_cms

def convert_to_cms_format(input_path, output_path):
    if input_path.endswith('.pdf'):
        temp_html = "temp.html"
        pdf_to_html(input_path, temp_html)
    elif input_path.endswith('.docx'):
        temp_html = "temp.html"
        docx_to_html(input_path, temp_html)
    else:
        raise ValueError("Formato de archivo no soportado")

    with open(temp_html, "r", encoding="utf-8") as f:
        html = f.read()

    formatted_html = format_for_cms(html)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted_html)
