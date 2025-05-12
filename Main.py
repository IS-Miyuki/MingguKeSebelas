dictionary = {1:10,2:20,3:30,4:40,5:50,6:60}
def Latihan1(x):
    
    print("key\tvalue\titem")
    for i,j  in enumerate(x):
        print(f"{j}\t{x[j]}\t{i+1}")

Latihan1(dictionary)

list1 = ['red','green','blue']
list2 = ['#FF0000','#008000','#0000FF']
def Latihan2(x,y):
    out = {}
    for i in range(len(x)):
        out[x[i]] = y[i]
    print(out)

Latihan2(list1,list2)

file = 'MingguKeSebelas/mbox-short.txt'
def Latihan3(files):
    try:
        with open(files) as file:
            file = file.read()
            file = file.split()
    except FileNotFoundError:
        return print(f"File {file} tidak ditemukan")
        
    
    email_count = {}
    
    for line in file:
        if line.startswith('From '):
            # Split the line and get the sender's email (second element)
            words = line.split()
            if len(words) >= 2:
                sender = words[1]
                # Count the occurrences of each email
                email_count[sender] = email_count.get(sender, 0) + 1
    
    # Print dictionary with pretty formatting
    print("{")
    for i, (email, count) in enumerate(email_count.items()):
        if i < len(email_count) - 1:
            print(f" '{email}': {count}, ")
        else:
            print(f" '{email}': {count}")
    print("}")

# Menjalankan Latihan 11.3
Latihan3(file)

def Latihan4():
    file = input("Masukkan nama file: ")
    try:
        with open(file) as file:
            file = file.read()
            file = file.split()
    except FileNotFoundError:
        print(f"File {file} tidak ditemukan")
        return
    
    domain_count = {}
    
    for line in file:
        if line.startswith('From '):
            # Split the line and get the sender's email
            words = line.split()
            if len(words) >= 2:
                email = words[1]
                # Extract domain (part after @)
                if '@' in email:
                    domain = email.split('@')[1]
                    # Count domains
                    domain_count[domain] = domain_count.get(domain, 0) + 1
    
    # Format and print dictionary
    output = "{"
    for i, (domain, count) in enumerate(domain_count.items()):
        output += f"'{domain}': {count}"
        if i < len(domain_count) - 1:
            output += ", "
    output += "}"
    print(output)

# Menjalankan Latihan 11.4
Latihan4()

