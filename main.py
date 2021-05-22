import lib as lib
import sqlite3
con = sqlite3.connect('database.db')

"""" CHANGE COLUMNS HERE THAT YOU NEED TO ENCRYPT"""
TABLE_NAME = 'ultimate_dictionary'
ID_COLUMN_NAME = 'id'
COLUMNS = [
    'bn_synonym',
    'en_meaning',
    'en_synonym',
    'antonym',
    'bn_details',
    'example',
    'gm_details'
    ]

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con.row_factory = dict_factory
cur = con.cursor()

query = "SELECT "+ID_COLUMN_NAME+", "+', '.join(COLUMNS)+" FROM "+TABLE_NAME

for row in cur.execute(query):
        print('WORKING ON {}'.format(row['id']))
        for cname in COLUMNS:
            if (row[cname]) != None:
                cursor = con.cursor()
                cursor.execute(
                    '''UPDATE `{}`
                    SET "{}"="{}"
                    WHERE {} = {}
                   '''.format(
                        TABLE_NAME,
                        cname,
                        lib.encryptText(row[cname]).decode('utf-8'),
                        ID_COLUMN_NAME,
                        row[ID_COLUMN_NAME]
                        )
                )

con.commit()