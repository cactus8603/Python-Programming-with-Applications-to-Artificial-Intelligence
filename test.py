# read file
data = []
with open("三國演義.txt", "r+", errors="ignore") as f:
    data = f.readlines()
    
    # print(data[74])
for row in range(75,125):
    data[row] = "\t" + data[row].strip() + "\n"
    
    ind = 1
    while(ind):
        ind = data[row].find("。")
        if (data[row][ind+1] != "」"): 
            data[row] = data[row][ind:] + "\n\t" + data[row][:ind]
            print(data[row])
    

with open("output.txt", "w+") as f:
    f.writelines(data)