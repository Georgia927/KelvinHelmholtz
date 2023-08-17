import yt
import os

folder_path = os.path.expanduser("~/Desktop/athena4.2/modified_kh_runs")

vtk_files = [file for file in os.listdir(folder_path) if file.endswith(".vtk")]

for vtk_file in vtk_files:
    # Construct the full file path
    file_path = os.path.join(folder_path, vtk_file)
    
    ds = yt.load(file_path)
    
    p = yt.SlicePlot(ds, "z", ("athena", "momentum_x")).save()
