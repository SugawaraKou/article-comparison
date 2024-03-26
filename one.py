from faker import Faker
import psycopg2
import datetime


class ConnectDB:
    def __init__(self, dbname='fake_data_0', user='test', host='localhost', password='1qw23er4'):
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password

        self.connection = psycopg2.connect(
            database=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )
        self.cursor = self.connection.cursor()

    def execute(self, query):
        try:
            self.cursor.execute(query)
        except Exception as e:
            self.connection = psycopg2.connect(
                database=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host
            )
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
        return False

    def init_to_db(self, data):
        try:
            self.execute(f"""INSERT INTO people VALUES ('{data['job']}', '{data['company']}', '{data['ssn']}', '{data['residence']}', '{data['current_location']}', '{data['blood_group']}', '{data['website']}', '{data['username']}', '{data['name']}', '{data['address']}', '{data['mail']}', '{data['birthdate']}')""")
            self.connection.commit()
        except:
            pass


print('time start:', datetime.datetime.now())

dat_st = datetime.datetime.now().timestamp()
fake = Faker()
db = ConnectDB()

for i in range(0, 1):
    re = fake.profile()
    rec = {}

    rec['job'] = re['job']
    rec['company'] = re['company']
    rec['ssn'] = re['ssn']
    rec['residence'] = re['residence']
    rec['current_location'] = str([float(re['current_location'][0]), float(re['current_location'][1])])
    rec['blood_group'] = re['blood_group']
    rec['website'] = re['website'][0]
    rec['username'] = re['username']
    rec['name'] = re['name']
    rec['address'] = re['address']
    rec['mail'] = re['mail']
    rec['birthdate'] = str(re['birthdate'])
    db.init_to_db(rec)

p = float(datetime.datetime.now().timestamp() - dat_st)
print('time finish:', datetime.datetime.now())
print('time :', p)
print('RPS:', 10000 / p)
