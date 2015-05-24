from Rewrite_CodonGeneconv import *

if __name__ == '__main__':
##    pairs = []
##    with open('../All_Pairs.txt', 'r') as f:
##        for line in f.readlines():
##            pairs.append(line.replace('\n','').split('_'))
##    pairs.remove(['YLR028C', 'YMR120C'])
##    pairs = pairs[-4:]
    pairs = [['ECP', 'EDN']]
    alignment_file = '../data/cleaned_input_data.fasta'
    newicktree = '../data/input_tree.newick'
    for pair in pairs:
        #alignment_file = '/Users/xji3/Genconv/PairsAlignemt/' + '_'.join(pair) + '/'+ '_'.join(pair) + '_input.fasta'
        #newicktree = '/Users/xji3/Genconv/PairsAlignemt/YeastTree.newick'
        paralog = pair
        Force = {4:0.0}

        x = np.array([-0.71060742, -0.51134973, -0.90114847,  2.32335336,  0.33647224,
       -5.01794203, -2.41741848, -3.48126512, -3.23389773, -4.57747962,
       -3.66450502, -4.96295342, -3.60311728, -5.80374553, -3.32299616,
       -3.96429684, -4.25932289])

        x_clock = np.array([-0.69108294, -0.53249743, -0.88422331,  0.94941569,  0.33647224, -2.09265894,
                            -0.7838321,  -0.45862259, -0.44907997, -0.1621296,  -0.21203529, -0.20060665])

        x = np.log([0.49024670857999997, 0.5770568002820878, 0.500764318357639, 2.11389841003, 1.8204058747,
         0.0706132002156, 0.102974211706, 0.00878905788968, 0.0511441873578, 0.0109179434163,
         0.0298626978464, 0.00455556207782, 0.00501138322281])        
        test = ReCodonGeneconv( newicktree, alignment_file, paralog, Model = 'HKY',Force = None, clock = False)
        test.update_by_x(x)
        print 'Now Calculate likelihood for pair ', pair
        try:
            result = test.get_mle(display = False)
            #test.get_ExpectedNumGeneconv()
            test.save_to_file(path = './NewPackageNewRun/')
        except:
            print 
            print 'Failed for ', pair, ' non clock'
            print

##        test2 = ReCodonGeneconv( newicktree, alignment_file, paralog, Model = 'HKY', clock = True)
##        #test2.update_by_x_clock(x_clock)
##        try:
##            result = test2.get_mle(display = False)
##            #test2.get_ExpectedNumGeneconv()
##            test2.save_to_file( path = './NewPackageNewRun/')
##        except:
##            print
##            print 'Failed for ', pair, ' clock'
##            print
##            
##        test3 = ReCodonGeneconv( newicktree, alignment_file, paralog, Model = 'HKY', clock = False, Force = Force)
##        #test3.update_by_x(x = x)
##        try:
##            result = test3.get_mle(display = False)
##            #test.get_ExpectedNumGeneconv()
##            test3.save_to_file(path = './NewPackageNewRun/Force_')
##        except:
##            print 
##            print 'Failed for ', pair, ' non clock Force'
##            print
##
##        test4 = ReCodonGeneconv( newicktree, alignment_file, paralog, Model = 'HKY', clock = True, Force = Force)
##
##        #test4.update_by_x_clock(x_clock)
##        try:
##            result = test4.get_mle(display = False)
##            #test.get_ExpectedNumGeneconv()
##            test4.save_to_file(path = './NewPackageNewRun/Force_')
##        except:
##            print
##            print 'Failed for ', pair, ' clock Force'
##            print


