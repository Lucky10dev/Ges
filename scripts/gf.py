import xml.dom.minidom
import sys
import os

# Aggiungi il percorso del progetto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def prettify_xml(input_file, output_file):
    try:
        # Legge il contenuto del file .ui (XML)
        with open(input_file, 'r', encoding='utf-8') as file:
            xml_str = file.read()
        
        # Parsing della stringa XML e formattazione con indentazione
        dom = xml.dom.minidom.parseString(xml_str)
        pretty_xml_as_str = dom.toprettyxml(indent="    ")
        
        # Scrive il risultato in un nuovo file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(pretty_xml_as_str)
    except Exception as e:
        print(f"An error occurred: {e}")

# Utilizzo:
input_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'views', 'ui', 'dashboard.ui'))
output_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'views', 'ui', 'output.ui'))
prettify_xml(input_file, output_file)
