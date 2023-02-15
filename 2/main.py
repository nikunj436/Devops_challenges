import re
from size import good_look, is_n_max, is_m_above_limit, add_size

f = open('input.txt', 'r')
o = open('output.txt','w')

#['web2', '0', 'r', 'UNASSIGNED', '']
#['web3', '1', 'r', 'STARTED', '3014', '31.1gb', '192.168.56.20', 'I8hydUG']
#defining 
count_p, count_r = 0,0 
size_p, size_r = '0kb','0kb'
max_size,max_nord = "-1kb",[]
storage_matrix = []


for i in f:
    i = i.strip()
    i = re.split('\s+', i)


    # we are not counting unassigned to null
    if i[3] == "UNASSIGNED":
        continue
    i[5] = good_look(i[5])

    #count
    if i[2] == "p":
        count_p +=1
        size_p = add_size(i[5], size_p)
    else:
        count_r +=1
        size_r = add_size(i[5],size_r)
    
    
    #max and max nord
    i_max = is_n_max(i[5], max_size)
    if i_max == "same":
        max_nord.append(i[-1])
    elif i_max == "True":
        max_size = i[5]
        max_nord = [i[-1]]
    
    if is_m_above_limit(i[5]):
        storage_matrix.append(i[-1])



res=[]

#1st, 2nd
res.append("count: " + "[primary: {0}, replica: {1}]".format(count_p,count_r))
res.append("size: " + "[primary: {0}, replica: {1}]".format(size_r,size_r))
res.append("disk-max-node: "+ ",".join(max_nord))
res.append("watermark-breached: [" +",".join(storage_matrix) +"]")

le= len(res)
for i in range(le):
    print(res[i])
    if i != le-1:     #just for not go to next line
        res[i] += "\n"     
    o.write(res[i])
f.close()
o.close()