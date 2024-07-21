
def encrypt(text, key) :
    result = []
    
    for char in text:
        if char.isalpha():              # Got it !
            # Check uppercase/lowercase
            offset = ord('A') if char.isupper() else ord('a')            # ord # IMP_NEW #
            
            shifted_char = chr(offset + (ord(char) - offset + key) % 26)
            result.append(shifted_char)
        
        else:
            result.append(char)
    
    return ''.join(result)          # ???

def decrypt(text, key) :
    return encrypt(text, -key)      # simply, negative key


# key = 27
# plaintext = text = "DEFEND 22 @ defend"

# print ('\n encrypted text:' , encrypt(text, key))
# print ('decrypted text:' , decrypt(text, key))




# Method 2

# # we need 2 helper mappings, from letters to ints and the inverse
# L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
# I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

# # encipher
# ciphertext = ""
# for c in plaintext.upper():
#     if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
#     else: ciphertext += c

# # decipher
# decyptedtext = ""
# for c in ciphertext.upper():
#     if c.isalpha(): decyptedtext += I2L[ (L2I[c] - key)%26 ]
#     else: decyptedtext += c


# print (plaintext)
# print (ciphertext)
# print (decyptedtext)