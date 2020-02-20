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
        if field in self.fields:
            newTup = {item for item in self.tups if val in item}
            return Table('result', self.fields, newTup)
        pass

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
        pass
    
    def insert(self, *tup):
        pass
    
    def remove(self, field, val):
        pass

    # Serialization and text backup
    def store(self):
        file = open(f'{self.name}.db', 'wb')
        pickle.dump(self, file)
        file.close()

    @staticmethod
    def restore(fname):
        with open(f'{fname}', 'rb') as file:
            table = pickle.load(file)
        
        pass

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
