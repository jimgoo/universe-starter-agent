"""
Game tags have:

set([u'perspective'])
    set(['', u'driver', u'birdseye'])
"""

import os
import sys
import json
import pandas as pd
import pymongo


client = pymongo.MongoClient()
db = client['rl']
coll = db['universe-flashgames']

coll.drop()

p = '/home/jimmie/git/universe/universe/runtimes/flashgames.json'
js = json.load(open(p))

# print 'Num recs %i' % coll.count()
# for game, attrs in js.items():
#     d = {}
#     d['_id'] = game
#     for key, val in attrs.items():
#         d[key] = val
#         coll.insert(d)
# print 'Num recs %i' % coll.count()

#print json.dumps(js, indent=2)

print 'file:     %s' % p
print 'nb_games: %i' % len(js.keys())

# format more readable
json.dump(js, open('flashgames.json', 'w+'), indent=2)

df = pd.read_json('flashgames.json', orient='records').T

## convert {} to '' for easier summaries
# cols = ['height', 'tags', 'extra_files']
# for col in cols:
#     df.loc[:,col] = ['' if x == {} else x for x in df.loc[:,col].values ]
# #print df.describe()

print df.columns
print df.categories.value_counts().head(20)
print df.enable_internet.value_counts().head(20)
print df.autostart.value_counts()
print df.rewarder.value_counts()
print df.width.describe()
print 'screen-resolutions:'
print pd.Series(['%i X %i' % (h,w) for h,w in zip(df.height.values, df.width.values) if h and w]).value_counts().head(20)

# tags
dft = df.tags[df.tags != {}]
#print dft

print '='*100

print 'perspectives'
tags = set()
pers = set()
for game, attrs in js.items():
    tag = attrs['tags'].keys()
    per = attrs['tags'].get('perspective', '')
    tags.update(tag)
    pers.update([per])

print 'Game tags:'
print tags
print 'Game tag:perspectives'
print pers

# for attrs in js.values():
#     print '='*100
#     print attrs
#     print attrs['tags'].get('perspective', '')

print '='*100
print 'All Gym envs:'
from gym import envs
print(envs.registry.all())[:10]
