from . import CURSOR,CONN


class Hospital:
    all = {}

    def __init__(self,name,city,id=None):
        self.name = name
        self.city = city
        self.id = id
    
    def __repr__(self):
        return f"<Hospital {self.id}: {self.name}, {self.city}"
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value,str) or not (1<= len(value)<= 20):
            raise ValueError("Name must be 1-20 char ")
        self._name = value

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self,value):
        if not isinstance(value,str) or len(value) == 0:
            raise ValueError("City must not be empty")
        self._city = value

    @classmethod
    def create_table(cls):
        sql ="""
            CREATE TABLE IF NOT EXISTS hospitals(
            id INTEGER PRIMARY KEY,
            name TEXT,
            city TEXT)
        """
         
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS hospitals;
    """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO hospitals(name,city)
            VALUES(?,?)
        """
        CURSOR.execute(sql,(self.name,self.city))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls,name,city):
        hospital = cls(name,city)
        hospital.save()
        return hospital
    
    def delete(self):
        sql = """
            DELETE FROM hospitals 
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def instance_from_db(cls,row):
        hospital = cls.all.get(row[0])
        if hospital:
            hospital.name = row[1]
            hospital.city = row[2]
        else:
            hospital = cls(row[1],row[2])
            hospital.id = row[0]
            cls.all[hospital.id] = hospital
        return hospital

    @classmethod 
    def get_all(cls):
        sql = """
            SELECT * 
            FROM hospitals
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls,id):
        
        sql = """
           SELECT *
           FROM hospitals
           WHERE id = ?
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod 
    def find_by_name(cls,name):

        sql = """
            SELECT *
            FROM hospitals
            WHERE name =  ?
        """
        row = CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    def patients(self):
        from models.patient import Patient
        sql = """
            SELECT * FROM patients
            WHERE hospital_id = ?
        """

        CURSOR.execute(sql,(self.id,))
        rows = CURSOR.fetchall()
        return [Patient.instance_from_db(row) for row in rows]