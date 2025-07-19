from abc import ABC,abstractmethods

class Doc(ABC):
    def __init__(self,doc_code,imprint,releases):
        self._doc_code = doc_code # ma_tai_lieu
        self._imprint = imprint # ten_nxb
        self._releases = releases # so_ban_phat_hanh

    @property
    def doc_code(self):
        return self._doc_code

    @property
    def imprint(self):
        return self._imprint

    @property
    def releases(self):
        return self._releases

    @abstractmethods
    def show_info(self):
        pass


class Book(Doc):
    def __init__(self, doc_code, imprint, releases, issue, release_month):
        super().__init__(doc_code, imprint, releases)
        self._issue = issue # so_phat_hanh
        self._release_month = release_month # thang_phat_hanh

    def show_info(self):
        print(f"""
Document code: {self._doc_code}

""")

