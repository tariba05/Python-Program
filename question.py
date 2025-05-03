# Purpose: to create a class with accessors mutators and string representation
# Author: Areesha Tariq
# 12/11/2023

class Question:
    def __init__(self, question, opt1, opt2, opt3, opt4, answer):   # initializer with parameters
        self.__question = question
        self.__opt1 = opt1
        self.__opt2 = opt2 
        self.__opt3 = opt3
        self.__opt4 = opt4
        self.__answer = answer

    def get_question (self):                # accessors
        return self.__question
    def get_opt1 (self):
        return self.__opt1
    def get_opt2 (self):
        return self.__opt2
    def get_opt3 (self):
        return self.__opt3
    def get_opt4 (self):
        return self.__opt4
    def get_answer (self):
        return self.__answer

    def set_question(self, question):       # mutators
        self.__question = question
    def set_opt1(self, opt1):
        self.__opt1 = opt1
    def set_opt2 (self, opt2):
        self.__opt2 = opt2
    def set_opt3 (self, opt3):
        self.__opt3 = opt3
    def set_opt4 (self, opt4):
        self.__opt4 = opt4
    def set_answer (self, answer):
        self.__answer = answer

                                            # string representation

    def __str__(self):
        return f"{self.__question}\n1. {self.__opt1}\n2. {self.__opt2}\n3. {self.__opt3}\n4. {self.__opt4}\n"
    
    
