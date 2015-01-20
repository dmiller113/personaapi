import bs4
import yaml
import sys
import glob


if __name__ == '__main__':
    file = sys.argv[1]
    if file is None:
        print("Please provide a file to convert")
        sys.exit()

    if file == '-g':
        file = glob.glob(sys.argv[2])
    else:
        file = [file]

    for f in file:
        try:
            with open('%s' % f, 'r') as fr:
                soup = bs4.BeautifulSoup(fr.read(), 'xml')
        except:
            print("File not found")
            sys.exit()

        entity_type = soup.find('Arcana')['Name']
        temp = []
        for persona in soup.find_all('Persona'):
            temp.append({
                'name': persona.get('Name'),
                'level': persona.find('Level').text,
                'entity_type': entity_type,
                'strength': persona.find("Stats")['ST'],
                'magic': persona.find("Stats")['MA'],
                'endurance': persona.find("Stats")['EN'],
                'agility': persona.find("Stats")['AG'],
                'luck': persona.find("Stats")['LU']
            })
            print(yaml.dump(temp))

        if f.find('.') != -1 and f.rfind('/') != -1:
            f = f[f.rfind('/')+1:f.rfind('.')]
        elif f.find('.') != -1:
            f = f[:f.rfind('.')]
        else:
            f = f
        with open('personaapi/info/%s.yml' % f, mode='w+') as fw:
            fw.write('---\n' + yaml.dump(temp))
