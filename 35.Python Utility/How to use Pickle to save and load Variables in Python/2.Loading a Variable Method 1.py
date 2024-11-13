import pickle

# This is the result of previous code
binary_string = b'\x80\x04\x95K\x00\x00\x00\x00\x00\x00\x00]\x94(}\x94(\x8c\x04This\x94\x8c\x02is\x94\x8c\x07Example\x94K\x01u\x8c\x02of\x94\x8c\rserialisation\x94]\x94(\x8c\x05using\x94\x8c\x06pickle\x94ee.'

# Use loads to load the variable
myvar = pickle.loads(binary_string)

print(myvar)
