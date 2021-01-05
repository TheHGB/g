#This is a "complex" Ceaser's cypher and shoud never be used to encrypt sensible data



import sys

def encrypt(x):
    x = str(x)
    enc = []
    for i in range(len(x)):
        enc.append(chr((ord(x[i])+i)%256))
    enc = ''.join(enc)
    return enc

def decrypt(x):
    x = str(x)
    dec = []
    for i in range(len(x)):
        dec.append(chr((ord(x[i])-i)%256))
    dec = ''.join(dec)
    return dec




if __name__ == "__main__":

    if (len(sys.argv) != 3) or (sys.argv[1] != "e" and sys.argv[1] != "d") :
        print "Usage: python  python 04-encrypt-decrypt.py action(e/d) file.txt"
        exit(0)


    with open(sys.argv[2], 'r') as myfile:
      data = myfile.read()
    
    if sys.argv[1] == "e":
        data = encrypt(data)
        print "Saving into encrypted.txt"
        f = open("encrypted.txt", "w")
        f.write(data)
        f.close
        exit(0)

    if sys.argv[1] == "d":
        data = decrypt(data)
        print "Saving into decrypted.txt"
        f = open("decrypted.txt", "w")
        f.write(data)
        f.close
        exit(0)
