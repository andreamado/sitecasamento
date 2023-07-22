from os import system, remove

navbaritems = [
    {
        'pt': ['Home', 'index'],
        'en': ['Home', 'index_en'],
        'disabled': False
    },{
        'pt': ['A nossa história (brevemente!)', 'historia'],
        'en': ['Our story (coming soon!)', 'story'],
        'disabled': True
    },{
        'pt': ['Como chegar', 'comochegar'],
        'en': ['How do I get there?', 'howdoigetthere'],
        'disabled': False
    },{
        'pt': ['Outras informações', 'outrasinformacoes'],
        'en': ['Other info', 'otherinfo'],
        'disabled': False
    },{
        'pt': ['Fotos (a seguir ao casamento)', 'fotos'],
        'en': ['Photos (after the wedding)', 'photos'],
        'disabled': True
    },{
        'pt': ['Contacto', 'contacto'],
        'en': ['Talk to us', 'contact'],
        'disabled': False
    }
]

def generate_json(item, language):
    with open(f'{folder}data.json', 'w', encoding="utf-8") as f:
        f.write('{\n')

        # navbar
        f.write('    "navbar-items": [\n')
        for i, navitem in enumerate(navbaritems):
            active = 'true' if navitem == item else 'false'
            disabled = 'true' if navitem['disabled'] else 'false'
            link = '#' if navitem == item else navitem[language][1] + '.html'

            f.write( '            {\n')
            f.write(f'                "name": "{navitem[language][0]}",\n')
            f.write(f'                "active": {active},\n')
            f.write(f'                "disabled": {disabled},\n')
            f.write(f'                "link": "{link}"\n')
            if i != len(navbaritems) - 1:
                f.write( '            },\n')
            else:
                f.write( '            }\n')
        f.write('    ],\n')
        # end navbar

        # language menu
        f.write( '    "languages": [\n')

        active = 'true' if language == 'pt' else 'false'
        link = '#' if language == 'pt' else item['pt'][1] + '.html'
        f.write( '        {\n')
        f.write( '            "name": "Português",\n')
        f.write(f'            "active": {active},\n')
        f.write(f'            "link": "{link}"\n')
        f.write( '        },\n')

        active = 'true' if language == 'en' else 'false'
        link = '#' if language == 'en' else item['en'][1] + '.html'
        f.write( '        {\n')
        f.write( '            "name": "English",\n')
        f.write(f'            "active": {active},\n')
        f.write(f'            "link": "{link}"\n')
        f.write( '        }\n')

        f.write('    ]\n')
        # end language menu

        f.write('}')

# folder containing the mustache templates
folder = 'mustache/'

for item in navbaritems:
    for language in ['pt', 'en']:
        if not item['disabled']:
            generate_json(item, language)

            basename = item[language][1]
            system(f'mustache -p {folder}navbar.mustache {folder}data.json {folder}{basename}.html > {basename}.html')

remove(f'{folder}data.json')