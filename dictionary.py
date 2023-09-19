from fileinput import close


words = set()

def main():

    def check(word):
        if word.lower() in words:
            return True
        else:
            return False

    def load(dictionary):
        file = open(dictionary, "r")
        for line in file:
            word = line.rstrip()
            words.add(word)
        close(file)
        return True

    def size():
        return len(words)
    
if __name__ == "__main__":
    main()