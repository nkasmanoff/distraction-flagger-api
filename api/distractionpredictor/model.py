class TFIDF:
    def __init__(self):
        self.documents = None
        self.vocab = None
        self.idf = None
        self.tf = None
        self.tfidf = None

    def fit(self, documents):
        import numpy as np
        self.documents = documents
        self.vocab = list(set([word for doc in documents for word in doc.split()]))
        self.idf = np.zeros(len(self.vocab))
        self.tf = np.zeros((len(self.documents), len(self.vocab)))
        self.tfidf = np.zeros((len(self.documents), len(self.vocab)))
        for i, doc in enumerate(self.documents):
            for j, word in enumerate(self.vocab):
                self.tf[i, j] = doc.split().count(word) / len(doc.split())
                if self.tf[i, j] > 0:
                    self.idf[j] += 1
        self.idf = np.log(len(self.documents) / self.idf)
        self.tfidf = self.tf * self.idf
    
    def transform(self, documents):
        import numpy as np

        tfidf = np.zeros((len(documents), len(self.vocab)))
        for i, doc in enumerate(documents):
            for j, word in enumerate(self.vocab):
                tfidf[i, j] = doc.split().count(word) / len(doc.split()) * self.idf[j]
        return tfidf
    
    def fit_transform(self, documents):
        self.fit(documents)
        return self.tfidf
    
    def save_model(self, path):
        import dill
        with open(path, 'wb') as f:
            dill.dump(self, f)
        
    def load_model(self, path):
        import dill
        with open(path, 'rb') as f:
            self = dill.load(f)
        return self
    






class LogisticRegression:
    
    def __init__(self, learning_rate=0.01, n_iters=5000):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        import numpy as np
        # initialize weights and bias to zeros
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # gradient descent optimization
        for i in range(self.n_iters):
            # calculate predicted probabilities and cost
            z = np.dot(X, self.weights) + self.bias
            y_pred = self._sigmoid(z)
            cost = (-1 / n_samples) * np.sum(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
            
            # calculate gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))            
            db = (1 / n_samples) * np.sum(y_pred - y)
            
            # update weights and bias
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
    def predict(self, X,probabilities=False):
        import numpy as np
        # calculate predicted probabilities
        z = np.dot(X, self.weights) + self.bias
        y_pred = self._sigmoid(z)
        if probabilities:
            return y_pred
        
        # convert probabilities to binary predictions
        return np.round(y_pred).astype(int)

    def _sigmoid(self, z):
        import numpy as np
        return 1 / (1 + np.exp(-z))
    
    def save_model(self, path):
        import dill
        with open(path, 'wb') as f:
            dill.dump(self, f)

    def load_model(self, path):
        import dill
        with open(path, 'rb') as f:
            self = dill.load(f)
        return self
    

