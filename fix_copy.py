import glob
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the legal text in privacy/terms
    content = content.replace('desarrollo inmobiliario "Descubre Mérida con Carlos"', 'desarrollo inmobiliario "Ciudad Central Mérida"')
    content = content.replace('ventas de "Descubre Mérida con Carlos"', 'ventas de "Ciudad Central Mérida"')
    content = content.replace('relacionados con el desarrollo inmobiliario "Descubre Mérida con Carlos"', 'relacionados con el desarrollo inmobiliario "Ciudad Central Mérida"')

    # Fix the contact form text in index.html
    content = content.replace('toda la información sobre Descubre Mérida con Carlos.', 'toda la información sobre Ciudad Central Mérida.')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
