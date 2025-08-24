

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._logged = ""

    def log(self,info):
        self._logged += f"{info}\n"

    def show(self):
        print(self._logged)

log1 = Logger()
log2 = Logger()
log1.log("Chương trình bắt đầu")
log2.log("Lỗi: Không tìm thấy file")

log1.show()


#results:

# Chương trình bắt đầu
# Lỗi: Không tìm thấy file



