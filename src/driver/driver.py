

class Driver():
    def __init__(self, surname: str, givenname: str, nationality: str, surname_first: bool = False):
        self.surname = surname
        self.givenname = givenname
        self.nationality = nationality
        self.surname_first = surname_first

    def getNameFormatted(self) -> str:
        '''
        formats the name of the driver as `LAST First` or `First LAST` depending on driver preference
        
        returns:
        str
        '''
        if self.surname_first:
            return f"{self.surname.upper()} {self.givenname}"
        
        return f"{self.givenname} {self.surname.upper()}"