import random
small="abcdefghijkl"
caps="ABCDEFGHIJKL"
symbo="+_)(*&^%$#@!"
number="1234567890"
pass_symbols=small+caps+symbo+number
pass_length=8
random_pass="".join(random.sample(pass_symbols,pass_length))
print(random_pass)