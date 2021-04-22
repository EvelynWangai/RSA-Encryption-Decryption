my_dict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
       'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,
       'y':25,'z':26,' ':27}

decrpt_dict={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',
            17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z',27:' '}

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

p = int(input("Enter a prime number (GIVE SAME NUMBER WHEN YOU RAN THE ENCRYPTION FILE):"))
q = int(input("Enter a second prime number (GIVE SAME NUMBER WHEN YOU RAN THE ENCRYPTION FILE):"))

public,private = generate_key_pair(p,q)


def decryption(key,cipher_text):
    #encry = encry.split(",")
    d, n = key
    new = []
    
       
    for cr in (cipher_text):
        encrptd_msg = (int(cr)**int(d)) % n
        new.append(encrptd_msg)
    return new

def encryption(key,text):
    """
    function: encryption
    
    instruct the user to enter a message
    
    output: encrypted message
    
    """
    e, n=key
    nw =[]
    text = text.lower()
    
    for letter in text:
        value = int(my_dict[letter])
        
        cipher = (value ** e) %n 
        
        nw.append(cipher)
    
    return nw


def origi_msg(msg):
    
    y = []
    for value in msg:
        decrptd_msg = str(decrpt_dict[value])
        
        y.append(decrptd_msg)
        
    return ''.join(y) 

   

message = input("Welcome! What would you like to encrypt today?")
encrptd_msg = encryption(public,message)
print("Your encrypted message is:",encrptd_msg)

#command = input("The encrypted message is", encryption(message))
print("We will now decrypt your encrypted message, using the private key",private)

decrptd_msg = decryption(private,encrptd_msg)
print("The decryption translation is:",decrptd_msg)

print("The original message is:", origi_msg(decrptd_msg))

print("YOU DID IT. YOU FINALLY BROKE THE CODE")