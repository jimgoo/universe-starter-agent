"""
Game tags have:

set([u'perspective'])
    set(['', u'driver', u'birdseye'])
"""

import os
import sys
import json
import pymongo

p = '/home/jimmie/git/universe/universe/runtimes/flashgames.json'
js = json.load(open(p))

print json.dumps(js, indent=2)
print 'nb_games: %i' % len(js.keys())

client = pymongo.MongoClient()
db = client['rl']
coll = db['universe-flashgames']
for j in js:
    coll.insert_many(j)

json.dump(js, open('flashgames.json', 'w+'), indent=3)

sys.exit(0)
################

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

