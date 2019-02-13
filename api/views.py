import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.metrics import fbeta_score
from sklearn.metrics import accuracy_score

# Django
from django.shortcuts import render
import datetime
import time
from datetime import datetime

# Serializer
from .serializers import UpdateSerializer, HistorySerializer

# Model
from .models import update_table, history_table

# RestFramework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets

#Uploading data
class upload_data(generics.CreateAPIView):
    model = update_table
    serializer_class = UpdateSerializer

    def post(self, request, *args, **kwargs):
        
        #Get serializer
        self.wine_data = []
        serializer = self.get_serializer(data = request.data)
        
        #Check if serializer is valid
        if serializer.is_valid():
            #If valid, create new user
            serializer.save()
            ph =  serializer.data.get('ph')
            alcohol_content = serializer.data.get('alcohol_content')
            temperature = serializer.data.get('temperature')
            volatile_acid = serializer.data.get('volatile_acid')

            self.wine_data = [ph, alcohol_content, temperature, volatile_acid]
            self.prediction()

            results = history_table(ph = ph, alcohol_content = alcohol_content, temperature = temperature, volatile_acid = volatile_acid, rating = self.result)
            results.save()

            return Response({'rating': "rate:" + self.result}, status=status.HTTP_201_CREATED)
    
    def prediction(self):
        # Load the Wines dataset
        data = pd.read_csv("api/newFile.csv")
        n_wines = data.shape[0]

        # Number of wines with quality rating above 6
        quality_above_6 = data.loc[(data['quality'] > 6)]
        n_above_6 = quality_above_6.shape[0]

        # Number of wines with quality rating below 5
        quality_below_5 = data.loc[(data['quality'] < 5)]
        n_below_5 = quality_below_5.shape[0]

        # Number of wines with quality rating between 5 to 6
        quality_between_5 = data.loc[(data['quality']) >= 5 & (data['quality'] <= 6)]
        n_between_5 = quality_between_5.shape[0]

        #Defining the splits for categories. 1-4 will be poor quality, 5-6 will be average, 7-10 will be great
        bins = [1,4,6,10]

        #0 for low quality, 1 for average, 2 for great quality
        #quality_labels=[0,1,2]
        quality_labels=["Poor","Average","Great"]
        data['quality_categorical'] = pd.cut(data['quality'], bins=bins, labels=quality_labels, include_lowest=True)

        # Split the data into features and target label
        quality_raw = data['quality_categorical']
        features_raw = data.drop(['quality', 'quality_categorical'], axis = 1)

        # Classifier
        # TODO: Initialize the classifier
        clf = RandomForestClassifier(max_depth=None, random_state=None)
        parameters = {'n_estimators': [100], 'max_features':[None], 'max_depth': [None]}

        # TODO: Make an fbeta_score scoring object using make_scorer()
        scorer = make_scorer(fbeta_score, beta=0.5, average="micro")

        # TODO: Perform grid search on the classifier using 'scorer' as the scoring method using GridSearchCV()
        grid_obj = GridSearchCV(clf, parameters, scoring=scorer)

        # TODO: Fit the grid search object to the training data and find the optimal parameters using fit()
        grid_fit = grid_obj.fit(features_raw, quality_raw)

        # Get the estimator
        best_clf = grid_fit.best_estimator_

        # Make predictions using the unoptimized and model
        #  predictions = (clf.fit(features_raw, quality_raw)).predict(X_test)
        # best_predictions = best_clf.predict(X_test)
        
        #Testing
        wine_data = [[self.wine_data[0], self.wine_data[1], self.wine_data[2], self.wine_data[3]]]
        print(best_clf.predict(wine_data))
        self.result = ""
        self.result = best_clf.predict(wine_data)

        # Show predictions
        #for i, quality in enumerate(best_clf.predict(wine_data)):
            #print("Predicted quality for Wine {} is: {}".format(i+1, quality))
          

#Listing the results value
class result_list(generics.ListAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        return history_table.objects.all()

#Updating the values on table
class update_list(generics.UpdateAPIView):
    serializer_class = UpdateSerializer

    lookup_field = 'id'
    queryset = update_table.objects.all()

    def update(self, request, *args, **kwargs):

        serializer = UpdateSerializer(data=request.data)

        if serializer.is_valid():   
            serializer.save()

        #values stored in history_table
            ph = serializer.data.get('ph')
            alcohol = serializer.data.get('alcohol_content')
            temperature = serializer.data.get('temperature')
            volatile = serializer.data.get('volatile_acid')

            results = history_table(ph = ph, alcohol_content = alcohol, temperature = temperature, volatile_acid = volatile)
            results.save()
            

        return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#

class delete_history(APIView):

    def get_object(self, pk):
        try:
            return history_table.objects.get(pk=pk)
        except history_table.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        return self.destroy(request, pk)

    def destroy(self, request, pk, format=None):
        
        instance = self.get_object(pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()


