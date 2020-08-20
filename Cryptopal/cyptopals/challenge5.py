#Burning 'em, if you ain't quick and nimble
#I go crazy when I hear a cymbal


#0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
#a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

def cypher_xor(plain, key):
        cipher = bytearray()
        for i in xrange(len(plain)):
            cipher.append(chr(plain[i] ^ key[i%len(key)]))
        return cipher

def main():
    line = [
        "Burning 'em, if you ain't quick and nimble/n",
        "I go crazy when I hear a cymbal"
    ]
    text = "".join(line)
    
    # key "ICE"
    key = bytearray("ICE" * len(text))
    #repeating-key XOR
    text = (cypher_xor(bytearray(text),key))
    plaintext = str(text).encode('hex')
    print 'cipher: {0}'.format(plaintext)

if __name__ == "__main__":
    main()


