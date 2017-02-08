import json

with open('data.json','r') as f:
    read_data=json.load(f)
graphlist=read_data.replace('[','').replace(']','').replace(', {','').replace('{','').replace(', \'\'','').encode('utf-8').split('}')
fakelist=[]
for subreddit in graphlist:
    if subreddit:
        split1=subreddit.split(', \'subreddit\': ')
        subname=split1[1]
        split2=split1[0].split(', \'clusterdist\': ')
        cdist = float(split2[1])
        split3=split2[0].split(', \'subsize\': ')
        subsize=int(split3[1])
        clusternum=split3[0].split('\'cluster\': ')[1]
        fakelist.append({'id':subname,'clusternum':clusternum,'cdist':cdist,'subsize':subsize})
#        graph['nodes'][coolthing2.split(':')[0]]=coolthing2.split(':')[1]
