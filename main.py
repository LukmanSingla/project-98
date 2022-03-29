def swapfiledata():
    file1 = input("Enter the name of file 1 : ")
    file2 = input("Enter the name of file 2 : ")
    open1 = open(file1, 'r+')
    open2 = open(file2, 'r+')
    data1 = open1.read()
    data2 = open2.read()
    write1 = open(file1, 'w+')
    write2 = open(file2, 'w+')
    write1.write(data2)
    write2.write(data1)
    print("Data has been replaced")


swapfiledata()
