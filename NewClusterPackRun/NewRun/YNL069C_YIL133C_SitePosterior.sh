#!/bin/bash
python get_site_posterior.py --paralog1 YNL069C --paralog2 YIL133C --model HKY --clock --force --no-dir --no-gBGC
python get_site_posterior.py --paralog1 YNL069C --paralog2 YIL133C --model HKY --clock --no-force --no-dir --no-gBGC
python get_site_posterior.py --paralog1 YNL069C --paralog2 YIL133C --model HKY --clock --no-force --no-dir --gBGC
python get_site_posterior.py --paralog1 YNL069C --paralog2 YIL133C --model HKY --clock --no-force --dir --no-gBGC
python get_site_posterior.py --paralog1 YNL069C --paralog2 YIL133C --model HKY --clock --no-force --dir --gBGC
python get_site_posterior.py --paralog1 YNL069C --paralog2 YIL133C --model MG94 --clock --force --no-dir --no-gBGC
python get_site_posterior.py --paralog1 YNL069C --paralog2 YIL133C --model MG94 --clock --no-force --no-dir --no-gBGC
python get_site_posterior.py --paralog1 YNL069C --paralog2 YIL133C --model MG94 --clock --no-force --no-dir --gBGC
python get_site_posterior.py --paralog1 YNL069C --paralog2 YIL133C --model MG94 --clock --no-force --dir --no-gBGC
python get_site_posterior.py --paralog1 YNL069C --paralog2 YIL133C --model MG94 --clock --no-force --dir --gBGC