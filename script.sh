#!/bin/bash

desktop_path="/Users/georgiarichardson/desktop"
cd "$desktop_path/athena4.2"
./configure --with-gas=hydro --with-problem=BHSim --enable-viscosity
make all
cp "bin/athena" "$desktop_path/athena_runs"
cd "$desktop_path/athena_runs"
./athena -i "../athena4.2/tst/2D-hydro/athinput.bh.kh"
