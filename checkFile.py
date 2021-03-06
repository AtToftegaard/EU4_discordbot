import os, sys, io, tkinter, re, pandas

def check_country(file, country):
    openFile = open(file)
    pattern = re.compile('.*(%s).*'%country)
   
    for line in openFile:
        if(re.match(pattern, line)):
            return True

def get_country(file, country):
    openFile = open(file)
    pattern = re.compile('.*(%s).*'%country)
   
    for line in openFile:
        if(re.match(pattern, line)):
            return line

def main():
    print("importing file: " +sys.argv[1])
    file = open(sys.argv[1])
    country = "Assam"
    if(check_country(file, country)):
        print("true")

if __name__ == '__main__':
    main()

