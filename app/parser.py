def file_call(word):
    import json
    import pprint

    file = open('chap18_all.json')
    data = json.load(file)

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
    for part in data['section']:
        search(part['diag'])

    # print('Found {} results'.format(len(ls)))
    # pp = pprint.PrettyPrinter()
    # pp.pprint(ls)

    file.close()
    return ls
