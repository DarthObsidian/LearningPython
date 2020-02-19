
class Table:

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
        pass

    def project(self, *fields):
        pass

    @staticmethod
    def join(tab1, tab2):
        pass
    
    def insert(self, *tup):
        pass
    
    def remove(self, field, val):
        pass

    # Serialization and text backup
    def store(self):
        pass

    @staticmethod
    def restore(fname):
        pass

    @staticmethod
    def read(fname):
        file = open(fname, 'r')
        fileList = file.readlines()
        file.close()
        
        tabName = fileList.pop(0)
        tabCol = tuple(fileList.pop(0).split(','))
        print(tabName, tabCol)
        tups = {tuple(x.split(',')) for x in fileList}

        return Table(tabName, tabCol, tups) 

    def write(self, fname):
        pass