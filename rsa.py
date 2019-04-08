import random
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def modInverse(a, m) :
    m0 = m
    y = 0
    x = 1

    if (m == 1) :
        return 0

    while (a > 1) :

        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t


    # Make x positive
    if (x < 0) :
        x = x + m0

    return x
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2- temp1* x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        return d + phi
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    #Generaing the private key
    d = modInverse(e, phi)
    #Public key is (e, n) and private key is (d, n)
    return ((e,n),(d,n))
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [((ord(char)**key) % int(n)) for char in plaintext]
    return cipher
def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % int(n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    print("RSA Implementation for CARS")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not the one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public,private = generate_keypair(p,q)
    print("Your public key is ", public ," and your private key is ", private)
    f = open("file.txt","r")
    message = f.read()
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    encrypted_str = ''.join(map(lambda x: str(x), encrypted_msg))
    print(encrypted_str)
    print("Decrypting message with public key ", public ," . . .")
    print("Your message is:")
    decrypted_message = decrypt(public, encrypted_msg)
    print(decrypted_message)
    print("Your encrypted file is encryptednew.txt and decrypted file is decryptedbew.txt")
    f = open("encryptednew.txt","w+")
    f.write(encrypted_str)
    f = open("decryptednew.txt","w+")
    f.write(decrypted_message)
