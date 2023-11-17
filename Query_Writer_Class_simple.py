from typing import Dict


class QueryWriter:

    def __init__(self, query=""):
        self.query = query
        self.table_statement: NewColumns

    def __str__(self):
        return self.query

    def __repr__(self):
        return self.query

    def end_of_query(self):
        self.query += ";\n\n"
        return self

    def encode(self, encoding_code):
        return self.query.encode(encoding_code)

    def select_all(self):
        self.query += "SELECT *"
        return self

    def select(self, column_name):
        self.query += f"SELECT {column_name}"
        return self

    def from_st(self, table_name):
        self.query += f" FROM {table_name}"
        return self

    def where(self, where_st):
        self.query += f" WHERE {where_st}"
        return self

    def create_db(self, db_name):
        self.query += f"CREATE DATABASE {db_name}"
        return self

    def create_table(self, table_name):
        return NewColumns(self, table_name)


class NewColumns:
    def __init__(self, writer_obj, table_name=None):
        self.__table_name = table_name
        self.columns: Dict[str, ColumnProperties] = {}
        self.__writer_obj: QueryWriter = writer_obj

    def __build_columns_statement(self):
        statement = f"CREATE TABLE {self.__table_name} (\n"
        for column_name in self.columns:
            statement += f"{column_name} {self.columns[column_name].column_properties},\n"
        statement += ")"
        return statement

    def new_column(self, column_name):
        return ColumnProperties(self, column_name)

    def end_table_creation(self):
        self.__writer_obj.query += f"{self.__build_columns_statement()}"
        return self.__writer_obj


class ColumnProperties:

    def __init__(self, column_obj, column_name):
        self.__column_obj = column_obj
        self.__column_obj.columns[column_name] = self
        self.column_type = ""
        self.unique = False
        self.primary_k = False
        self.auto_increment = False
        self.__column_properties = ""

    @property
    def column_properties(self):
        return self.__column_properties

    @column_properties.getter
    def column_properties(self):
        statement = ""
        if self.column_type != "":
            statement += f"{self.column_type}"
        if self.unique:
            statement += " UNIQUE"
        if self.primary_k:
            statement += " PRIMARY KEY"
        if self.auto_increment:
            statement += " AUTO_INCREMENT"

        return statement

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

