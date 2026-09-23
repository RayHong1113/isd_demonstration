"""This module defines a Lecture Course"""

from course.course import Course
from course.department import Department
from course.student import Student

class LectureCourse(Course, object):
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


    @property
    def lecture_hall(self) -> str:
        """Gets the lecture hall that the course is offered in
        
            Returns:
                str: the lecture hall
        """
        return self.__lecture_hall

    def enroll_student(self, student: Student) -> None:
        """Enrolls a student in a course
        
            Args:
                student (Student) : represent the student in the course.    
        """
        buffer = int(Course.ENROLLMENT_LIMIT * .1)
        if len(self.students) >= Course.ENROLLMENT_LIMIT + buffer:
            raise ValueError("Cannot enroll student; course at capacity")

        self.__students.append(student)

    def __str__(self) -> str:
        """Return the string representation of this this object: LectureCourse
        
            Returns:
                str: the string representation of lectureCourse
        
        """ 
        return (f"{super().str()}\n"
                f"Lecture Hall: {self.lecture_hall}")
        
