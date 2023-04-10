from dataclasses import dataclass

from dataclasses import fields
@dataclass
class Number:
    val:int
    val2:int
    val3:int
    val4:int

a=fields(Number)
print(a)
print(1)