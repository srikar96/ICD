def file_call(word):
    import json
    import pprint

    file = open('../icd_full.json')
    data = json.load(file)

    instructions = data['ICD10CM.tabular']['introduction']
    version = data['ICD10CM.tabular']['version']
    data = data['ICD10CM.tabular']['chapter']
    
    def search(data):
        for val in data:
            if word in val['desc'].lower():
                ls.append(val)
            else:
                if 'diag' in val.keys():
                    search(val['diag'])
        return

    # word = input('Enter search query: ')

    ls = []
    for val in data:
        for part in val['section']:
            if 'diag' in part:
                search(part['diag'])

    # print('Found {} results'.format(len(ls)))
    # pp = pprint.PrettyPrinter()
    # pp.pprint(ls)

    file.close()
    return ls
