import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_sertificate(self, nomer, url, ism_familiya, kurs_nomi, kurs_soati, upload_link, sana):
        self.cur.execute("""insert into mainapp_sertificate(nomer, url, ism_familiya, 
        kurs_nomi, kurs_soati, upload_link, sana) values (?, ?, ?, ?, ?, ?, ?)""",
                         (nomer, url, ism_familiya, kurs_nomi, kurs_soati, upload_link, sana))
        self.conn.commit()

    def get_nomers(self):
        self.cur.execute("""SELECT nomer FROM mainapp_sertificate""")
        sertificates = dict_fetchall(self.cur)
        return sertificates

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))