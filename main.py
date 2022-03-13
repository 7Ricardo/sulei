file_path = ("C:/Users/86133/Desktop/yq_in.txt")
with open(file_path,'r') as f:
    file = f.readlines()

file_len = len(file)
num = [0, 0, 0, 0, 0, 0, 0, 0]  #用于记录第几行开始发生变化
j=0
line = []

for i in range(file_len-1):
    if(file[i][0:3] != file[i+1][0:3]):
        num[j] = i+2
        j+=1
        #print(i+2)
        #print(file[i+1][0:3])

for j in range(file_len):
    list_str = list(file[j])
    if(j==0 or j==12 or j==24 or j==45 or j==58 or j==72 or j==88 or j==101 or j==120):
        line.append(list_str[:3])
    line.append(list_str[3:])

for var in line:
    print (var)




