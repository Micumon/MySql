from typing import Dict


class NewColumns:
    def __init__(self, table_name):
        self.columns: Dict[str, ColumnProperties] = {}
        self.__table = table_name


    def new_column(self, column_name):
        return ColumnProperties(self, column_name)


class ColumnProperties:

    def __init__(self, column_obj, column_name):
        self.__column_obj = column_obj
        self.__column_obj.columns[column_name] = self
        self.column_type = ""
        self.unique = False
        self.primary_k = False
        self.auto_increment = False

    def varchar_type(self, char_number):
        self.column_type = f"varchar({str(char_number)})"
        return self

    def unique_true(self):
        self.unique = True
        return self

    def primary_k_true(self):
        self.primary_k = True
        return self

    def auto_increment_true(self):
        self.auto_increment = True
        return self

    def end_column(self) -> NewColumns:
        return self.__column_obj



