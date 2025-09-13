


class Book:
    def __init__(self, title:str, author:str, year:str):
        self._title = title
        self._author = author
        self.year = year

    @property
    def title(self) -> str:
        return self._title
    @property
    def author(self) -> str:
        return self._author

    @property
    def year(self) -> str:
        return self._year if hasattr(self,"_year") else None
    @year.setter
    def year(self,value):
        try:
            int(value)
            if len(value) > 4:
                raise ValueError("Year must be 4 digits or lower.")
            self._year = value
        except ValueError:
            raise ValueError("Year must be 4 digits or lower.")


    def __str__(self) -> str:
        return f"{self._title} - {self._author} ({self._year})"


