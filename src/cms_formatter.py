def format_for_cms(html):
    # Aquí agregamos las modificaciones específicas que necesita el CMS
    # Ejemplo: Añadir clases CSS específicas, modificar etiquetas, etc.
    formatted_html = html.replace('<h1>', '<h1 class="cms-title">')
    # Realiza más transformaciones según sea necesario
    return formatted_html
