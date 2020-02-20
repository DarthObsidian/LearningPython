import pickle

class Table:

    __slots__ = ['__name', '__fields', '__tups']
    def __init__(self, name='', fields=tuple(), tups=None):
        self.__name = name
        self.__fields = fields
        self.__tups = tups

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def fields(self):
        return self.__fields

    @property
    def tups(self):
        return self.__tups

    # Relational operations:
    def select(self, field, val):
        newTup = {item for item in self.tups if val in item}
        return Table('result', self.fields, newTup)

    def project(self, *fields):
        i = 0
        indexies = list()
        while i < len(self.fields):
            if self.fields[i] in fields:
                indexies.append(i)
            i += 1

        newTups = {tuple([item[index] for index in indexies]) for item in self.tups}

        return Table('result', fields, newTups)

    @staticmethod
    def join(tab1, tab2):
        i = 0
        while i < len(tab1.fields):
            if tab1.fields[i] in tab2.fields:
                commonInd1 = i
                break
            i += 1

        newField = tab1.fields + tuple([item for item in tab2.fields if item not in tab1.fields])
        
        newTups = set()
        for tupe in tab1.tups:
            for tupe2 in tab2.tups:
                if tupe[commonInd1] in tupe2:
                    newTups.add(tupe + tuple([thing for thing in tupe2 if thing not in tupe]))

        return Table('result', newField, newTups)
    
    def insert(self, *tup):
        if len(tup) == len(self.fields):
            self.tups.add(tup)
    
    def remove(self, field, val):
        itemsToRemove = {item for item in self.tups if val in item}

        for tupe in itemsToRemove:
            self.tups.remove(tupe)

    # Serialization and text backup
    def store(self):
        with open(f'{self.name}.db', 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def restore(fname):
        with open(f'{fname}', 'rb') as file:
            return pickle.load(file)
        
        
    @staticmethod
    def read(fname):
        file = open(fname, 'r')
        fileList = file.read().splitlines()
        file.close()
        
        tabName = fileList.pop(0).strip()
        tabCol = tuple([item for item in fileList.pop(0).split(',')])
        tabTups = {tuple(x.split(',')) for x in fileList}

        return Table(tabName, tabCol, tabTups)

    def write(self, fname):
        result = f"{self.name}\n{','.join(self.fields)}\n"
        for item in self.tups:
            result += f"{','.join(item)}\n"
        file = open(fname, 'w')
        file.write(result)
        file.close()

    #magic methods
    def __str__(self):
        underline = '=' * len(self.name)
        result = f"{self.name}{self.fields}\n{underline}\n"
        for item in self.tups:
            result += str(item) + '\n'
        return result
