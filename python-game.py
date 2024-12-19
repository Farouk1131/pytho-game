import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
# from sklearn.metrics import accuracy_score
# from sklearn.ensemble import RandomForestClassifier
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# from tensorflow.keras.utils import to_categorical


# Load test and evaluation datasets
test_data = pd.read_csv("C:\Amr\Titanic\train.csv")
eval_data = pd.read_csv(f"C:\Amr\Titanic\eval.csv")
"C:\Amr\Titanic\train.csv"
# Display the first few rows of the test data
print(test_data.head())