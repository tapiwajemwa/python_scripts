# This is a file script to rename file names given the names in a text file

import os

filepath = r'C:\Users\learning\Downloads\Complete Vue Developer in 2021 (w Vuex, Composition API, Router)\[TutsNode.com] - Complete Vue Developer in 2021 (w Vuex, Composition API, Router)'
filename = os.path.join(filepath,'Complete Vue Developer in 2021 (w Vuex, Composition API, Router).txt') 

#get the names of the files in the folder
def get_names(filepath):   
    '''This fuction collexts all the names of the files inside that path'''
    filenames = []
    for filename in os.listdir(filepath):
        if filename.endswith('.txt'):
            continue
        filenames.append(filename)
    filenames.sort()
    return filenames

#read files from text file
def read_file(filename):
    '''This funtion collect filenames saved inside a txt file'''
    new_filenames = []
    if os.path.exists(filename):
        with open(filename, encoding='utf-8') as f:
            for file in f.readlines():
                '''read the files inside a text file and format all the characters removing all those that are not wanted'''
                new_filenames.append(file.strip(' \n')
                                    .strip(' (5:55)')
                                    .replace(':','-' )
                                    .replace('"', '#')
                                    .replace('?','' )
                                    .replace('\\', '')
                                    .replace('/',' or '))
        return new_filenames
    else:
        print('nothing found')

# rename the files in the folder to a new name
def change_filename(filename, filepath):
    new_filenames = read_file(filename)
    old_filenames = get_names(filepath)

    for file in old_filenames:
        #get the index
        index = int(file.split('lesson')[1].split('.')[0])     
        new_filename = filepath +r'\{}. '.format(index)+ r'{}.mp4'.format(new_filenames[index-1])
        # rename the file
        os.rename(filepath + r'\{}'.format(file), new_filename)

change_filename(filename, filepath)