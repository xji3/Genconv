#!/bin/bash
python GenerateInfomationMatrix.py --paralog1 YPR159W --paralog2 YGR143W --model HKY --no-clock --no-force --no-dir --no-gBGC
python GenerateInfomationMatrix.py --paralog1 YPR159W --paralog2 YGR143W --model HKY --no-clock --no-force --no-dir --gBGC
python GenerateInfomationMatrix.py --paralog1 YPR159W --paralog2 YGR143W --model HKY --no-clock --no-force --dir --no-gBGC
python GenerateInfomationMatrix.py --paralog1 YPR159W --paralog2 YGR143W --model HKY --no-clock --no-force --dir --gBGC