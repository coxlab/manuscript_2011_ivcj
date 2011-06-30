#!/usr/bin/env python
import matplotlib.pylab as pl
import numpy as np
import os

show_perf = True

def show_or_not(perf_string, doit):
    if(doit):
        return perf_string
    else:
        return ""

def adjust_axis(ax):

    for loc, spine in ax.spines.iteritems():
        if loc in ['left','bottom']:
            spine.set_position(('outward', 10))
            spine.set_linewidth(0.5)
        if loc in ['right', 'top']:
            spine.set_color('none')

    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    fontsize = 8
    for tick in ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(fontsize)
        tick.label1.set_family('sans-serif')
    for line in ax.xaxis.get_ticklines() + ax.yaxis.get_ticklines():
        line.set_markeredgewidth(0.5)

v1_crops_roc_data = {'title': "V1-like + crops" + show_or_not(" (82.4%)", show_perf),
                     'data': np.loadtxt("../data/lfw2__lfw_view2.csv.svm_ova_results.v1like_a_plus_gray_crops.12kernels.mat.roc.txt"),
                     'color': '0.75',
                     'linewidth': 1,
                     }

megablend_1_2_4_roc_data = {'title': "$\it{V1}+\it{L2}+\it{L3}_{(weighted)}$" + show_or_not(" (88.1%)", show_perf),
                            'data': np.loadtxt("../data/lfw2__lfw_view2.csv.svm_ova_results.1x_v1like_a_plus_gray_crops.12kernels+2x_ht_l2_top5_gray.60kernels+4x_ht_l3_top5_gray.60kernels.mat.roc.txt"),
                            'color': 'red',
                            'linewidth': 2,
                            }

megablend_1p1_1_roc_data = {'title': "(V1+L2)+L3 blend",
                            'data': np.loadtxt("../data/lfw2__lfw_view2.csv.svm_ova_results._v1like_a_plus_gray_crops.12kernels+ht_l2_top5_gray.60kernels_+ht_l3_top5_gray.60kernels.mat.roc.txt"),
                            'color': 'blue',
                            'linewidth': 1,
                            }

megablend_1_1_1_roc_data = {'title': "$\it{V1}+\it{L2}+\it{L3}$" + show_or_not(" (87.6%)", show_perf),
                            'data': np.loadtxt("../data/lfw2__lfw_view2.csv.svm_ova_results.v1like_a_plus_gray_crops.12kernels+ht_l2_top5_gray.60kernels+ht_l3_top5_gray.60kernels.mat.roc.txt"),
                            'color': 'magenta',
                            'linewidth': 1.5,
                            }

v1_l2_blend_roc_data = {'title': "V1+L2 ",
                        'data': np.loadtxt("../data/lfw2__lfw_view2.csv.svm_ova_results.v1like_a_plus_gray_crops.12kernels+ht_l2_top5_gray.60kernels.mat.roc.txt"),
                        'color': 'red',
                        'linewidth': 1,
                        }

l2_l3_blend_roc_data = {'title': "L2+L3" + show_or_not(" (87.5%)", show_perf),
                        'data': np.loadtxt("../data/lfw2__lfw_view2.csv.svm_ova_results.ht_l2_top5_gray.60kernels+ht_l3_top5_gray.60kernels.mat.roc.txt"),
                        'color': 'red',
                        'linewidth': 1,
                        }

l2_top5_roc_data = {'title': "$\it{L2}$ top 5 blend" + show_or_not(" (86.7%)", show_perf),
                    'data': np.loadtxt("../data/lfw2__lfw_view2.csv.svm_ova_results.ht_l2_top5_gray.60kernels.mat.roc.txt"),
                    'color': '0.5',
                    'linewidth': 1.5,
                    }

l3_top5_roc_data = {'title': "$\it{L3}$ top 5 blend" + show_or_not(" (87.8%)", show_perf),
                    'data': np.loadtxt("../data/lfw2__lfw_view2.csv.svm_ova_results.ht_l3_top5_gray.60kernels.mat.roc.txt"),
                    'color': '0',
                    'linewidth': 2,
                    }

wolf_data = {'title': "Wolf et al. ACCV09" + show_or_not(" (86.8%)", show_perf),
             'data': np.loadtxt("../data/accv09-wolf-hassner-taigman-roc.txt"),
             'color': 'blue',
             'linewidth': 1,
             }

kumar_data = {'title': "Kumar et al. ICCV09" + show_or_not(" (85.3%)", show_perf),
              'data': np.loadtxt("../data/kumar_attrs_sims.txt"),
              'color': 'green',
              'linewidth': 1,
              }

cao_data = {'title': "Cao et al. CVPR10" + show_or_not(" (84.5%)", show_perf),
              'data': np.loadtxt("../data/LE_combine.txt"),
              'color': 'cyan',
              'linewidth': 1,
              }

pl.rc("xtick", direction="out")
pl.rc("ytick", direction="out")

for name, grp in ( ('within', (l3_top5_roc_data,
                               l2_top5_roc_data,
                               v1_crops_roc_data,
                               )),
                   ('mega_blend', (
                       megablend_1_2_4_roc_data,
                       megablend_1_1_1_roc_data,
                       #v1_l2_blend_roc_data,
                       wolf_data,
                       kumar_data,
                       cao_data,
                       ))):

    f = pl.figure(figsize=(3.5, 3.5), dpi=100, facecolor='w')
    ax = f.add_subplot(1,1,1, aspect='equal')
    pl.hold(True)

    pl.subplots_adjust(left = 0.2,
                    right = 0.8,
                    bottom = 0.15,
                    top = 0.9,
                    wspace = 0.1,
                    hspace = 0.65)

    for model in grp:
        data = model['data']
        col = model['color']
        lw = model['linewidth']
        pl.plot(data[:,1], data[:,0], label=model['title'],
                color=col, linewidth=lw)

    adjust_axis(ax)
    ax.set_ylim(0.5, 1.0)
    ax.set_xlim(0.0, 0.5)
    ax.set_xlabel("false positive rate")
    ax.set_ylabel("true positive rate")

    label_font = {'size':7}
    leg = pl.legend(loc=4, prop=label_font, fancybox=True)
    leg.get_frame().set_alpha(0.1)

    figure_name = "%s_roc.pdf" % name
    pl.savefig(figure_name)
    os.system("open %s" % figure_name)


