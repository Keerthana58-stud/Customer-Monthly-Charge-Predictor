from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import mlflow
import mlflow.sklearn
from data_loader import fetch_data


df = fetch_data()
if df.empty:
    raise Exception("Data is empty")


# print("Columns:", df.columns.tolist())  # Debug line
# print(df.head())   

X=df.drop(columns=['monthly_charges', 'customer_id'])
y=df["monthly_charges"]



X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train,y_train)

score=model.score(X_test,y_test)


joblib.dump(model,"model.pkl")


with mlflow.start_run():
    mlflow.sklearn.log_model(model,"linear_model")
    mlflow.log_metric("r2_score",score)
print(f"Linear Regression model saved, R2 score: {score:.2f}")