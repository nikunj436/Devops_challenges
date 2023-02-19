import re
import redis
r = redis.Redis(host='redis_cache', port=6379,db=0)

def add_to_dic(i):
    i_l = len(i)
    for j in range(i_l):
        #print(i[:j+1])
        r.zadd('Dic_set',{i[:j+1]:0})  #zadd key score1 value1...
        if j == i_l -1:
            with_ = i[:] + "*"
            #print(with_)
            r.zadd('Dic_set',{with_:0})

def find_match(i):

    res = []
    n = r.zcard('Dic_set')    #zcard(Dic_set)  #totoal 
    n_index = n -1 
    # or both give same value
    #n_index = r.zrank('Dic_set',r.zrange('Dic_set',-1,-1))
    fetch_index = r.zrank('Dic_set', i)  #if there is no match then sent "nonetype" and if condition it's treated as False
    
    fetch_index = str(fetch_index)
    if fetch_index == "None":
        return res
    fetch_index = int(fetch_index)
    
    fetch_index += 1 #next word
    
    while(len(res)!=10 and fetch_index<= n_index  ):

        comp = r.zrange('Dic_set',fetch_index, fetch_index)
        comp_value = str(comp[0])
        comp_value = comp_value[(comp_value.index('\'')+1):].strip("'")
        
        
        if not re.match("^"+i, comp_value):
            
            return res
        if comp_value[-1] == "*":
            res.append(comp_value[:-1])
        fetch_index += 1
    
    return res


file ="female-name.txt"

#initialization Dictonary 
def ini(file):
    f = open(file, "r")
    for i in f:
        i=i.strip()
        add_to_dic(i)
    f.close
