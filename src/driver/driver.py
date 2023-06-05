

class Driver():
    """
    a class to represent a driver
    """
    def __init__(self, surname: str, givenname: str, number: int, nationality: str, surname_first: bool = False):
        
        # type checking

        if not isinstance(surname, str):
            raise TypeError(f"{surname} must be of type str, not {type(surname)}")
        if not isinstance(givenname, str):
            raise TypeError(f"{givenname} must be of type str, not {type(givenname)}")
        if not isinstance(number, int):
            raise TypeError(f"{number} must be of type int, not {type(number)}")
        if not isinstance(nationality, str):
            raise TypeError(f"{nationality} must be of type str, not {type(nationality)}")
        if not isinstance(surname_first, bool):
            raise TypeError(f"{surname_first} must be of type bool, not {type(surname_first)}")
        
        self.surname = surname
        self.givenname = givenname
        self.number = number
        self.nationality = nationality
        self.surname_first = surname_first

    def __str__(self) -> str:
        '''
        formats the name of the driver as `LAST First` or `First LAST` depending on driver preference
        
        returns:
        str
        '''
        if self.surname_first:
            return f"{self.surname.upper()} {self.givenname} #{self.number}"
        
        return f"{self.givenname} {self.surname.upper()} #{self.number}"