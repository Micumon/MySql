class QueryWriter:

    def __init__(self, query=""):
        self.query = query

    def __str__(self):
        return self.query

    def __repr__(self):
        return self.query

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

    def create_table(self, table_name, new_columns):
        statement = f"CREATE TABLE {table_name} ("


        return self



