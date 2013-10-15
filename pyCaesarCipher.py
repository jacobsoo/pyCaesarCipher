import sys, os, optparse

def main(key, szfile):
    try:
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
    except IOError:
        print("Error: can\'t find file or read data")

# Banner
def Banner():
    print("=================================================")
    print("Caesar Cipher v0.1                               ")
    print("=================================================")

if __name__ == '__main__':
    Banner()
    parser = optparse.OptionParser()
    parser.add_option('-k', '--key', dest='key', help='Length of <key> must be 1-26', type=int)
    parser.add_option('-i', '--inputfile', dest='ifile', help='Name of inout file. <Name_of_File>')
    
    (options,args) = parser.parse_args()
    
    if options.key and options.ifile:
        szRes = main(options.key, options.ifile)
        if szRes!=None:
            print("Decoded String : %s" % szRes)
        else:
            print("There could be problem with the file.")
    elif len(args) != 3:
        parser.error("wrong number of arguments")
        print options
        print args