import elasticsearch
import json
es = elasticsearch.Elasticsearch()
query='"match": {"_index": "homedepot"}'
# print es.get(index='homedepot', doc_type='items', id=3)
set=es.search(index="homedepot", size=10000,body={"query": {"match": {"product_title":"light"}}})
#total, max_score, hits
s=set['hits']
s1=s['hits']
print len(s1)
s2= s['total']
print s2
