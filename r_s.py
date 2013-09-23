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
        return sort(less) + [pivot] + sort(greater)	

print sort([['http://t.co/YSC8RBaMvs', 'Mon Sep 23 20:40:52 +0000 2013', 7.560599470125351e-05], 
 ['http://t.co/72gBHuUZer', 'Mon Sep 23 18:55:55 +0000 2013', 7.560599470125351e-05]])