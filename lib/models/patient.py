from . import CURSOR, CONN
from models.hospital import Hospital



class Patient:
    all = {}
    def __init__(self,name,age,illness,hospital_id,id=None):
        self.name = name
        self.age = age
        self.illness = illness
        self.hospital_id =  hospital_id
        self.id = id

    def __repr__(self):
        return(
            f"Patient{self.id} : {self.name}, {self.age}, {self.illness}>"+
            f"<Hospital ID: {self.hospital_id}>"
        )
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value,str) or len(value) == 0:
            raise ValueError("Name must not be empty")
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        if not isinstance(value,int) or value > 120:
            raise ValueError("Age must be a realistic number")
        self._age = value

    @property
    def illness(self):
        return self._illness
    
    @illness.setter
    def illness(self,value):
        if not isinstance(value,str) or len(value) == 0:
            raise ValueError("The illness entered should not be empty")
        self._illness = value
    
    @property
    def hospital_id(self):
        return self._hospital_id
    
    @hospital_id.setter
    def hospital_id(self,value):
        if type(value) is int and Hospital.find_by_id(value):
            self._hospital_id = value
        else:
            raise ValueError("must refernce a current hospital")
        
    @classmethod
    def create_table(cls):
        sql = """
             CREATE TABLE IF NOT EXISTS patients(
             id INTEGER PRIMARY KEY,
             name TEXT,
             age TEXT,
             illness TEXT,
             hospital_id INTEGER,
             FOREIGN KEY (hospital_id) REFERENCES hospitals(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS patients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO patients (name, age, illness,hospital_id)
                VALUES (?, ?, ?,?)
        """

        CURSOR.execute(sql, (self.name, self.age, self.illness,self.hospital_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):
        sql= """
            DELETE FROM patients
            WHERE id = ?
        """

        CURSOR.execute(sql,(self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
    def update(self):
        sql = """
             UPDATE patients
             SET name = ?, age = ? , illness = ?, hospital_id = ?
             WHERE id = ?
        """
        CURSOR.execute(sql,(self.name,self.age,self.illness,self.hospital_id,self.id))
        CONN.commit()

    @classmethod
    def create(cls,name,age,illness,hospital_id):
        patient = cls(name,age,illness,hospital_id)
        patient.save()
        return patient
    
    @classmethod
    def instance_from_db(cls,row):
        patient = cls.all.get(row[0])

        if patient:
            patient.name = row[1]
            patient.age= int(row[2])
            patient.illness = row[3]
            patient.hospital_id = row[4]
        else:
            patient = cls(row[1],int(row[2]),row[3],row[4])
            patient.id = row[0]
            cls.all[patient.id] = patient
        return patient
    
    @classmethod 
    def get_all(cls):
        
        sql =  """
            SELECT * 
            FROM patients
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT *
            FROM patients
            WHERE id = ?
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod 
    def find_by_name(cls,name):
        sql = """
            SELECT * 
            FROM patients
            WHERE name = ?
        """
        row = CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None
