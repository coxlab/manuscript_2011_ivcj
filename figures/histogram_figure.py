#!/usr/bin/env python

import matplotlib.pyplot as plt
import cPickle as pkl

from numpy import *
import os

def adjust_axis(ax):
        
    for loc, spine in ax.spines.iteritems():
        if loc in ['left']:
            spine.set_position(('outward', 10))
        if loc in ['right', 'top']:
            spine.set_color('none')

    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    
    fontsize = 8
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(fontsize)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(fontsize)
    
    
v1_data = pkl.load(open('../data/eccv10_screening__ht_v1.pkl'))
l2_data = pkl.load(open('../data/eccv10_screening__ht_l2.pkl'))
l3_data = pkl.load(open('../data/eccv10_screening__ht_l3.pkl'))


plt.rc("xtick", direction="out")
plt.rc("ytick", direction="out")

f = plt.figure(figsize=(4, 5.5), dpi=100, facecolor='w')


plt.subplots_adjust(left = 0.2,
                right = 0.8,
                bottom = 0.15,
                top = 0.9,
                wspace = 0.1,
                hspace = 0.65)

# -------------------------------------------
# create the histogram
# -------------------------------------------

for name,data in ( ("v1like", v1_data), ("l2", l2_data), ("l3", l3_data)):
    perfs = [x[1] for x in data]
    model_ids = [x[0] for x in data]

    print len(perfs)

    f = plt.figure(figsize=(5, 3), dpi=100, facecolor='w')

    ax = f.add_subplot(1,1,1)
    plt.hold(True)

    plt.subplots_adjust(left = 0.2,
                        right = 0.8,
                        bottom = 0.15,
                        top = 0.95,
                        wspace = 0.1,
                        hspace = 0.65)

    ax.hold(True)

    hist = plt.hist(perfs, 30)
    ax.set_xlim([45.,85.])
    adjust_axis(ax)
    
    label_font = {'fontsize':9}
    ax.xaxis.set_label_text("performance", label_font)
    ax.yaxis.set_label_text("number of models", label_font)
    
    figure_name = "ht_%s_histogram.pdf" % name
    plt.savefig(figure_name)
    os.system("open %s" % figure_name)    
    
    
    
    # -------------------------------------------
    # Plot best 5 as bars
    # -------------------------------------------
    sorted_perfs = sort(perfs)
    top5 = sorted_perfs[-5:]

    f = plt.figure(figsize=(2.5, 3.5), dpi=100, facecolor='w')
    ax = f.add_subplot(1,1,1)
    plt.hold(True)

    plt.subplots_adjust(left = 0.3,
                    right = 0.8,
                    bottom = 0.15,
                    top = 0.9,
                    wspace = 0.1,
                    hspace = 0.65)

    width = 0.5
    labels = ['5th', '4th', '3rd', '2nd', '1st']
    xlocations = arange(0,5)
    
    plt.bar(xlocations, top5, width=width)
    
    plt.xticks(xlocations+ width/2, labels)
    
    ax.set_ylim([50.,90.])
    adjust_axis(ax)

    label_font = {'fontsize':9}
    ax.xaxis.set_label_text("model rank", label_font)
    ax.yaxis.set_label_text("performance", label_font)

    figure_name = "ht_%s_histogram_top5.pdf" % name
    plt.savefig(figure_name)
    os.system("open %s" % figure_name)
