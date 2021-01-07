from flask_table import Table, Col



class LibTable(Table):
    code = Col('code' )
    name = Col('description')
    adress = Col('adress')
