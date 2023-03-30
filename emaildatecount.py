name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
cnt=dict()
for line in handle:
    if line.startswith("From "):
        line=line.split()
        line=line[5].split(":")
        if cnt.get(line[0],0)>=1:
            cnt[line[0]]=cnt[line[0]]+1
        else:
            cnt[line[0]]=1
cnt=sorted(cnt.items())
for k,va in cnt:
    print(k,va)
