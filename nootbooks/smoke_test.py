import pathlib
import pandas as pd

# تحديد المسار للوصول إلى sample.csv من داخل مجلد src
data_path = pathlib.Path(__file__).parent.parent / "data" / "sample.csv"

df = pd.read_csv(data_path)

print("Shape:", df.shape)
print(df.head())
print(df.describe())