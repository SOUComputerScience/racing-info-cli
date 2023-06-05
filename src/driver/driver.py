

class Driver():
    """
    TODO
    """
    def __init__(self, surname: str, givenname: str, number: int, nationality: str, surname_first: bool = False):
        # type checking

        if not isinstance(surname, str):
            raise TypeError(f"") # TODO
        if not isinstance(givenname, str):
            raise TypeError(f"") # TODO
        if not isinstance(number, int):
            raise TypeError(f"") # TODO
        if not isinstance(nationality, str):
            raise TypeError(f"") # TODO
        if not isinstance(surname_first, bool):
            raise TypeError(f"") # TODO
        
        self.surname = surname
        self.givenname = givenname
        self.number = number
        self.nationality = nationality
        self.surname_first = surname_first

    def getNameFormatted(self) -> str:
        '''
        formats the name of the driver as `LAST First` or `First LAST` depending on driver preference
        
        returns:
        str
        '''
        if self.surname_first:
            return f"{self.surname.upper()} {self.givenname} #{self.number}"
        
        return f"{self.givenname} {self.surname.upper()} #{self.number}"