from glob import glob
import os
import sys
from os import path
from pprint import pprint
import cPickle
import scipy as sp
from scipy import io

mypath = path.dirname(path.realpath(__file__))

def results2pkl(datasets, models, ntrain_l, ntest_l, out_prefix, ntrials, save_data=False):


    # -- loop over all the datasets
    # each dataset will produce a different pickle file
    keys = datasets.keys()
    keys.sort()
    for ds_name in keys:

        ds_dict = datasets[ds_name]
        
        ds_path = ds_dict['path']
        ds_pattern = ds_dict['pattern']
        ds_ntrials = ds_dict.get('ntrials', ntrials)
        ds_ntrain_l = ds_dict.get('ntrain_l', ntrain_l)
        ds_ntest_l = ds_dict.get('ntest_l', ntest_l)

        # assume the data is complete for now...
        complete = True

        # -- loop over the models    
        ntotal = 0
        nok = 0
        output = {}
        for m_name, m_id in models.iteritems():
            print ds_name, m_name, m_id

            m_ntrain_l = []
            m_accuracy_l = []

            nsubtotal = 0
            nsubok = 0
            for ntrain, ntest in zip(ds_ntrain_l, ds_ntest_l):
                sys.stdout.write("%s, " % ntrain)
                sys.stdout.flush()
                pval = {'ntrain': ntrain, 'ntest': ntest, 'm_id': m_id}
                pattern = path.join(ds_path, ds_pattern % pval)
                print pattern
                
                fname_l = glob(pattern)
                
                nok += len(fname_l)
                nsubok += len(fname_l)

                ntotal += ds_ntrials
                nsubtotal += ds_ntrials
                
                if len(fname_l) != ds_ntrials:
                    complete = False
                else:
                    curr_acc_l = []
                    if save_data:
                        for fname in fname_l:
                            ok = False
                            try:
                                acc = io.loadmat(fname)['accuracy'][0].ravel()
                                curr_acc_l += [acc]
                                ok = True
                            except IndexError, IOError:
                                print "[ERROR] with", fname
                                complete = False
                        if ok:
                            m_ntrain_l += [ntrain]
                            m_accuracy_l += [curr_acc_l]
            print
            print 100.*nsubok/nsubtotal

            if save_data:
                output[m_name] = {"ntrain_l": m_ntrain_l,
                                  "accuracy_l": sp.array(m_accuracy_l).reshape(-1, ds_ntrials)}
                assert len(output[m_name]['ntrain_l']) == len(output[m_name]['accuracy_l'])
                print len(output[m_name]['accuracy_l'])
                print output[m_name]['ntrain_l']
                print output[m_name]['accuracy_l'].mean(1)

        print
        print "%s (%.2f%% complete)" % (ds_name, 100.*nok/ntotal)
        print "*"*80
        print

        if save_data:
            if complete:
                out_pattern = "%s%s__COMPLETE.pkl"
            else:
                out_pattern = "%s%s__INCOMPLETE.pkl"
            out_fname = path.join(mypath, out_pattern % (out_prefix, ds_name))

            print "Writing:", out_fname
            fin = open(out_fname, "w+")
            cPickle.dump(output, fin, protocol=2)
            fin.close()    
        
