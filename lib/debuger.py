import ipdb
from  models.hospital import Hospital
from models.patient import Patient

def reset_database():
    Hospital.drop_table()
    Hospital.create_table()

    belmount = Hospital.create("Bealmount","dearborn","a")


reset_database()
ipdb.set_trace()