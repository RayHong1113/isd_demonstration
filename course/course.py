from course.department import Department

class Course():

    def __init__(
            self,
            name: str,
            department: Department,
            credit_hours: int): 
        """Represents a course at an education institution"""

        if len(name.strip()) == 0:
            raise ValueError("name cannot be an empty string")

        # if isinstance(credit_hours, int):
        #     if credit_hours <= 0:
        #         raise ValueError("credit_hours must be a value greater than zero")
           
                 
        self.credit_hours = credit_hours # call the setter directly

        self.__name = name 
        self.__department = department
       

    @property
    def name(self) -> str:
        """Gets the name of the course

            Returns:
                str: The name of the course
        
        """
        return self.__name

    @property
    def department(self)->int:
        return self.__department

    @property
    def credit_hours(self)-> int:
        return self.__credit_hours

    @credit_hours.setter
    def credit_hours(self,credit_hours:int) -> None:
        if credit_hours <= 0:
            raise ValueError("credit_hours must be a value greater than zero") 
        self.__credit_hours = credit_hours


    def __str__(self)->str:
        return (f"Course: {self.__name.title()}\n"
                f"Department: {self.__department.name.replace('_',' ').title()}\n"
                f"Credit Hours: {self.__credit_hours}")



