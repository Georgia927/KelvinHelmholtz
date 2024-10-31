# Athena Setup and Simulation Execution

This repository contains a Bash script to configure, build, and run a specific Athena simulation with predefined settings. Athena is a grid-based code for astrophysical magnetohydrodynamics (MHD) simulations, and this script is configured to simulate a black hole system using specific modules and parameters.

## Requirements

- **Athena source code** (version 4.2) should be located in a folder named `athena4.2` on your desktop.
- **gcc and other compilation dependencies** for building Athena.
  
Ensure you have these dependencies installed before running the script.

## Instructions

### 1. Setting Up the Directory Structure

Ensure your project directory is set up as follows:

```bash
<your_desktop_path>
├── athena4.2        # Contains Athena source code and configuration files
└── athena_runs      # Directory where the compiled binary and simulation output will be stored 
```
### 2. Running the Script

This script configures, compiles, and runs the Athena simulation with the following commands:

```bash
desktop_path="/Users/georgiarichardson/desktop"
cd "$desktop_path/athena4.2"
./configure --with-gas=hydro --with-problem=BHSim --enable-viscosity
make all
cp "bin/athena" "$desktop_path/athena_runs"
cd "$desktop_path/athena_runs"
./athena -i "../athena4.2/tst/2D-hydro/athinput.bh.kh"


