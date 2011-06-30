import sys

save_data = bool(int(sys.argv[1]))

out_prefix = "eccv10_individual_models__synthsets__"

ntrials = 5

models = {
    
    # -- V1
    'v1like_a_plus': 'v1like_a_plus',

    # -- HT-V1
    # export couchdb=lfw_phase1_ac_fulldev
    # export view='lfw_phase1_ac_fulldev/sort_v1'
    # export NIDS=5
    # python -c "from couchdb import client; srv=client.Server(); db=srv['$couchdb']; print '\n'.join([item.id for item in db.view('$view')][:$NIDS])"    
    # e92d1787f0a905a15c66b1f032016ec5aff2bd6a
    # 2a611fc3d36b203511dbd8172023d158873fcf80
    # 17c8f7b7fb6db0b162c742e9b04ac189e6d4a3bd
    # 1b73e7dcf296d65f520947f019497d8e12993aae
    # c6c8fdb45780a3e8f6a8244a562eff63f682120b
    'ht_v1_1st' : 'v1like_pt2_e92d1787f0a905a15c66b1f032016ec5aff2bd6a_gray', 
    'ht_v1_2nd' : 'v1like_pt2_2a611fc3d36b203511dbd8172023d158873fcf80_gray', 
    'ht_v1_3rd' : 'v1like_pt2_17c8f7b7fb6db0b162c742e9b04ac189e6d4a3bd_gray', 
    'ht_v1_4th' : 'v1like_pt2_1b73e7dcf296d65f520947f019497d8e12993aae_gray', 
    'ht_v1_5th' : 'v1like_pt2_c6c8fdb45780a3e8f6a8244a562eff63f682120b_gray', 
    
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
    'ht_l2_1st' : 'r3ls_pt2_c6648f55164b541d388b72c91a6b0bae4f7b066d_gray',
    'ht_l2_2nd' : 'r3ls_pt2_0b9ec368f5e5e1eeb02b9d159e15d0d21a860ce7_gray',
    'ht_l2_3rd' : 'r3ls_pt2_653b6ec4cdb71c4666a0108f582b3521a488e15b_gray',
    'ht_l2_4th' : 'r3ls_pt2_7075d927ca8c052fc9b8a48b08bad836a999cf9f_gray',
    'ht_l2_5th' : 'r3ls_pt2_7f3d7267a2470ddee759b2ea392b66457ed87ddf_gray',
    
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
    'ht_l3_1st' : 'r3ls_pt2_150fd767e9d5d6822e414b6ae20d7da6ce9469fa_gray',
    'ht_l3_2nd' : 'r3ls_pt2_d87123face6a91282d28a845dffb2e3e7328a669_gray',
    'ht_l3_3rd' : 'r3ls_pt2_de2b6b2be72cb9e6f9af06f04c7a073544d5c9e3_gray',
    'ht_l3_4th' : 'r3ls_pt2_53976e98ffa38aaea63b26f6aba132a486606236_gray',
    'ht_l3_5th' : 'r3ls_pt2_0f1aff3b5033e9442244accc9acbe1db6327dfa3_gray',
    
    }

ntrain_l = ["150"]
ntest_l = ["150"]
datasets = {
    "SynthSet_2_Faces_Var00": {
        "path": "/thor_share/ControlSets_Faces/CVPR2010_ControlSet_2_Faces_Variation00_NaturalBg_n300_150x150_GS",
        "pattern": "train%(ntrain)stest%(ntest)s_split_??.csv.svm_ova_results.%(m_id)s.mat",
       },
    "SynthSet_2_Faces_Var01": {
        "path": "/thor_share/ControlSets_Faces/CVPR2010_ControlSet_2_Faces_Variation01_NaturalBg_n300_150x150_GS",
        "pattern": "train%(ntrain)stest%(ntest)s_split_??.csv.svm_ova_results.%(m_id)s.mat",
       },
    "SynthSet_2_Faces_Var02": {
        "path": "/thor_share/ControlSets_Faces/CVPR2010_ControlSet_2_Faces_Variation02_NaturalBg_n300_150x150_GS",
        "pattern": "train%(ntrain)stest%(ntest)s_split_??.csv.svm_ova_results.%(m_id)s.mat",
       },
    "SynthSet_2_Faces_Var03": {
        "path": "/thor_share/ControlSets_Faces/CVPR2010_ControlSet_2_Faces_Variation03_NaturalBg_n300_150x150_GS",
        "pattern": "train%(ntrain)stest%(ntest)s_split_??.csv.svm_ova_results.%(m_id)s.mat",
       },
    "SynthSet_2_Faces_Var04": {
        "path": "/thor_share/ControlSets_Faces/CVPR2010_ControlSet_2_Faces_Variation04_NaturalBg_n300_150x150_GS",
        "pattern": "train%(ntrain)stest%(ntest)s_split_??.csv.svm_ova_results.%(m_id)s.mat",
       },
    "SynthSet_2_Faces_Var05": {
        "path": "/thor_share/ControlSets_Faces/CVPR2010_ControlSet_2_Faces_Variation05_NaturalBg_n300_150x150_GS",
        "pattern": "train%(ntrain)stest%(ntest)s_split_??.csv.svm_ova_results.%(m_id)s.mat",
       },
    "SynthSet_2_Faces_Var06": {
        "path": "/thor_share/ControlSets_Faces/CVPR2010_ControlSet_2_Faces_Variation06_NaturalBg_n300_150x150_GS",
        "pattern": "train%(ntrain)stest%(ntest)s_split_??.csv.svm_ova_results.%(m_id)s.mat",
       },
    }


#CVPR2010_ControlSet_2_Faces_Variation01_NaturalBg_n300_150x150_GS
#CVPR2010_ControlSet_2_Faces_Variation02_NaturalBg_n300_150x150_GS
#CVPR2010_ControlSet_2_Faces_Variation03_NaturalBg_n300_150x150_GS
#CVPR2010_ControlSet_2_Faces_Variation04_NaturalBg_n300_150x150_GS
#CVPR2010_ControlSet_2_Faces_Variation05_NaturalBg_n300_150x150_GS
#CVPR2010_ControlSet_2_Faces_Variation06_NaturalBg_n300_150x150_GS

from results2pkl import results2pkl

results2pkl(datasets, models, ntrain_l, ntest_l, out_prefix, ntrials, save_data)
