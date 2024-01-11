import random
test_num=25

def Generate(outfile):
    n=100000
    outfile.write(str(n)+"\n")
    s=""
    for i in range(1,int(n/5+1)):
        s=s+str(random.randint(1,1000000))+" "
    outfile.write(s+s+s+s+s)
    outfile.write("\n")