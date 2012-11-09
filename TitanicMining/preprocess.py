'''
Created on Nov 9, 2012

@author: AshBooth
'''

def enum_categ_data(data, int_or_float, max_cats):
    '''
    Searches data for categorical data and changes to float/int form, also 
    returns a list of lists of the categories.
    
    The index of the category in a list represents its new float/int value

    '''
    cats = [[] for i in range(len(data[1]))]
    
    for obs in data:
        for (col, data_point) in enumerate(obs):
            try:
                float(data_point)
                continue
            except ValueError:
                # we know that we have a string
                if data_point != '':
                    if data_point not in cats[col]:
                        cats[col].append(data_point)
    
    for col in cats:
        if len(col) > max_cats: col = []
    
    for (row, obs) in enumerate(data):
        for (col, data_point) in enumerate(obs):
            if cats[col]:  # if we have some categories
                for (indx, cat) in enumerate(cats[col]):
                    if data_point == cat:
                        if int_or_float == 'f' or int_or_float == 'F':
                            data[row][col] = float(indx)
                        elif int_or_float == 'i' or int_or_float == 'I':
                            data[row][col] = int(indx)
                        else:
                            print "Must specify int_or_float as f or i"
                            return
    return cats             

def strf_to_floats(data, missing='average'):
    '''
    Takes a data as a list of lists of floats represented as strings and outputs 
    the data as a list of lists of floats
    
    Missing can be either 'average' or 'previous' (for time series)
    
    To do:
    - catch error if non-float data is received (while retaining ability to deal 
      with missing data)
    - How often does averaging the converted categorical make sense? Modal value?
    - What to do if 'previous' and the missing element is in the first observation?
    '''
    if missing == 'average' or missing == 'previous':
        missing_data = []
        col_sums = [0 for i in range(len(data[0]))]
        col_lengths = [0 for i in range(len(data[0]))]
        for(row, obs) in enumerate(data):
            for (col, data_point) in enumerate(obs):
                try:
                    data[row][col] = float(data_point)
                    col_sums[col] += float(data_point)
                    col_lengths[col] += 1
                except:
                    missing_data.append([row, col])
        if missing == 'average':
            col_avrgs = []
            for i in range(len(col_sums)):
                col_avrgs.append(col_sums[i] / float(col_lengths[i]))
            for val in missing_data:
                data[val[0]][val[1]] = col_avrgs[val[1]]
        else:  # assuming missing='previous'
            for val in missing_data:
                data[val[0]][val[1]] = data[val[0] - 1][val[1]]
    else:
        print "Missing must be set to 'average' or 'previous'"
    



