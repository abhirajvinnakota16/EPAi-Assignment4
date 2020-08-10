import random
import decimal
from decimal import Decimal

class Qualean(int):

    def __new__(Qualean, real_value):

        if real_value not in (-1,0,1):
            raise Exception("Sorry, enter a value between -1, 0, 1")

        return int.__new__(Qualean, real_value)

    def __init__(self, real_value):

        if type(real_value) is str:
            if real_value == 'True':
                real_value = 1
            elif real_value == 'False':
                real_value = 0
            elif real_value == 'Maybe':
                real_value = -1

        self.real_value = Decimal(real_value)
        decimal.getcontext().prec = 10

        self.random_num = Decimal(str(random.uniform(-1,1)))
        self.f_value = self.real_value * self.random_num

    def __and__(self, other):
        if isinstance(other, Qualean):
            return self.f_value and other.f_value
        else:
             return False

    def __or__(self, other):
        if isinstance(other, Qualean):
            return self.f_value or other.f_value
        else:
            return False

    def __repr__(self):
        return str(self.f_value)

    def __str__(self):
        return   "ObjectType: Qualean, State : " + ['False','True','Maybe'][int(self.real_value)] + ', Value: ' + str(self.f_value)

    def __add__(self, other):
        if isinstance(other, Qualean):
            return self.f_value + other.f_value
        elif isinstance(other, Decimal):
            return self.f_value + other
        else:
            raise ValueError("Object not a Qualean")

    def __eq__(self, other):
        if isinstance(other, Qualean):
            return self.f_value == other.f_value
        elif isinstance(other, bool):
            return self.__bool__() == other
        else:
            raise TypeError("'==' only supported between Qualean instances ")

    def __float__(self):
        return float(self.f_value)

    def __ge__(self, other):
        if isinstance(other, Qualean):
            return self.f_value >= other.f_value
        else:
            raise TypeError("'>=' only supported between Qualean instances ")
        return self.f_value >= other.f_value

    def __gt__(self, other):
        if isinstance(other, Qualean):
            return self.f_value > other.f_value
        else:
            raise TypeError("'>' only supported between Qualean instances ")

    def __invertsign__(self):
        return (self.f_value.copy_negate())

    def __le__(self, other):
        if isinstance(other, Qualean):
            return self.f_value <= other.f_value
        else:
            raise TypeError("'<=' only supported between Qualean instances ")


    def __lt__(self, other):
        if isinstance(other, Qualean):
            return self.f_value < other.f_value
        else:
            raise TypeError("'<' only supported between Qualean instances ")
        

    def __mul__(self, other):
        if isinstance(other, Qualean):
            return self.f_value * other.f_value
        else:
            raise ValueError("Object not a Qualean")

    def __sqrt__(self):
        if self.f_value < 0:
            temp = abs(self.f_value).sqrt()
            return complex(0, temp)
        else:
            return self.f_value.sqrt()

    def __bool__(self):
        return self.real_value != 0