FLAG = 0x7E
ESC = 0x7D

def sender(data):
    result = []
    for b in data:
        if b == FLAG or b == ESC:
            result.append(ESC)
            result.append(b ^ 0x20)
        else:
            result.append(b)
    return result
    
def receiver(data):
    result = []
    i = 0
    while i < len(data):
        if data[i] == ESC:
            if i + 1 > len(data):
                print("Invalid ESC at the end")
            i += 1
            result.append(data[i] ^ 0x20)
        else:
            result.append(data[i])
        i += 1
    return result
    
data = [67, 126, 68, 125, 79]
stuffed = sender(data)
received = receiver(stuffed)
print("Original : ", data)
print("Stuffed data : ", stuffed)
print("Received data : ", received)