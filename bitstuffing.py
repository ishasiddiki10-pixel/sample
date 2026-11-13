FLAG = '01111110'

def sender(data):
    result = ''
    count = 0
    for bit in data:
        result += bit
        if bit == '1':
            count += 1
            if count == 5:
                result += '0'
                count = 0
        else:
            count = 0
    return result
    
def receiver(data):
    result = ''
    count = i = 0
    while i < len(data):
        bit = data[i]
        result += bit
        if bit == '1':
            count += 1
            if count == 5:
                if i + 1 >= len(data) or data[i + 1] != '0':
                    raise ValueError("Invalid stuffed data")
                i += 1
                count = 0
        else:
            count = 0
        i += 1
    return result
    
def frame(data):
    if any(bit not in '01' for bit in data):
        raise ValueError("Invalid data")
    return FLAG + sender(data) + FLAG
    
def unframe(data):
    if len(data) < 16 or not data.startswith(FLAG) or not data.endswith(FLAG):
        raise ValueError("Invalid frame ")
    return receiver(data[8:-8])
    
data = '111110111111'
stuffed = frame(data)
original = unframe(stuffed)
print("Original:", data)
print("Stuffed Frame:", stuffed)
print("Received:", original)