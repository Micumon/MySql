class NewColumns:

    def __init__(self):
        self.columns = {}

    def new_column(self, column_name):
        self.columns[column_name] = ColumnProperties(self)
        return ColumnProperties(self)


class ColumnProperties:

    def __init__(self, column_obj):
        self.__column_obj = column_obj
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



