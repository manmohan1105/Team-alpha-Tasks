'''
One-method-that-accepts the "url" variable-below, parses the query string-parameters (everything-after-the-?), and returns 
the following dictionary/hashmap/hash-with-the-query-string-key-values-as -key-values-in-the-data-structure. 
If-there-are-identical-keys, add-the

#Input:

gid-10"

values to a list. -url "https://api.komodohealth.com/vi/organizations?oid=5&pid=4&pid=7&qid=10"

#Returns (Python-dictionary, not-JSON):
{
"oid": 5,
"pid":[4,7], 
"qid": 10
}
'''
import collections
def function(url):
    d=collections.defaultdict(list)
    _,s=url.split("?")
    s=s.split("&")
    for i in s:
        x,y=i.split("=")
        d[x].append(int(y))
    d1={}
    for i in d:
        if len(d[i])==1:
           d1[i]=d[i][0]
        else:   
            d1[i]=d[i]
    print(d1) 
function("https://api.komodohealth.com/vi/organizations?oid=5&pid=4&pid=7&qid=10")           


 