from New_Columns_classes import NewColumns

columns_writer = NewColumns()

columns_query = columns_writer.new_column("name").varchar_type(40).end_column().new_column("last").varchar_type(50)\
    .end_column().new_column("ale").varchar_type(50).end_column().new_column("tata").varchar_type(60).end_column()\
    .new_column("marmolada").end_column().

print(columns_writer.columns["name"].column_type)
print(columns_writer.columns["last"].column_type)
print(columns_query.columns)