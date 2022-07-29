K = 4

def parity(bin_str, indicies):
    # Compute the parity bit for the given string and indicies
    sub = ''
    for i in indicies:
        sub += bin_str[i]
    return str(str.count(sub, '1') % 2)

def hamming(bits):
    # Return given 4 bits plus parity bits for bits (1,2,3), (2,3,4), and (1,3,4)
    t1 = parity(bits, [0,1,3])
    t2 = parity(bits, [0,2,3])
    t3 = parity(bits, [1,2,3])
    return t1 + t2 + bits[0] + t3 + bits[1:]

def encode(s):
    while len(s) >= K: 
        nibble = s[0:K]
        input(hamming(nibble))
        s = s[K:]


if __name__ == "__main__":
    print("Enter Input String of bits - ") #just for testing
    input_string = input().strip()
    print(" Output - ",end=' ') #just for testing
    encode(input_string)