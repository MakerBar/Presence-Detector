import pickle

def build_dict():
    d = dict()
    d['E4:CE:8F:24:B5:58'] = 'Bert' # laptop (wireless)
    d['00:23:76:99:9C:AF'] = 'Bert' # phone
    return d

if __name__ == '__main__':
    pickle.dump(build_dict(), open('macs.pckl', 'w'))
