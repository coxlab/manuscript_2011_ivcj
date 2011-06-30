
import os
from os import path, environ
import sys
import scipy as sp
import cPickle as pkl

out_fname = "eccv10_tp_fp_overlap.pkl"

SCLAS = "/home/thor/projects/sclas"
DATA_IN = "/media/raid2TB/LFW"
DATA_OUT = "/media/raid2TB/LFW"

# -- 
sys.path = [SCLAS] + sys.path
from error_analysis import error_analysis
# def error_analysis(input_fname1,
#                    input_fname2,
#                    # --
#                    input_path = DEFAULT_INPUT_PATH,
#                    output_path = DEFAULT_OUTPUT_PATH,
#                    overwrite = DEFAULT_OVERWRITE,
#                    ):

pattern = path.join(DATA_OUT, "lfw2__lfw_view2_split_%(ntrial)s.csv.svm_ova_results.%(model)s.mat")
print pattern

ntrials = 10

model_l = [
    ('v1like_a_plus', "v1like_a_plus_gray_crops.12kernels"),
    
    # -- HT-L2
    # export couchdb=lfw_phase4_ac_fulldev
    # export view='sort_v1/sort_v1'
    # export NIDS=5
    # python -c "from couchdb import client; srv=client.Server(); db=srv['$couchdb']; print '\n'.join([item.id for item in db.view('$view')][:$NIDS])" 
    # c6648f55164b541d388b72c91a6b0bae4f7b066d
    # 0b9ec368f5e5e1eeb02b9d159e15d0d21a860ce7
    # 653b6ec4cdb71c4666a0108f582b3521a488e15b
    # 7075d927ca8c052fc9b8a48b08bad836a999cf9f
    # 7f3d7267a2470ddee759b2ea392b66457ed87ddf
    ('ht_l2_1st', 'r3ls_pt2_c6648f55164b541d388b72c91a6b0bae4f7b066d_gray_crops.12kernels'),
    ('ht_l2_2nd', 'r3ls_pt2_0b9ec368f5e5e1eeb02b9d159e15d0d21a860ce7_gray_crops.12kernels'),
    ('ht_l2_3rd', 'r3ls_pt2_653b6ec4cdb71c4666a0108f582b3521a488e15b_gray_crops.12kernels'),
    ('ht_l2_4th', 'r3ls_pt2_7075d927ca8c052fc9b8a48b08bad836a999cf9f_gray_crops.12kernels'),
    ('ht_l2_5th', 'r3ls_pt2_7f3d7267a2470ddee759b2ea392b66457ed87ddf_gray_crops.12kernels'), 
    
    # -- HT-L3
    # export couchdb=lfw_phase2_ac_fulldev
    # export view='sort_v1/sort_v1'
    # export NIDS=5
    # python -c "from couchdb import client; srv=client.Server(); db=srv['$couchdb']; print '\n'.join([item.id for item in db.view('$view')][:$NIDS])"
    # 150fd767e9d5d6822e414b6ae20d7da6ce9469fa
    # d87123face6a91282d28a845dffb2e3e7328a669
    # de2b6b2be72cb9e6f9af06f04c7a073544d5c9e3
    # 53976e98ffa38aaea63b26f6aba132a486606236
    # 0f1aff3b5033e9442244accc9acbe1db6327dfa3
    ('ht_l3_1st', 'r3ls_pt2_150fd767e9d5d6822e414b6ae20d7da6ce9469fa_gray_crops.12kernels'),
    ('ht_l3_2nd', 'r3ls_pt2_d87123face6a91282d28a845dffb2e3e7328a669_gray_crops.12kernels'),
    ('ht_l3_3rd', 'r3ls_pt2_de2b6b2be72cb9e6f9af06f04c7a073544d5c9e3_gray_crops.12kernels'),
    ('ht_l3_4th', 'r3ls_pt2_53976e98ffa38aaea63b26f6aba132a486606236_gray_crops.12kernels'),
    ('ht_l3_5th', 'r3ls_pt2_0f1aff3b5033e9442244accc9acbe1db6327dfa3_gray_crops.12kernels'),

    # -- Blends
    ("ht_l2_top5", "ht_l2_top5_gray.60kernels"), 
    ("ht_l3_top5", "ht_l3_top5_gray.60kernels"),
    ("v1like_a_plus+ht_l2_top5_sum", "v1like_a_plus_gray_crops.12kernels+ht_l2_top5_gray.60kernels"),
    ("v1like_a_plus+ht_l2_top5+ht_l3_top5_sum", "v1like_a_plus_gray_crops.12kernels+ht_l2_top5_gray.60kernels+ht_l3_top5_gray.60kernels"),
    ("ht_l2_top5+ht_l3_top5_sum", "ht_l2_top5_gray.60kernels+ht_l3_top5_gray.60kernels"),
    ("1x_v1like_a_plus+2x_ht_l2_top5+4x_ht_l3_top5_hsum", "1x_v1like_a_plus_gray_crops.12kernels+2x_ht_l2_top5_gray.60kernels+4x_ht_l3_top5_gray.60kernels"),
    ]


nmodels = len(model_l)

tp_overlap_arr = sp.zeros((nmodels, nmodels), dtype='float32')
fp_overlap_arr = sp.zeros((nmodels, nmodels), dtype='float32')

for ntrial in xrange(ntrials):
    
    for j, (name1, model1) in enumerate(model_l):

        fname1 = pattern % {"model": model1, "ntrial": "%02d" % (ntrial+1)}
        
        for i, (name2, model2) in enumerate(model_l):

            fname2 = pattern % {"model": model2, "ntrial": "%02d" % (ntrial+1)}

            if i > j:
                continue

            if i == j:
                tp_overlap_arr[j,i] += 100.
                fp_overlap_arr[j,i] += 100.
                continue

            #print fname1
            #print fname2

            error = error_analysis(fname1, fname2, input_path=DATA_IN)

            tp_overlap = error['tp']['overlap']
            tp_overlap_arr[j,i] += tp_overlap
            tp_overlap_arr[i,j] += tp_overlap

            fp_overlap = error['fp']['overlap']
            fp_overlap_arr[j,i] += fp_overlap
            fp_overlap_arr[i,j] += fp_overlap
        
output_d = {
    "mean_tp_overlap": tp_overlap_arr/ntrials,
    "mean_fp_overlap": fp_overlap_arr/ntrials,
    "model_l": model_l,
    }

print "Saving", out_fname
pkl.dump(output_d, open(out_fname, 'w+'), protocol=2)


# import pylab as pl

# im = pl.matshow(tp_overlap_arr)
# for label in im.axes.xaxis.get_ticklabels():
#     label.set_rotation(90)

# im = pl.matshow(fp_overlap_arr)
# for label in im.axes.xaxis.get_ticklabels():
#     label.set_rotation(90)


# pl.show()

