import xml.etree.ElementTree as ET
import re

# Carregar o arquivo XML
tree = ET.parse('feed_psel.xml')
root = tree.getroot()

# Função para extrair a cor do título
def extract_color_from_title(title):
    # Lista de cores para exemplo
    colors = ['vermelho', 'azul', 'verde', 'amarelo', 'preto', 'branco']
    for color in colors:
        if color in title.lower():
            return color
    return 'Indefinido'  # Retornar um valor padrão se nenhuma cor for encontrada

# Função para corrigir os links das imagens
def correct_image_link(link):
    # Exemplo de correção: adicionar 'https://' se estiver faltando
    if not link.startswith('http://') and not link.startswith('https://'):
        return 'https://' + link
    return link

# Excluir produtos fora de estoque
for product in root.findall('product'):
    if product.find('stock').text == '0':  # Supondo que '0' signifique fora de estoque
        root.remove(product)

# Adicionar cor aos produtos
for product in root.findall('product'):
    if product.get('id') in ['261557', '235840']:
        title = product.find('title').text
        color = extract_color_from_title(title)
        product.find('color').text = color

# Corrigir links das imagens
for product in root.findall('product'):
    if product.get('id') in ['246804', '217865']:
        image_link = product.find('image_link').text
        corrected_link = correct_image_link(image_link)
        product.find('image_link').text = corrected_link

# Exibir o feed XML com as alterações
ET.dump(root)