# update model by using db data
import numpy as np

from movieclassifier.vectorizer import vect
from .models import Review


def update_model(model, batch_size=10000):
    all_feedback = Review.objects.all()
    size = all_feedback.count()
    print(size)
    init = 0
    while init < size:
        useddatanum = min(size, init + batch_size)
        data_sentiment = np.array([data['sentiment'] for data in all_feedback[init:useddatanum].values('sentiment')])
        data_text = np.array([data['text'] for data in all_feedback[init:useddatanum].values('text')])
        X = data_text[:]
        y = data_sentiment[:].astype(int)
        classes = np.array([0, 1])
        X_train = vect.transform(X)
        model.partial_fit(X_train, y, classes=classes)
        init = useddatanum
    return model
