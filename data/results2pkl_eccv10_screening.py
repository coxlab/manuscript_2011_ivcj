
from os import path
import cPickle
from couchdb import client
mypath = path.dirname(path.realpath(__file__))

# ------------------------------------------------------------------------------
# -- Parameters
# ------------------------------------------------------------------------------
prefix = "eccv10_screening__"

models = {
    'ht_v1': ('lfw_phase1_ac_fulldev', 'lfw_phase1_ac_fulldev/sort_v1'),
    'ht_l2': ('lfw_phase4_ac_fulldev', 'sort_v1/sort_v1'),
    'ht_l3': ('lfw_phase2_ac_fulldev', 'sort_v1/sort_v1'),
    }

# ------------------------------------------------------------------------------
# -- Results extraction code
# ------------------------------------------------------------------------------
srv=client.Server()
for m_name, (db_name, view_name) in models.iteritems():

    print m_name, db_name, view_name
    
    db = srv[db_name]
    output = [(item.id, abs(item.key))
              for item in db.view(view_name)]
    print len(output)
    
    out_fname = path.join(mypath, prefix+m_name+'.pkl')
    
    print "Writing:", out_fname
    fin = open(out_fname, "w+")
    cPickle.dump(output, fin, protocol=2)
    fin.close()
