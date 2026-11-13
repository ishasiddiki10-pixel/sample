def bincon(data):
    return ''.join((ord(char), '08b') for char in data)
def crccal(data, poly):
    n = len(poly) - 1
    rem = list(data + '0' * n)
    for i in range(len(data)):
        if rem[i] == '1':
            for j in range(len(poly)):
                rem[i + j] = str(int(rem[i + j]) ^ int(poly[j]))
    return ''.join(rem[-n : ])
def crcver(data, poly):
    rem = list(data)
    for i in range(len(data) - len(poly) + 1):
        if rem[i] == '1':
            for j in range(len(poly)):
                rem[i + j] = str(int(rem[i + j]) ^ int(poly[j]))
    return ''.join(rem[-(len(poly) - 1) : ])
data = '110101101011'
poly = '1100000001111'
crc = crccal(data, poly)
rec = crcver(data + crc, poly)
if '1' not in rec:
    print("No error detected")
else:
    print("Error detected")
    
100000111
1100000001111
11000000000000101
10001000000100001