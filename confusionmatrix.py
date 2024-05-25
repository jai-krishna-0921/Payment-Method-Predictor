import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

file_path = r'C:\Users\jai krishna\Desktop\Documents\college\ds lab\IDSE Project\normalized_data.xlsx'
data = pd.read_excel(file_path)

# Assuming you have a dataset loaded into X (features) and y (labels)
# Example dataset (replace with your actual data)
features = ['gender', 'year of study', 'average amount spent']
X = data[features]
y = data['how they make payments']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizing the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Training the SVM model
svm_model = SVC(kernel='linear', C=1)  # Adjust the kernel and C parameter as needed
svm_model.fit(X_train, y_train)

# Making predictions
y_pred = svm_model.predict(X_test)

# Computing the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Printing the confusion matrix
print("Confusion Matrix:")
print(cm)

# Printing the classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Printing the accuracy score
print("Accuracy Score:")
print(accuracy_score(y_test, y_pred))

# Visualizing the confusion matrix
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=svm_model.classes_, yticklabels=svm_model.classes_)
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

# Analyzing feature importance
if hasattr(svm_model, 'coef_'):
    feature_importance = pd.DataFrame({
        'Feature': features,
        'Coefficient': svm_model.coef_[0]
    }).sort_values(by='Coefficient', ascending=False)

    print("\nFeature Importance:")
    print(feature_importance)

    # Visualizing feature importance
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Coefficient', y='Feature', data=feature_importance, palette='viridis')
    plt.title('Feature Importance Based on SVM Coefficients')
    plt.xlabel('Coefficient Value')
    plt.ylabel('Feature')
    plt.show()
else:
    print("The SVM model does not have coefficients attribute. Use a linear kernel SVM for feature importance.")