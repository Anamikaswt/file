
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
file1=open("bank.txt","r+")
for i in banks_list:
    file1.write(i)
    file1.write("\n")


# f=open("bank.txt","r")
# filedata=f.read()
# f.close()
# print(filedata)


