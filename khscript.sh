#!/bin/bash

cd ~/desktop/athena4.2
./configure --with-gas=hydro --with-problem=kh_modified
make all
cd modified_kh_runs
./athena -i ../tst/2D-hydro/athinput.kh_modified.kh
