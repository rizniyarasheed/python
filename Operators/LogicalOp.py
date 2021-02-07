# &,|,^

#rule of & is if one end is false entire term bocome false

print( True&True)
print(False&False)
print(True&False)
print(2&4) #0010*0100=0000-->0
print(2&8)

#rule of | is if one end is true entire term become true

print( True|True)
print(False|False)
print(True|False)
print(2|4)
print(2|8)

#rule of ^ is if both  end are same bit it will be return false
#rule of ^ is if both  end are different bit it will be return true

print( True^True)
print(False^False)
print(True^False)
print(2^4)
print(2^8)