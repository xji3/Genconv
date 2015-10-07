from Rewrite_CodonGeneconv import ReCodonGeneconv
import argparse

def main(args):
    paralog = [args.paralog1, args.paralog2]
    sim_num = args.simnum
    Force = None
    clock = False
    alignment_file = './Simulation/' + '_'.join(paralog) + '/' + '_'.join(paralog) + '_MG94_nonclock_Sim_' + str(sim_num) + '.fasta'
    save_name = './SimulationSave/' + '_'.join(paralog) + '/' + '_'.join(paralog) + '_MG94_nonclock_Sim_' + str(sim_num) + '_save.txt'
    newicktree = './YeastTree.newick'
    test = ReCodonGeneconv( newicktree, alignment_file, paralog, Model = 'MG94', Force = None, clock = False, save_name = save_name)
    test.get_mle(True, True, 0, 'BFGS')
    test.get_individual_summary(summary_path = './SimulationSummary/' + '_'.join(paralog) + '/', file_name = './SimulationSummary/' + '_'.join(paralog) + '/' + '_'.join(paralog) + '_MG94_nonclock_Sim_' + str(num_boot) + '_summary.txt')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--paralog1', required = True, help = 'Name of the 1st paralog')
    parser.add_argument('--paralog2', required = True, help = 'Name of the 2nd paralog')
    parser.add_argument('--simnum', type = int, help = 'Number of Simulation Replicate')
    
    main(parser.parse_args())
## 
##    pairs = []
##    all_pairs = './Filtered_pairs.txt'
##    with open(all_pairs, 'r') as f:
##        for line in f.readlines():
##            pairs.append(line.replace('\n','').split('_'))
##    
##    model = 'MG94_'
##    sh_line = 'sbatch -o Sim-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./ShFiles/'
##
##    #pairs = [pairs[0]]
##
##    for paralog in pairs:
##    
##        with open('./Run_Sim_'+ '_'.join(paralog) +'.sh', 'w+') as f:
##            f.write('#!/bin/bash' + '\n')
##            for num_boot in range(100):
##                f.write(sh_line + model + '_'.join(paralog) + '_sim' + str(num_boot + 1) + '.sh\n')
##                with open('./ShFiles/' + model + '_'.join(paralog) + '_sim' + str(num_boot + 1) + '.sh', 'w+') as g:
##                    g.write('#!/bin/bash' + '\n')
##                    printscreen = ' > ' + '_'.join(paralog) + '_MG94_nonclock_Sim' + str(num_boot + 1) + '_PrintScreen.txt\n'
##                    g.write('python AnalyzeSimulation.py ' + ' --paralog1 ' + paralog[0] + ' --paralog2 ' + paralog[1] + ' --simnum ' + str(num_boot + 1) + printscreen)
##