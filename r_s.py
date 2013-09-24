import urllib

site_ls={}

def rank(links,followers,friends,favorite,total,time):
	if total==0 or followers==0:
		sig=0
	else:
		if friends==0:
			friends=1
		elif favorite==0:
			favorite=1
	sig=float(followers)/float(friends)*float(favorite)/float(total)
	links=str(links[0])
	return [links,str(time),sig]
	
def sort(ls):
    if not ls:
        return []
    else:
        pivot = ls[0]
        less = [x for x in ls[1:] if x[2] <  pivot[2]]
        greater = [x for x in ls[1:] if x[2] >= pivot[2]]
        return sort(greater) + [pivot] + sort(less)
        
def d_ls(ls):
	new_ls=[]
	for t,d,s in ls.values():
		new_ls.append([t,d,s])
	return new_ls
	
	
def check(lst):
	for ls in lst:
		c=urllib.urlopen(ls[0])
		c=c.url
		if c not in site_ls:
			site_ls[c]=ls
		else:
			if ls[2]>site_ls[c][2]:
				site_ls[c]=ls 
	d=d_ls(site_ls)
	return d

		


#print check_sort([['http://t.co/72gBHuUZer', 'Mon Sep 23 18:55:55 +0000 2013', 1.3693905472665277e-05],['http://t.co/72gBHuUZer', 'Mon Sep 23 18:55:55 +0000 2013', 1.3693905472665277e-05]])