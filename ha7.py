def find_first_larger(L,e,start=0):
    #L list wird als sortiert abgegeben.
    #diese Funktion macht binary search, divide and conquer
    #um die erste Grosse nummer als ggb Nummer(e) zu finden.
    #zb e= 10, funktion findet 11 in die liste oder 12...
    #die kleinste Großte nummer als e.
    #immmer noch halbe kontrollieren, sodass gibts O(log n) anstatt O(n)
    x=0
    mid=len(L)//2
    #mid = mitte der Liste, sodass prüfen wir rechte oder linken Seite.
    if L==[]:
        return 0
    #falls der Liste ist leer return 0.
    if e>=L[-1]:
        return len(L)
    #falls der ggb Nummer ist Großer als der Letzte element von L,
    #beispielsweise wird es der naechste element nach Letzte element
    #die Liste. zb: L=[10 , 22 , 33 , 56], e=70
    #e wird            0  , 1  , 2  , 3  , 4...
    #die möglichste Index für 70 wird 4.
    end=len(L)-1
    #finden wir immer mitte,erste und letzte element.
    while start<=end:
        mid=(start+end)//2
        #die element in mitte der Liste = mid
        if L[mid]<=e:
            start=mid+1
        #falls L=[10,22,33,56],e=40, mid=33, weil len(L)=4 4//2=2 L[2]=33
        #L[mid]<e (33,40)
        #dann start=3. Index also L[3]
        #und L[3] ist 56, return 56 also 4.te Index.
        else:
            end=mid-1
    return start

def unique(L):
    u=[]
    if L==[]:
        return []
    u=list(dict.fromkeys(L))
    
    k=0
    n=len(L)
    y=find_first_larger(L,L[k])
	if y=L[0]:
		return y
			
	i=0
	z+=L[i]
    while i<len(L):
		z=find_first_larger(L,L[i],i)
		u+=L[z]
	return u
			 
	#oder;;;
	
	for k in range(n):
		y=find_first_larger(L,L[k])
		L.
		    
    #
    #macht einfach for loop prüfen,
    #falls das kontrollierte element und naechste element ist gleich,
    #addiere die nicht. falls die sind ungleich, addieren.
    '''
    for i in range(len(L)-1):
        if L[i]!=L[i+1]:
            u+=[L[i]]
    if L:
        u+=[L[-1]]
    '''
    return u
