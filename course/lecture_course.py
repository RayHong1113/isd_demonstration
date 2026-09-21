from course.course import Course
from course.department import Department

class LectureCourse(Course):
    """"This class represents a LectureCourse."""

    def __init__(self, 
                 name: str,
                 department:Department, 
                 credit_hours: int, 
                 lecture_hall: str) -> None:
        """"Initializes a new instance of LectureCourse
        
            Args:
                name(str) : The name of the course
                departmnent (Department) : The department the course is delivered by
                credit_hours (int) : The number of credit hours
                lecture_hall (str) : The hall the course is being taught in.

                Raises:
                    ValueError: Raised when 
                        - the name contains no no-white characters
                        - the credit_hours value is less than or equal to zero
                        - the lecture_hall contains no non-whitespace characters.
        """
        super().__init__(name, department, credit_hours)

        lecture_hall = lecture_hall.strip()

        if lecture_hall == "":
            raise ValueError("lecture_hall cannot be an empty string")

        self.__lecture_hall = lecture_hall

