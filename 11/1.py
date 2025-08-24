

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            print("Creating DatabaseConnection...")
            cls._instance = super().__new__(cls)
        else:
            print("Reusing Existing DatabaseConnection...")
        return cls._instance

db1 = DatabaseConnection()
db2 = DatabaseConnection()
db3 = DatabaseConnection()

print(id(db1) == id(db2) == id(db3))




