import sys

save_data = bool(int(sys.argv[1]))

out_prefix = "eccv10_blends__lfw__"

ntrials = 10

models = {
    
    # -- HT-L2-top5
    'ht_l2_top5' : 'ht_l2_top5_gray.60kernels',
    
    # -- HT-L3-top5
    'ht_l3_top5' : 'ht_l3_top5_gray.60kernels',

    # -- V1 + HT-L2-top5
    'v1like_a_plus+ht_l2_top5_sum': 'v1like_a_plus_gray_crops.12kernels+ht_l2_top5_gray.60kernels',

    # -- v1 + ht_l2_top5 + ht_l3_top5
    'v1like_a_plus+ht_l2_top5+ht_l3_top5_sum': 'v1like_a_plus_gray_crops.12kernels+ht_l2_top5_gray.60kernels+ht_l3_top5_gray.60kernels', 
    
    # -- ht_l2_top5 + ht_l3_top5
    'ht_l2_top5+ht_l3_top5_sum' : 'ht_l2_top5_gray.60kernels+ht_l3_top5_gray.60kernels',

    # -- 1*v1 + 2*ht_l2_top5 + 4*ht_l3_top5
    '1x_v1like_a_plus+2x_ht_l2_top5+4x_ht_l3_top5_hsum': '1x_v1like_a_plus_gray_crops.12kernels+2x_ht_l2_top5_gray.60kernels+4x_ht_l3_top5_gray.60kernels',

    # -- ((v1 + ht_l2_top5) + ht_l3_top5) # not the right formulation
    #'v1like_a_plus+ht_l2_top5+ht_l3_top5_hsum': '_v1like_a_plus_gray_crops.12kernels+ht_l2_top5_gray.60kernels_+ht_l3_top5_gray.60kernels',
    
    }


datasets = {
    
    # -- View 1
    "LFW-View1_gray_crops": {
        "path": "/media/raid2TB/LFW",
        "pattern": "lfw2__lfw_view1.csv.svm_ova_results.%(m_id)s.mat",
        "ntrain_l": ["2200"],
        "ntest_l": ["1100"],
        "ntrials": 1,
        },

    # -- View 2    
    "LFW-View2_gray_crops": {
        "path": "/media/raid2TB/LFW",
        "pattern": "lfw2__lfw_view2_split_??.csv.svm_ova_results.%(m_id)s.mat",
        "ntrain_l": ["5400"],
        "ntest_l": ["600"],
        "ntrials": 10,
        },
    }

from results2pkl import results2pkl

results2pkl(datasets, models, None, None, out_prefix, None, save_data)
