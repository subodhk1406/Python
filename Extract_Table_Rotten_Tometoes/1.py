import re
f = open("2.html","r")
i=0
j=0
k=0
tr=[]
counter =0
for x in f:
	i=i+1
	if "Movies Opening This Week" in x:
		print(x)
		j=1
	if "<table" in x and j==1:
		k=1
		j=0
	if "/table>" in x and k==1:
		k=0
	if k==1 and j==0:
		s=re.findall("<td(.*?)</td>",x)
		if s:
			a=re.findall(">(.*?)<",s[1])
			print(a[-1])