import pandas as pd
from ydata_profiling import ProfileReport
from importlib.metadata import PackageNotFoundError, version

df = pd.read_csv('results_2024.csv')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file(output_file="results.html")

try:
    print(f"ydata-profiling version: {version('ydata-profiling')}")
except PackageNotFoundError:
    print("ydata-profiling is not installed.")


