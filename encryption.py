# library to be imported
import math

# creating my ditionary

my_dict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
       'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,
       'y':25,'z':26,' ':27}

## Creating RSA keys and encrypting a message
def generate_key_pair(p,q):
    """
    function: generate 2 prime numbers
    
    input: 2 prime numbers, phi, a random integer i, e
    
    output: public key and private key
    
    """
    n = p * q
    
    phi = (p-1) * (q-1)
    
    e = 5
    
    i = 2
    d = int((i * phi + 1)/e)
    
    
    
    return ((e,n), (d,n))
 
p = int(input("Enter a prime number:"))
q = int(input("Enter a second prime number:"))

public,private = generate_key_pair(p,q)

print("Your public key is:", public,"and your private key is:",private)

def encryption(key,text):
    """
    function: encryption
    
    instruct the user to enter a message
    
    output: encrypted message
    
    """
    e, n=key
    nw =[]
    text = text.lower() # converts the text to lowercase
    
    for letter in text:
        value = int(my_dict[letter])
        
        cipher = (value ** e) %n # formula to calculate the cipher
        
        nw.append(cipher)
    
    return nw

message = input("Welcome! What would you like to encrypt today?")
print("Your encrypted message is:",encryption(public,message))
