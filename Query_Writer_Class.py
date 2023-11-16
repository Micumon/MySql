class QueryWriter:

    def __init__(self):
        self.query = ""
        self.__select_statement = ""
        self.from_statement = ""
        self.where_statement = ""
        self.__secondary_select_statement_list = []

    @property
    def select_statement(self):
        return self.__select_statement

    @select_statement.setter
    def select_statement(self, statement):
        if self.__select_statement == "":
            self.__select_statement = statement
        else:
            inner_select_statement = QueryWriter()
            inner_select_statement.select_statement = statement
            self.__secondary_select_statement_list.append(inner_select_statement)

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


