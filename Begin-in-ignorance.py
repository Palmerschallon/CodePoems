import numpy as np
from sklearn.linear_model import LinearRegression

# We begin in ignorance
X = np.random.rand(10, 1) * 10  # Our features
y = 2 * X + 1 + np.random.rand(10, 1)  # Our targets

# A mind, empty but for the capacity to learn
model = LinearRegression()

# Through experience,
model.fit(X, y)

# We glean knowledge
print("Learned coefficients:", model.coef_)

# And with knowledge, we predict, we understand
print("Predictions for the original inputs:", model.predict(X))
