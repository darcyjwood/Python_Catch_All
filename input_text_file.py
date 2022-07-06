def open_input(file):
    with open(file, 'r') as f:
        text = f.read() #We use read() to read the actual contents of the file
        print(text)

def main():
    open_input("brown_fox_text.txt") #put your file name here

if __name__=="__main__":
    main()
