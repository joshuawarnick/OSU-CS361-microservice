import time
def test():
    file = open('pipe.txt', 'w')
    file.write('Hunter')
    file.close()

    time.sleep(12)
    file = open('pipe.txt', 'r')
    filename = file.readline()
    file.close()
    print(filename)

if __name__ == '__main__':
    test()