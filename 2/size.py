ref = ["kb","mb","gb","tb"]

def arthi(num,num_str,op):
    if op == "/":
        num /= 1024
        num_str = ref[ref.index(num_str)+1]

    elif op == "*":
        num *= 1024
        num_str = ref[ref.index(num_str)-1]
    num = round(num,1)
    
    return num,num_str


def good_look(size_str):
    n,n_str = float(size_str[:-2]),size_str[-2:]
    

    while(n>1000 and n_str != ref[-1]):
        n,n_str = arthi(n,n_str,"/")
    
    while(n<1 and n_str != ref[0]):
        n,n_str = arthi(n,n_str,"*")
    
    return str(n)+n_str


def is_n_max(n,max):

    n,n_str = float(n[:-2]),n[-2:]
    max,max_str = float(max[:-2]),max[-2:]

    while(max_str != n_str):
        if ref.index(max_str) > ref.index(n_str):
            n,n_str = arthi(n,n_str,"/")
        else:
            n,n_str = arthi(n,n_str,"*")
    
    if n ==  max:
        return "Same"
    if n > max:
        return "True"
    else:
        return "False"

def is_m_above_limit(n):
    n,n_str = float(n[:-2]),n[-2:]

    if n_str == "tb":
        n,n_str = arthi(n,n_str,"*")
    while(n_str != "gb"):
        n,n_str = arthi(n,n_str,"/")
    
    if n >= 128*0.8:
        return True

def add_size(n,Total):

    n,n_str = float(n[:-2]),n[-2:]
    Total,Total_str = float(Total[:-2]),Total[-2:]
    
    while(Total_str != n_str):
        if ref.index(Total_str) > ref.index(n_str):
            n,n_str = arthi(n,n_str,"/")
        else:
            n,n_str = arthi(n,n_str,"*")
    
    Total += n
    Total =  str(Total)+Total_str
    return good_look(Total)