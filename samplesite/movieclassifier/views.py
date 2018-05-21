from django.shortcuts import render
from django import forms

from .models import Review

######### ï™óﬁäÌÇÃèÄîı ###############
from .vectorizer import vect
import pickle
import os
import numpy as np

cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'rb'))
def classify(document):
	label = {0: 'negative', 1: 'positive'}
	X = vect.transform([document])
	y = clf.predict(X)[0]
	proba = clf.predict_proba(X).max()
	return label[y], proba
	
def train(document, y):
    X = vect.transform([document])
    clf.partial_fit(X, [y])

########################################

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ('text',)

def index(request):
	form = ReviewForm()
	return render(request, 'movieclassifier/reviewform.html', {'form': form})

def results(request):
	if request.method == "POST":
		form = ReviewForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			y, proba = classify(post.text)
			return render(request, 'movieclassifier/results.html', {'content':post.text, 'prediction':y, 'probability':proba})
	return render(request, 'movieclassifier/reviewform.html', {'form': form})

def feedback(request):
	if request.method == "POST":
		feedback = request.POST['feedback_button']
		review = request.POST['review']
		prediction = request.POST['prediction']

		inv_label = {'negative':0, 'positive':1}
		y = inv_label[prediction]
		if feedback == 'Incorrect':
			y = int(not(y))
		train(review, y)
		review_db = Review()
		review_db.text = review
		review_db.sentiment = y
		review_db.save()
		return render(request, 'movieclassifier/thanks.html')
	form = ReviewForm()
	return render(request, 'movieclassifier/reviewform.html', {'form', form})