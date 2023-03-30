fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    ipos=line.find(":")
    text=line[ipos+1:].strip()
    no=float(text)
    total=total+no
AVg=total/count
print("Average spam confidence:",AVg)
    
