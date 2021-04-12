import csv
import copy
import operator
import functools

class Table:
    def __init__(self, filename=None, setTypes=False):
        self.filename = filename
        self.data = self.load_table(filename) if filename else []
        if setTypes:
            self.tableSetType()

    def load_table(self, filename):
        self.filename = filename
        return [fields for fields in csv.reader(open(filename, newline=''), delimiter=";")]

    def save_table(self, filename):
        csv.writer(open(filename, "w", newline=''), delimiter=";").writerows(self.data)

    def __str__(self):
        return str(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        print(stop)
        if stop is None:
            stop = len(self.data)

        return copy.deepcopy(self.data[start:stop]) if copy_table else self.data[start:stop]

    def get_rows_by_index(self, vals, copy_table=False):
        result = []

        for val in vals:
            for row in self.data:
                if row[0] == val:
                    result.append(row)

        return copy.deepcopy(result) if copy_table else result

    def get_column_types(self, by_number=True):
        result = {}

        for i in range(len(self.data[0])):
            try:
                columnType = self.getType(self.data[1][i])
            except IndexError:
                print("Error: в таблице нет данных")
                break

            if by_number:
                result[i] = columnType
            else:
                result[self.data[0][i]] = columnType

        return result

    def getType(self, val):
        columnType = None
        try:
            if not (val == "False" or val == "True"):
                raise TypeError()
            columnType = "bool"
        except:
            try:
                int(val)
                columnType = "int"
            except:
                try:
                    float(val)
                    columnType = "float"
                except:
                    columnType = "str"

        return columnType

    def setType(self, typeName, val):

        return {"bool": bool,
                "int": int,
                "float": float,
                "str": str}[typeName](val)

    def tableSetType(self):
        for j in range(len(self.data[0])):

            try:
                columnType = self.getType(self.data[1][j])
            except IndexError:
                print("Error: в таблице нет данных")
                break

            for i in range(1, len(self.data)):
                self.data[i][j] = self.setType(columnType, self.data[i][j])

    def get_values(self, column=0):
        if isinstance(column, str):
            column = self.data[0].index(column)

        result = []
        try:
            columnType = self.getType(self.data[1][column])
        except IndexError:
            print("Error: в таблице нет данных")
            return result

        for row in range(1, len(self.data)):
            result.append(self.setType(columnType, self.data[row][column]))

        return result

    def get_value(self, column=0):
        try:
            return self.get_values(column)[0]
        except IndexError:
            print("Error: в таблице нет данных")
            return []

    def set_values(self, values, column=0):
        if isinstance(column, str):
            column = self.data[0].index(column)

        minrows = min(len(values), len(self.data) - 1)

        for i in range(minrows):
            self.data[i + 1][column] = values[i]

    def set_value(self, value, column=0):
        if isinstance(column, str):
            column = self.data[0].index(column)

        if len(self.data) - 1:
            self.data[1][column] = value

    def print_table(self):
        print(self)

    def execute(self,command,column,start, stop=None):
        if isinstance(column, str):
            column = self.data[0].index(column)

        if stop is None:
            stop = len(self.data)

        try:
            data = [row[column] for row in self.data[start:stop]]
            if not data:
                raise (IndexError)
        except IndexError:
            print("Error: в таблице нет данных")
            return None

        return functools.reduce(*{"mul": (operator.mul, data, 1),
                                  "add": (operator.add, data),
                                  "sub": (operator.sub, data),
                                  "div": (operator.floordiv, data)}[command])

    def filter_rows(self,command,value,column,start, stop=None,copy_table=False):
        if isinstance(column, str):
            column = self.data[0].index(column)

        if stop is None:
            stop = len(self.data)

        operators ={"eq":operator.eq,"ne":operator.ne,"gt":operator.gt, "lt":operator.lt, "ge":operator.ge,"le":operator.le}
        rows = []
        rows.append(copy.deepcopy(self.data[0]) if copy_table else self.data[0])
        for row in self.data[start:stop]:
            if operators[command](row[column],value):
                rows.append(copy.deepcopy(row) if copy_table else row)

        return rows