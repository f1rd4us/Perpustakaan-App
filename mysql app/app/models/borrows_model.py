from mysql.connector import connect

class database():
    def __init__(self):
        try:
            self.db = connect(host='localhost', 
            database='perpustakaan', 
            user='root',
            password='B3d3lb0d0l&^*@)!$')
        except Exception as e:
            print(e)
    
    def showBorrowByEmail(self, **params):
        cursor = self.db.cursor()
        query = '''
        select customers.username, borrows.* 
        from borrows
        inner join customers on borrows.userid = customers.userid
        where customers.email = "{0}" and borrows.isactive = 1;
        '''.format(params['email'])
        cursor.execute(query)
        result = cursor.fetchall()
        return result 

    def insertBorrow(self, **params):
        column = ', '.join(list(params.keys()))
        values = tuple(list(params.values()))
        cursor = self.db.cursor()
        query = '''
        insert into borrows ({0})
        value {1};
        '''.format(column, values)
        cursor.execute(query)


    def updateBorrow(self, **params):
        borrowid = params['borrowid']
        cursor = self.db.cursor()
        query = '''
        update borrows
        set isactive = 0
        where borrowid = {0};
        '''.format(borrowid)
        cursor.execute(query)

    def dataCommit(self):
        self.db.commit()

