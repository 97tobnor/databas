# -*- coding: utf-8 -*-
"""

@author: 97tobnor
"""

import sqlite3

def query(sql,data):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys ON")
        cursor.execute(sql,data)
        db.commit()
    
    
if __name__ == "__main__":
    sql = "update ProductType set ProductTypeID = 57 where ProductTypeID = 1"
    sql = "delete from ProductType where ProductTypeID = 57"
    query(sql,())