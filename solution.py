import xml.etree.ElementTree as ET

xml_data = ET.parse('feed_psel.xml')
root = tree.getroot()

def remover_produtos_fora_de_estoque(root):
    for item in root.findall('item'):
        availability = item.find('availability').text
        if "Fora de estoque" in availability:
            root.remove(item)

def adicionar_cor_aos_produtos(root):
    for item in root.findall('item'):
        id = item.find('id').text
        color = item.find('color')
        title = item.find('title').text
        if color.text == 'null':
            cor = title.split('-')[-1].strip().strip('"')
            color.text = cor

def corrigir_links_imagens(root):
    for item in root.findall('item'):
        id = item.find('id').text
        image_link = item.find('image_link')
        if ".mp3" in image_link.text:
            image_link.text = image_link.text.replace('.mp3', '.jpg')

remover_produtos_fora_de_estoque(root)
adicionar_cor_aos_produtos(root)
corrigir_links_imagens(root)

ET.dump(root)
