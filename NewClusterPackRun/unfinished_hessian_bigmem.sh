#!/bin/bash
sbatch -o cd-%j.out -p --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YBR117C_YPR074C_Dir_gBGC_HKY_Hessian_unfinished.sh
sbatch -o cd-%j.out -p --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YIR033W_YKL020C_Dir_gBGC_HKY_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YML026C_YDR450W__MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YER074W_YIL069C__MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YML026C_YDR450W_Dir_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YJL177W_YKL180W_Dir_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YER074W_YIL069C_Dir_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YLR333C_YGR027C_Dir_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YML026C_YDR450W_gBGC_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YPR157W_YGR141W_gBGC_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YMR143W_YDL083C_gBGC_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YER074W_YIL069C_gBGC_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YLR333C_YGR027C_gBGC_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YML026C_YDR450W_Dir_gBGC_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YPR157W_YGR141W_Dir_gBGC_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YER074W_YIL069C_Dir_gBGC_MG94_Hessian_unfinished.sh
sbatch -o cd-%j.out --mail-type=FAIL --mail-user=xji3@ncsu.edu ./NewRun/YLR333C_YGR027C_Dir_gBGC_MG94_Hessian_unfinished.sh
