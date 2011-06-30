
import cPickle as pkl
import pylab as pl
from numpy import *

import sys

filters = sys.argv[1:]

prefix = "eccv10_individual_models__synthsets__"
suffix = "__COMPLETE.pkl"
ntrain_l_gt = ['150']
ntrials = 5

datasets = ["SynthSet_2_Faces_Var%02d" % i for i in xrange(7)]

print "Loading data..."
data_l = [pkl.load(open(prefix+dataset+suffix))
          for dataset in datasets]

models = data_l[0].keys()
models.sort()

print "Verifying data..."
for dataset, data in zip(datasets, data_l):
    print dataset
    datakeys = data.keys()
    datakeys.sort()
    assert datakeys == models

print "Extracting ..."
if len(ntrain_l_gt) != 1:
    raise NotImplementederError("len(ntrain_l_gt) != 1")

plots = dict([(model, {'x':[], 'y':[], 'yerr':[]}) for model in models])

for i, (dataset, data) in enumerate(zip(datasets, data_l)):
    for key, value in data.iteritems():
        accuracy_l = value['accuracy_l']
        ntrain_l = value['ntrain_l']
        assert value['ntrain_l'] == ntrain_l_gt
        assert accuracy_l.shape == (len(ntrain_l_gt), ntrials)
        plots[key]['x'] += [i]
        plots[key]['y'] += [accuracy_l.mean()]
        plots[key]['yerr'] += [accuracy_l.std()]

print "Plotting ..."

just_first = False

for grp_key, grp_color in zip(('v1like', 'l2', 'l3'),(array([0,0,1]), array([0,1,0]), array([1,0,0]))):
        
    # f = pl.figure()
    #     ax = f.add_subplot(1,1,1)
    #     ax.set_title(grp_key)
    pl.hold(True)
    
    for model in models[::-1]:
       
        if just_first:
            if "v1like" not in model and "1st" not in model:
                continue
            

        mix_ratio = 1.
        for rank, ratio in zip(("1st","2nd","3rd","4th","5th"), linspace(1.0, 0.1, 5)):
            if rank in model:
                mix_ratio = ratio

        grp_color_final = mix_ratio * grp_color + (1 - mix_ratio) * array([1,1,1])
    
        
        if grp_key not in model:
            continue
        
        
        if len(filters) != 0 and len([filt for filt in filters if filt in model]) == 0:
            continue

        curves = plots[model]

        x = curves['x']
        y = curves['y']
        yerr = curves['yerr']

        lines = pl.errorbar(x, y, yerr=yerr, label=model, color=grp_color_final)
        

pl.legend()
pl.show()

