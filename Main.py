dictionary = {1:10,2:20,3:30,4:40,5:50,6:60}
def Latihan1(x):
    print("key\tvalue\titem")
    for i,j in dictionary.items():
        print(f"{i}\t{j}\t{i+1}")

Latihan1(dictionary)

list1 = ['red','green','blue']
list2 = ['#FF0000','#008000','#0000FF']
def Latihan2(x,y):
    out = {}
    for i in range(len(x)):
        out[x[i]] = y[i]
    print(out)

Latihan2(list1,list2)

def Latihan3():
    file = input("Masukkan nama file: ")
    try:
        with open(file) as files:
            file = (files.read()).splitlines()
    except FileNotFoundError:
        return print(f"File {file} tidak ditemukan")
    
    email_count = {}
    for line in file:
        if line.startswith('From '):
            words = line.split()
            if words[1] not in email_count:
                email_count[words[1]] = 1
            else:
                email_count[words[1]] += 1
    print(email_count)

Latihan3()

def Latihan4():
    file = input("Masukkan nama file: ")
    domain_count = {}
    try:
        with open(file) as file:
            file = (file.read()).splitlines()
    except FileNotFoundError:
        return print(f"File {file} tidak ditemukan")
    
    for line in file:
        if line.startswith('From '):
            words = line.split()
            if '@' in words[1]:
                domain = words[1].split('@')[1]
                if domain not in domain_count:
                    domain_count[domain] = 1
                else:
                    domain_count[domain] += 1
    print(domain_count)

Latihan4()

