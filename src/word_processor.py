from docx import Document
from mammoth import convert_to_html

# Implementa las funciones para leer y convertir archivos Word a HTML

def docx_to_html(docx_path, output_path):
    with open(docx_path, "rb") as f:
        result = convert_to_html(f)
        html = result.value
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
