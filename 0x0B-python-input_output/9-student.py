#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """Defining a student profile"""
    def __init__(self, first_name, last_name, age):
        """Initialize Student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return (self.__dict__)
