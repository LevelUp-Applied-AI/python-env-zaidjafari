import pandas as pd
from pathlib import Path

# تحديد المسار لملف CSV بالنسبة لمكان السكريبت
data_path = Path(__file__).parent.parent / "data" / "sample.csv"

# تنفيذ التحليل المطلوب
df = pd.read_csv(data_path)
print("Shape:", df.shape)
print("-" * 20)
print("First 5 rows:")
print(df.head())
print("-" * 20)
print("Statistical Summary:")
print(df.describe())
