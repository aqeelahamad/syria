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
	#return d_ls(site_ls)
	return site_ls

		


print check([['http://t.co/HZX0HrhNXV', 'Tue Sep 24 17:54:24 +0000 2013', 6.6773165756424475e-06], ['http://t.co/7i8kzYp13b', 'Tue Sep 24 16:44:45 +0000 2013', 6.6773165756424475e-06], ['http://t.co/b303Z8r933', 'Tue Sep 24 15:52:04 +0000 2013', 6.6773165756424475e-06], ['http://t.co/D7nHWSytr9', 'Tue Sep 24 15:48:24 +0000 2013', 6.6773165756424475e-06], ['http://t.co/bXv5exrMfA', 'Tue Sep 24 15:44:16 +0000 2013', 6.6773165756424475e-06], ['http://t.co/Wijhrodfwe', 'Tue Sep 24 15:36:57 +0000 2013', 6.6773165756424475e-06], ['http://t.co/L4pAJp85mY', 'Tue Sep 24 14:06:33 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Tue Sep 24 13:45:19 +0000 2013', 6.6773165756424475e-06], ['http://t.co/anhupA0uJA', 'Tue Sep 24 11:12:37 +0000 2013', 6.6773165756424475e-06], ['http://t.co/wtufHpxkcU', 'Tue Sep 24 10:46:53 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Tue Sep 24 09:45:19 +0000 2013', 6.6773165756424475e-06], ['http://t.co/LUIM8mK1hi', 'Tue Sep 24 00:34:26 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Mon Sep 23 23:45:19 +0000 2013', 6.6773165756424475e-06], ['http://t.co/72gBHuUZer', 'Mon Sep 23 18:55:55 +0000 2013', 6.6773165756424475e-06], ['http://t.co/IoibS1smcD', 'Mon Sep 23 18:00:41 +0000 2013', 6.6773165756424475e-06], ['http://t.co/Ao6j8E2hKI', 'Mon Sep 23 17:40:19 +0000 2013', 6.6773165756424475e-06], ['http://t.co/uScMIcj8rS', 'Mon Sep 23 17:06:41 +0000 2013', 6.6773165756424475e-06], ['http://t.co/7tD0ozbtYg', 'Mon Sep 23 17:05:41 +0000 2013', 6.6773165756424475e-06], ['http://t.co/rIscrmi97Q', 'Mon Sep 23 16:15:07 +0000 2013', 6.6773165756424475e-06], ['http://t.co/z8XrXjwfb2', 'Mon Sep 23 16:12:10 +0000 2013', 6.6773165756424475e-06], ['http://t.co/lGgugxs3Nd', 'Mon Sep 23 16:05:41 +0000 2013', 6.6773165756424475e-06], ['http://t.co/0LkSvuL2Pm', 'Mon Sep 23 16:01:07 +0000 2013', 6.6773165756424475e-06], ['http://t.co/4Zao0CjPeA', 'Mon Sep 23 14:45:21 +0000 2013', 6.6773165756424475e-06], ['http://t.co/iHLjosiV', 'Mon Sep 23 14:07:44 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Mon Sep 23 13:45:18 +0000 2013', 6.6773165756424475e-06], ['http://t.co/RfYNlxFN8Z', 'Mon Sep 23 13:44:59 +0000 2013', 6.6773165756424475e-06], ['http://t.co/0LkSvuL2Pm', 'Mon Sep 23 12:13:31 +0000 2013', 6.6773165756424475e-06], ['http://t.co/ROKHiCgkcv', 'Mon Sep 23 11:26:14 +0000 2013', 6.6773165756424475e-06], ['http://t.co/bROvteZ3MU', 'Mon Sep 23 09:55:29 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Mon Sep 23 09:45:18 +0000 2013', 6.6773165756424475e-06], ['http://t.co/RQdgXMogYw', 'Mon Sep 23 07:10:14 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Sun Sep 22 23:45:19 +0000 2013', 6.6773165756424475e-06], ['http://t.co/6qH3ulhL4G', 'Sun Sep 22 23:30:02 +0000 2013', 6.6773165756424475e-06], ['http://t.co/ivHHTcVTId', 'Sun Sep 22 23:08:55 +0000 2013', 6.6773165756424475e-06], ['http://t.co/X5Eg8u0Fcl', 'Sun Sep 22 22:00:40 +0000 2013', 6.6773165756424475e-06], ['http://t.co/oeGkDDl1Vm', 'Sun Sep 22 20:07:32 +0000 2013', 6.6773165756424475e-06], ['http://t.co/QfEdwzNbsF', 'Sun Sep 22 19:44:48 +0000 2013', 6.6773165756424475e-06], ['http://t.co/sUD77i8qbE', 'Sun Sep 22 18:35:18 +0000 2013', 6.6773165756424475e-06], ['http://t.co/3zP2RfeLRB', 'Sun Sep 22 18:35:02 +0000 2013', 6.6773165756424475e-06], ['http://t.co/SW4JsdFKH6', 'Sun Sep 22 18:17:10 +0000 2013', 6.6773165756424475e-06], ['http://t.co/0GNY4rN6Xu', 'Sun Sep 22 18:17:07 +0000 2013', 6.6773165756424475e-06], ['http://t.co/Hvxm2vwioy', 'Sun Sep 22 18:16:21 +0000 2013', 6.6773165756424475e-06], ['http://t.co/JASaefHGjO', 'Sun Sep 22 18:12:09 +0000 2013', 6.6773165756424475e-06], ['http://t.co/YU6FostY9x', 'Sun Sep 22 18:06:20 +0000 2013', 6.6773165756424475e-06], ['http://t.co/XrsjBCKfPf', 'Sun Sep 22 17:59:03 +0000 2013', 6.6773165756424475e-06], ['http://t.co/YHRn5KddMU', 'Sun Sep 22 17:56:05 +0000 2013', 6.6773165756424475e-06], ['http://t.co/8jQwc0jRuS', 'Sun Sep 22 15:16:08 +0000 2013', 6.6773165756424475e-06], ['http://t.co/FYIwYy19Ky.', 'Sun Sep 22 14:58:12 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Sun Sep 22 13:45:18 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Sun Sep 22 09:45:18 +0000 2013', 6.6773165756424475e-06], ['http://t.co/bm65PNDExT', 'Sun Sep 22 02:42:58 +0000 2013', 6.6773165756424475e-06], ['http://t.co/L4pAJp85mY', 'Sun Sep 22 00:22:13 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Sat Sep 21 23:45:19 +0000 2013', 6.6773165756424475e-06], ['http://t.co/gE50BBOydA', 'Sat Sep 21 17:20:47 +0000 2013', 6.6773165756424475e-06], ['http://t.co/3PSjXQLFzO', 'Sat Sep 21 15:38:24 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Sat Sep 21 13:45:18 +0000 2013', 6.6773165756424475e-06], ['http://t.co/U2kSQ5hOcN', 'Sat Sep 21 10:20:23 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Sat Sep 21 09:45:18 +0000 2013', 6.6773165756424475e-06], ['http://t.co/s0L9zqRTwE', 'Sat Sep 21 09:15:09 +0000 2013', 6.6773165756424475e-06], ['http://t.co/b0hIoRKYw5', 'Sat Sep 21 03:50:27 +0000 2013', 6.6773165756424475e-06], ['http://t.co/otNBgoaN2X', 'Fri Sep 20 23:45:19 +0000 2013', 6.6773165756424475e-06]])