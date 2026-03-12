from sklearn.datasets import load_digits #, load_iris
from sklearn.model_selection import train_test_split
#from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt


# Load the Iris (flower petal) dataset
# iris = load_iris()
data = load_digits()
X, y = data.data, data.target
target_names = [str(n) for n in data.target_names]

# Visualize a few sample digit images
fig_samples, axes_samples = plt.subplots(2, 5, figsize=(10, 4))
for i, ax in enumerate(axes_samples.flat):
    ax.imshow(data.images[i], cmap='gray_r', interpolation='nearest')
    ax.set_title(f'Label: {y[i]}')
    ax.axis('off')
fig_samples.suptitle('Sample Digit Images from Dataset')
plt.tight_layout()
plt.savefig('plots/sample_digit_images.png', dpi=150, bbox_inches='tight')

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
for perc in [0, 80, 90, 95, 99, 100]:
    print(f"Percentage of class 2 removed from training set: {perc}%")
    # Filter out the specified percentage of virginica (class 2) from the training set
    np.random.seed(42)
    virginica_mask = y_train == 2
    virginica_indices = np.where(virginica_mask)[0]
    n_remove = int((perc / 100) * len(virginica_indices))
    remove_indices = np.random.choice(virginica_indices, size=n_remove, replace=False)
    keep_mask = np.ones(len(y_train), dtype=bool)
    keep_mask[remove_indices] = False

    X_train = X_train[keep_mask]
    y_train = y_train[keep_mask]

    # Histogram of y_train showing number of training samples per class
    fig_hist, ax_hist = plt.subplots(figsize=(7, 5))
    ax_hist.hist(y_train, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], align='left', rwidth=0.8, color='steelblue', edgecolor='black')
    ax_hist.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ax_hist.set_xticklabels(target_names)
    ax_hist.set_xlabel('Class')
    ax_hist.set_ylabel('Number of Training Samples')
    ax_hist.set_title('Distribution of Classes in y_train')
    plt.tight_layout()
    plt.savefig(f'plots/train_class_histogram_{perc}.png', dpi=150)

    # Train a Decision Tree classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Evaluate on the test set
    y_pred = clf.predict(X_test)

    # Stacked histogram of y_pred colored by y_test
    fig_pred, ax_pred = plt.subplots(figsize=(7, 5))

    # Separate y_pred by actual class (y_test)
    pred_by_actual = [y_pred[y_test == c] for c in range(10)]

    ax_pred.hist(pred_by_actual, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], align='left', rwidth=0.8,
                stacked=True, edgecolor='black',
                label=target_names, color=plt.cm.tab10(np.linspace(0, 1, 10)))
    ax_pred.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ax_pred.set_xticklabels(target_names, rotation=45)
    ax_pred.set_xlabel('Predicted Class (y_pred)')
    ax_pred.set_ylabel('Number of Samples')
    ax_pred.set_title('Distribution of Predictions (colored by actual class)')
    ax_pred.legend(title='Actual Class (y_test)', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f'plots/pred_vs_test_histogram_{perc}.png', dpi=150, bbox_inches='tight')

    print(f"Results for {perc}% removal of class 2:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=target_names))
