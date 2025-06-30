# Step 1: Import libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 2: Load dataset
iris = load_iris()
X = iris.data      # Features: Sepal and petal measurements
y = iris.target    # Target: Species (0=setosa, 1=versicolor, 2=virginica)

# Step 3: Split dataset (train 80%, test 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Step 5: Predict and evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Step 6: Show results
print("Predictions:", y_pred)
print("Actual     :", y_test)
print("Accuracy   :", accuracy)
