import fitz  # PyMuPDF

# Implementa las funciones para leer y convertir archivos PDF a HTML

def pdf_to_html(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    html = ""
    for page in doc:
        html += page.get_text("html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)