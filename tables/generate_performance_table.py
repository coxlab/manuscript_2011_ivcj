#!/usr/bin/env python
import cPickle as pkl
from mako.template import Template
import scipy as sp

in_filename = "grand_performance_table.tex.mako"
out_filename = "grand_performance_table.tex"

in_file = open(in_filename, 'r')
template = in_file.read()
in_file.close()

data_dict = {}

gray_data = pkl.load(open("../data/eccv10_individual_models__lfw__LFW-View2_gray__COMPLETE.pkl"))
crops_data = pkl.load(open("../data/eccv10_individual_models__lfw__LFW-View2_gray_crops__COMPLETE.pkl"))
blends_data = pkl.load(open("../data/eccv10_blends__lfw__LFW-View2_gray_crops__COMPLETE.pkl"))

def trunc_prec(num):
    return int(100 * num) / 100.

for model in gray_data:
    data_dict[model] = (trunc_prec(gray_data[model]['accuracy_l'].mean()),
                        trunc_prec(gray_data[model]['accuracy_l'].std()/sp.sqrt(gray_data[model]['accuracy_l'].size)))
    data_dict[model + "_crops"] = (trunc_prec(crops_data[model]['accuracy_l'].mean()),
                                   trunc_prec(crops_data[model]['accuracy_l'].std()/sp.sqrt(crops_data[model]['accuracy_l'].size)))
    data_dict[model + "_color"] = (0, 0)

for model in blends_data:
    data_dict[model] = (trunc_prec(blends_data[model]['accuracy_l'].mean()),
                        trunc_prec(blends_data[model]['accuracy_l'].std()/sp.sqrt(blends_data[model]['accuracy_l'].size))
                        )

print data_dict

data_dict["ht_l2_blend"] = data_dict["ht_l2_top5"]
data_dict["ht_l3_blend"] = data_dict["ht_l3_top5"]
data_dict["v1_l2_blend"] = data_dict["v1like_a_plus+ht_l2_top5_sum"]
data_dict["l2_l3_blend"] = data_dict["ht_l2_top5+ht_l3_top5_sum"]
data_dict["v1_l2_l3_blend"] = data_dict["v1like_a_plus+ht_l2_top5+ht_l3_top5_sum"]
data_dict["v1_l2_l3_weighted_blend"] = data_dict["1x_v1like_a_plus+2x_ht_l2_top5+4x_ht_l3_top5_hsum"]

output = Template(template).render(**data_dict)

out_file = open(out_filename, 'w')
out_file.write(output)
out_file.close()
