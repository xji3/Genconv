#!/bin/bash
python GenerateInfomationMatrix.py --paralog1 YDR099W --paralog2 YER177W --model HKY --no-clock --no-force --no-dir --no-gBGC
python GenerateInfomationMatrix.py --paralog1 YDR099W --paralog2 YER177W --model HKY --no-clock --no-force --no-dir --gBGC
python GenerateInfomationMatrix.py --paralog1 YDR099W --paralog2 YER177W --model HKY --no-clock --no-force --dir --no-gBGC
python GenerateInfomationMatrix.py --paralog1 YDR099W --paralog2 YER177W --model HKY --no-clock --no-force --dir --gBGC