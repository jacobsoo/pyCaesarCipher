import sys, os

def main(key, szfile):
    hFile = open(szfile, "rb")
    message = hFile.read()
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated
    
# Banner
def Banner():
    print("=================================================")
    print("Caesar Cipher v0.1                               ")
    print("=================================================")

# Usage
def help_menu(cmd):
    print("Usage: %s <key> <Name_of_File>\n") % (cmd)
    print("     : Length of <key> must be 1-26\n")

if __name__ == '__main__':
    Banner()
    if len(sys.argv)<3:
        help_menu(sys.argv[0])
    else:
        key = int(sys.argv[1])
        hFile = sys.argv[2]
        szRes = main(key, hFile)
        print("Decoded String : %s" % szRes)