'''
Created on Nov 9, 2012

@author: Ash BOoth

'''

from sklearn.ensemble import RandomForestClassifier
import csv_io
import os
import math
import preprocess

def main():
    train = csv_io.read_data("{}/Data/train.csv".format(os.getcwd()), True)
    
    target = [float(x[0]) for x in train]
    
    # Remove the target from the training 
    train = [x[1:] for x in train]
    
    # Remove the categoricals that I can't convert
    for x in train:
        del x[1]
        del x[1]
        del x[5]
        del x[6]
    cats = preprocess.enum_categ_data(train, 'f', 10)
    preprocess.strf_to_floats(train, missing='average')
    
#    test = csv_io.read_data("{}/Data/test.csv".format(os.getcwd()), True)
#    
#    # Remove the categoricals that I can't convert
#    for x in test:
#        del x[1]
#        del x[1]
#        del x[5]
#        del x[6]

    # I can't just run enum_categ_data on test data, need to match the right cat to the right index!!!

#    cats = preprocess.enum_categ_data(test, 'f', 10)
#    preprocess.strf_to_floats(test, missing='average')
        

    rf = RandomForestClassifier(n_estimators=100, min_samples_split=2)
    rf.fit(train, target)
    
    print rf.score(train, target)
    
#    predicted_probs = rf.predict_proba(test)
#    predicted_probs = ["%f" % x[1] for x in predicted_probs]
#    csv_io.write_delimited_file("../Submissions/rf_benchmark.csv",
#                                predicted_probs)

if __name__ == "__main__":
    main()
