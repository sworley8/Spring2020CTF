import re
def score_alphatext(txt):
        scr = filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z' or x==' ', txt)
        return float(len(scr)) / len(txt)

def solve_single_key_xor(ba):
    res = []
    for i in range(256):
        characters = [chr(c ^ i) for c in ba]
        res.append([score_alphatext(characters), ''.join(characters), i])
    return max(res, key=lambda x: x[0])



# The ciphertexts are provided in a file named 4.txt
with open('4.txt', 'r') as f:
    lines = f.readlines()
    result = []
    for line in lines:
        line = bytearray(re.sub('[\n]','', line).decode('hex')    
        result.append(solve_single_key_xor(line))
    
    print(max(result, key=lambda x: x[0]))

    #cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    #print solve_single_key_xor(bytearray(cipher.decode('hex')))



