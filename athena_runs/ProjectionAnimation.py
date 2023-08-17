import yt
import os

folder_path = os.path.expanduser("~/Desktop/athena_runs")

vtk_files = [file for file in os.listdir(folder_path) if file.endswith(".vtk")]

for vtk_file in vtk_files:
    file_path = os.path.join(folder_path, vtk_file)
    ds = yt.load(file_path)
    p = yt.SlicePlot(ds, "z", ("athena", "density")).save()