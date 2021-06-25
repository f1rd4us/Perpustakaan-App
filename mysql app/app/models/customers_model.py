from mysql.connector import connect

class database:
    def __init__(self):
        try:
            self.db = connect(host='localhost', 
            database='perpustakaan', 
            user='root',
            password='B3d3lb0d0l&^*@)!$')
        except Exception as e:
            print(e)

    def showUsers(self):
        try:
            crud_query = '''select * from customers;'''
            cursor = self.db.cursor()
            cursor.execute(crud_query)
            hasil = cursor.fetchall()
            return hasil
        except Exception as e:
            print(e)

    def showUserById(self, **params):
        try:
            cursor = self.db.cursor()
            crud_query = '''select * from customers where userid = {0};'''.format(params["userid"])
            cursor.execute(crud_query)
            hasil = cursor.fetchone()
            return hasil
        except Exception as e:
            print(e)

    def showUserByEmail(self, **params):
        try:
            crud_query = '''select * from customers where email = "{0}";'''.format(params["email"])
            cursor = self.db.cursor()
            cursor.execute(crud_query)
            hasil = cursor.fetchone()
            return hasil
        except Exception as e:
            print(e)

    def insertUser(self, **params):
        try:
            column= ', '.join(list(params['values'].keys()))
            values= tuple(list(params['values'].values()))
            crud_query = '''insert into customers ({0}) values {1};'''.format(column, values)
            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e) 

    def updateUserById(self, **params):
        try:
            userid = params['userid']
            values = self.restructureParams(**params['values'])
            crud_query = '''update customers set {0} where userid = {1};'''.format(values, userid)
            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)

    def deleteUserById(self, **params):
        try:
            userid = params["userid"]
            crud_query = '''delete from customers where userid = {0};'''.format(userid)

            cursor = self.db.cursor()
            cursor.execute(crud_query)
        except Exception as e:
            print(e)
        pass

    def dataCommit(self):
        self.db.commit()

    def restructureParams(self, **data):
        list_data = ["{0} = {1}".format(item[0], item[1]) for item in data.items()]
        result = ', '.join(list_data)
        return result