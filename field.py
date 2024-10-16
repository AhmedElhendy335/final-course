from abc import ABC


class field(ABC):
    field_typy = None


    def __init__(self, max_length=255, unique=None):
        if unique is True:
            self.unique = 'UNIQUE'

        else:
            self.unique = ''

        if max_length:
            self.maxlength = max_length


    def __repr__(self):
        column = []
        if self.field_typy == 'VARCHAR':
            column.append(f'Varchar({self.maxlength})')
        else:
            column.append(self.field_typy)
            column.append(self.unique)
        return ''.join(column).strip()

class CharField(field):
    field_typy = 'VARCHAR'

    def __init__(self, max_length=255, unique=None):
        super().__init__(max_length, unique)
        self.maxlength = max_length
        self.unique = unique
        super().__init__(max_length=max_length, unique=unique)

class TextField(field):
    field_typy = 'TEXT'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)

class IntegerField(field):
    field_typy = 'INTEGER'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)    

class FloatField(field):
    field_typy = 'REAL'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class BooleanField(field):
    field_typy = 'Integer'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)


class DateTimeField(field):
    field_typy = 'TIMESTAMP'

    def __init__(self, unique=None):
        self.unique = unique
        super().__init__(unique=unique)