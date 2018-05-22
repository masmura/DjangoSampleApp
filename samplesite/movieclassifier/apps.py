from django.apps import AppConfig
import os
import pickle


class MovieclassifierConfig(AppConfig):
    name = 'movieclassifier'
    cur_dir = os.path.dirname(__file__)
    clf = pickle.load(
        open(os.path.join(cur_dir,
                          'pkl_objects',
                          'classifier.pkl'),
             'rb'))

    def ready(self):
        from movieclassifier.update import update_model
        self.clf = update_model(self.clf)
