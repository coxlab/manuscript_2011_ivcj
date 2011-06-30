

import pylab as pl
import cPickle as pkl


fname = "eccv10_tp_fp_overlap.pkl"

data = pkl.load(open(fname))

mean_tp_overlap = data['mean_tp_overlap']
mean_fp_overlap = data['mean_fp_overlap']

labels = [item[0] for item in data['model_l']]

#pl.figure(2)

#pl.subplot(121)
pl.figure(1)
#im = pl.matshow(mean_tp_overlap)
im = pl.imshow(mean_tp_overlap, interpolation='nearest')
pl.xticks(pl.arange(len(labels)), labels, rotation='vertical')
pl.yticks(pl.arange(len(labels)), labels)
pl.title("True Positives Overlap")

pl.figure(2)
#pl.subplot(122)
im = pl.imshow(mean_fp_overlap, interpolation='nearest')
pl.xticks(pl.arange(len(labels)), labels, rotation='vertical')
pl.yticks(pl.arange(len(labels)), labels)
pl.title("False Positives Overlap")

pl.show()
