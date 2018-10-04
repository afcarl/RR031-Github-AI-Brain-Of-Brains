# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 12:34:58 2018

@author: afcarl
"""

import json
import os, sys
import uuid
from collections import defaultdict
from shutil import copyfile
from shutil import make_archive
import shutil
from copy import deepcopy

import time

#import unicodedata        

def zpickle( obj, fname ):
    import pickle, gzip
    pickle.dump(obj=obj, file=gzip.open(fname, 'wb', compresslevel=3), protocol=2)

def zunpickle( fname ):
    import pickle, gzip
    return pickle.load(gzip.open(fname, "rb"))




#===========================
#===========================
i_1000_flag = 1
#i_1000_flag = 0
#===========================
#===========================



        
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read zpkl files
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#zpickle( doc_title_Similar_dict , 'doc_title_Similar_dict.zpkl' )
if i_1000_flag == 0:
    doc_title_Similar_dict = zunpickle( 'doc_title_Similar_dict.zpkl' )
else:
    doc_title_Similar_dict = zunpickle( 'doc_title_Similar_dict_1000.zpkl' )

#zpickle( doc_title_Similar_TAGS_dict , 'doc_title_Similar_TAGS_dict.zpkl' )
if i_1000_flag == 0:
    doc_title_Similar_TAGS_dict = zunpickle( 'doc_title_Similar_TAGS_dict.zpkl' )
else:
    doc_title_Similar_TAGS_dict = zunpickle( 'doc_title_Similar_TAGS_dict_1000.zpkl' )

#zpickle( doc_title_Similar_TAGS_dict_all , 'doc_title_Similar_TAGS_dict_all.zpkl' )
if i_1000_flag == 0:
    doc_title_Similar_TAGS_dict_all = zunpickle( 'doc_title_Similar_TAGS_dict_all.zpkl' )
else:
    doc_title_Similar_TAGS_dict_all = zunpickle( 'doc_title_Similar_TAGS_dict_all_1000.zpkl' )

keys_Similar = doc_title_Similar_TAGS_dict.keys()
#print("keys_Similar = ", keys_Similar)
#print("len(keys_Similar) = ", len(keys_Similar) )
TAG_Similar_set = set()
for i_key in keys_Similar:
    for i_TAG in doc_title_Similar_TAGS_dict[ i_key ]:
    
        if i_TAG.isnumeric():
            continue
        
        TAG_Similar_set.add( i_TAG )
    
TAG_Similar_list = list( TAG_Similar_set )
TAG_Similar_list.sort()
#print("TAG_Similar_list = ", TAG_Similar_list)
#print("len(TAG_Similar_set) = ", len(TAG_Similar_set) )
#sys.exit(0)

forked_author_list = []
#zpickle( forked_author_dict , 'forked_author_dict.zpkl' )
if i_1000_flag == 0:
    forked_author_dict = zunpickle( 'forked_author_dict.zpkl' )
else:
    forked_author_dict = zunpickle( 'forked_author_dict_1000.zpkl' )
keys_forked_author_dict = forked_author_dict.keys()
for i_title in keys_forked_author_dict:
    #forked_author_list.append( forked_author_dict[ i_title ] )
    forked_author_list.append( list(forked_author_dict[ i_title ]) )
forked_author_list.sort()
#print("forked_author_list = ", forked_author_list)
#print("len(forked_author_list) = ", len(forked_author_list))
#print("len(keys_forked_author_dict) = ", len(keys_forked_author_dict))
#sys.exit(0)

forked_author_to_titles_dict = defaultdict(list)
forked_author_to_titles_dict_tmp = defaultdict(list)
if i_1000_flag == 0:
    #forked_author_to_titles_dict = zunpickle( 'forked_author_to_titles_dict.zpkl' )
    forked_author_to_titles_dict_tmp = zunpickle( 'forked_author_to_titles_dict.zpkl' )
else:
    #forked_author_to_titles_dict = zunpickle( 'forked_author_to_titles_dict_1000.zpkl' )
    forked_author_to_titles_dict_tmp = zunpickle( 'forked_author_to_titles_dict_1000.zpkl' )
#keys_forked_author_to_titles_dict = forked_author_to_titles_dict.keys()
keys_forked_author_to_titles_dict = forked_author_to_titles_dict_tmp.keys()
#print("keys_forked_author_to_titles_dict = ", keys_forked_author_to_titles_dict)
i_max = -99999
for i_key_tmp in keys_forked_author_to_titles_dict:
    #print("i_key_tmp = ", i_key_tmp)
    #print("i_key_tmp = ", i_key_tmp)
    list_tmp = []
    #for i_title_list_tmp in forked_author_to_titles_dict[ i_key_tmp ]:
    for i_title_list_tmp in forked_author_to_titles_dict_tmp[ i_key_tmp ]:
        #print("i_title_list_tmp = ", i_title_list_tmp)
        #print("type(i_title_list_tmp) = ", type(i_title_list_tmp))
        #if i_key_tmp == "EricSchles":
        #    print(i_key_tmp)
        #    print(forked_author_to_titles_dict_tmp[ i_key_tmp ])
        #    print(len(forked_author_to_titles_dict_tmp[ i_key_tmp ]))
        #    #sys.exit(0)
        
        if len( i_title_list_tmp ) == 0:
            #print("i_key_tmp = ", i_key_tmp)
            #print("i_title_list_tmp = ", i_title_list_tmp)
            #print("type(i_title_list_tmp) = ", type(i_title_list_tmp))
            #sys.exit(0)
            pass
        else:
            list_tmp.append( i_title_list_tmp )
    forked_author_to_titles_dict[ i_key_tmp ] = list_tmp
    #print("len( forked_author_to_titles_dict[ i_key_tmp ] ) = ", len(forked_author_to_titles_dict[ i_key_tmp ] ))
    if i_max < len( list_tmp ):
        i_max = len( list_tmp )
    #    print("i_max = ", i_max , i_key_tmp , list_tmp )
#print("i_max = ", i_max)
#sys.exit(0)


#zpickle( doc_title_DisSimilar_dict , 'doc_title_DisSimilar_dict.zpkl' )
if i_1000_flag == 0:
    doc_title_DisSimilar_dict = zunpickle( 'doc_title_DisSimilar_dict.zpkl' )
else:
    doc_title_DisSimilar_dict = zunpickle( 'doc_title_DisSimilar_dict_1000.zpkl' )

#zpickle( doc_title_DisSimilar_TAGS_dict , 'doc_title_DisSimilar_TAGS_dict.zpkl' )
if i_1000_flag == 0:
    doc_title_DisSimilar_TAGS_dict = zunpickle( 'doc_title_DisSimilar_TAGS_dict.zpkl' )
else:
    doc_title_DisSimilar_TAGS_dict = zunpickle( 'doc_title_DisSimilar_TAGS_dict_1000.zpkl' )

#zpickle( doc_title_DisSimilar_TAGS_dict_all , 'doc_title_DisSimilar_TAGS_dict_all.zpkl' )
if i_1000_flag == 0:
    doc_title_DisSimilar_TAGS_dict_all = zunpickle( 'doc_title_DisSimilar_TAGS_dict_all.zpkl' )
else:
    doc_title_DisSimilar_TAGS_dict_all = zunpickle( 'doc_title_DisSimilar_TAGS_dict_all_1000.zpkl' )
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read zpkl files
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in list of Repo titles
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#if 0==1:
if 1==1:
    path_set = set()
    if i_1000_flag == 0:
        input = open( 'output_all_081618.dat' , 'r' )
    else:
        input = open( 'output_081918_1000.dat' , 'r' )
    test_input = input.readline()
    while test_input:
        i_find = test_input.rfind( '\\' )
        string = test_input[0:i_find]
        #print("test_input = ", test_input)
        #print("string = ", string)
        #sys.exit(0)
        if ( string.find('\\.git') == -1 ) and \
           ( string.find('L:\\Local_Git\\000_tmp') == -1 ) and \
           ( string.find('L:\\Local_Git\\00_gitim-master') == -1 ) and \
           ( string.find('L:\\Local_Git\\0_MD') == -1 ) and \
           ( string.find('L:\\Local_Git\\0_hold') == -1 ) and \
           ( string.find('__pycache__') == -1 ) and \
           ( len(string.split('\\')) == 3 ):
            #path_set.add(string)
            #path_set.add( string[string.rfind('\\'):-1])
            path_set.add( (string.split('\\'))[2] )
        try:
            test_input = input.readline()
        except:
            print("ERROR: ", test_input)
            test_input = input.readline()
    input.close()
    #print("len(path_set) = ", len(path_set))
    #sys.exit(0)

    if i_1000_flag == 0:
        output = open( 'output_all_081618.out' , 'w' )
    else:
        output = open( 'output_all_081618_1000.out' , 'w' )
    list_tmp = list(path_set)
    list_tmp.sort()
    for i in list_tmp:
        output.write( str(i) + '\n')
    output.close()
    #sys.exit(0)

    repo_names_list = []
    if i_1000_flag == 0:
        input_name = open( 'output_all_081618.out' , 'r' )
    else:
        #input_name = open( 'output_all_081618_1000.out' , 'r' )
        input_name = open( 'output_081918_1000.dat' , 'r' )
    test_input = input_name.readline()
    while test_input:
        repo_names_list.append( test_input.strip('\n') )
        test_input = input_name.readline()
    input_name.close()
    repo_names_list.sort()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in list of Repo titles
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++






#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source & Destination folder names
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
REF_dir = "./0_REF/"


results_dir = "./results/"
if not os.path.exists( results_dir ):
    os.mkdir( results_dir )
else:
    for the_file in os.listdir(results_dir):
        file_path = os.path.join(results_dir, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)    
#sys.exit(0)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source & Destination folder names
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    
    
    
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Ignore this for now
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
BrainId_NEW = str(uuid.uuid4())
i_BrainId_NEW_flag = 0
#i_BrainId_NEW_flag = 1
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Ignore this for now
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in all filenames
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
filename_access = 'access.json'
filename_attachments = 'attachments.json'
filename_brainusers = 'brainusers.json'
filename_calendarevents = 'calendarevents.json'
filename_links = 'links.json'
filename_meta = 'meta.json'
filename_modificationlogs = 'modificationlogs.json'
filename_settings = 'settings.json'
filename_syncpoints = 'syncpoints.json'
filename_thoughts = 'thoughts.json'
filename_tombstones = 'tombstones.json'

list_access = []
list_attachments = []
list_brainusers = []
list_calendarevents = []
list_links = []
list_meta = []
list_modificationlogs = []
list_settings = []
list_syncpoints = []
list_thoughts = []
list_tombstones = []

#dict_access = defaultdict()
dict_attachments = defaultdict()
dict_brainusers = defaultdict()
dict_calendarevents = defaultdict()
dict_links = defaultdict()
dict_meta = defaultdict()
dict_modificationlogs = defaultdict()
dict_settings = defaultdict()
dict_syncpoints = defaultdict()
dict_thoughts = defaultdict()
dict_tombstones = defaultdict()

author_already_included_set = set()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in all filenames
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





if i_1000_flag == 0:
    output_tmp = open("output.dat",'w')
else:
    output_tmp = open("output_1000.dat",'w')






    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Ignore this for now
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
first_time_flag = 0
#first_time_flag = 1

keys_set = set()
values_set = set()
values_dict = defaultdict(set)

if first_time_flag == 1:
    keys_set = zunpickle( 'keys_set.zpkl' )
    values_set = zunpickle( 'values_set.zpkl' )
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Ignore this for now
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source "access" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_access
#   {"CreationDateTime":    "2018-08-14T19:17:07.2700612",
#   "ModificationDateTime": "2018-08-14T19:17:07.2700612",
#   "AccessorId":           "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "BrainId":              "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "AccessType":           3,
#   "Id":                   "4c0b32d2-c76c-47cd-a3b2-9eac4870ec61"}
try:
    #list_access = []
    input = open( REF_dir + filename_access, encoding='utf-8-sig' )
    test_input = input.readline()
    while test_input:
        dict_access = defaultdict()
        data_access = json.loads(test_input.strip('\n'))
        list_access.append( data_access )
        #print("data_access = ", data_access )
        for p in data_access:
            #print(p , data_access[p])
            dict_access[ p ] = data_access[p]
            if first_time_flag == 0:
                keys_set.add(p + '_' + filename_access)
                values_set.add(data_access[p])
            else:
                #values_dict[ data_access[p] ].add( p + '_' + filename_access )
                values_dict[ str(data_access[p]) ].add( p + '_' + filename_access )
            if p == "BrainId" and i_BrainId_NEW_flag == 1:
                #print(p , data_access[p])
                data_access[p] = BrainId_NEW
                #print(p , data_access[p])
                #sys.exit(0)
        #list_access.append( dict_access )
        #sys.exit(0)
        test_input = input.readline()
    input.close()
except:
    pass
#print("list_access = ",list_access)
#print("len(list_access) = ", len(list_access))
#sys.exit(0)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source "access" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





        
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source "attachments" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_attachments
#    {"SourceId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "Name":"wallpaper.png",
#   "Position":0.0,
#   "Type":1,
#   "DataLength":271417,
#   "Location":"wallpaper.png",
#   "IsIcon":false,
#   "SourceType":1,
#   "IsWallpaper":true,
#   "CreationDateTime":"2018-08-14T19:17:08.212115",
#   "ModificationDateTime":"2018-08-14T19:17:08.212115",
#   "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "Id":"2355e239-50ab-41cc-84b2-b124dcfd5e3a"}
try:
    #list_attachments = []
    input = open( REF_dir + filename_attachments, encoding='utf-8-sig' )
    test_input = input.readline()
    while test_input:
        data_attachments = json.loads(test_input.strip('\n'))
        list_attachments.append( data_attachments )
        #print("data_attachments = ", data_attachments )
        for p in data_attachments:
            #print(p , data_attachments[p])
            if first_time_flag == 0:
                keys_set.add(p + '_' + filename_attachments)
                values_set.add(data_attachments[p])
            else:
                #values_dict[ data_attachments[p] ].add( p + '_' + filename_attachments )
                values_dict[ str(data_attachments[p]) ].add( p + '_' + filename_attachments )
            if p == "BrainId" and i_BrainId_NEW_flag == 1:
                #print(p , data_access[p])
                data_attachments[p] = BrainId_NEW
                #print(p , data_access[p])
                #sys.exit(0)
        #sys.exit(0)
        test_input = input.readline()
    input.close()
except:
    pass
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source "attachments" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++







 
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source "brainusers" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_brainusers
#   {"UserId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "Username":"xxxxxxxx",
#   "EmailAddress":"xxxxxxxx@xxxxxxxxxx.xxx",
#   "FirstName":"xxxxxxxxxx",
#   "LastName":"xxxxxxxxxx",
#   "CreationDateTime":"2018-08-14T19:17:07.4960741",
#   "ModificationDateTime":"2018-08-14T19:17:07.4960741",
#   "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "Id":"c274c674-35e7-4fdb-8a6b-f1d6ad1b99fc"}
'''brainusers_dict = defaultdict()  
brainusers_dict[ "UserId" ]               = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
brainusers_dict[ "Username" ]             = "xxxxxxxx"
brainusers_dict[ "EmailAddress" ]         = "xxxxxxxx@xxxxxxxxxx.xxx"
brainusers_dict[ "FirstName" ]            = "xxxxxxxxxx"
brainusers_dict[ "LastName" ]             = "xxxxxxxxxx"
brainusers_dict[ "CreationDateTime" ]     = "2018-08-14T19:17:07.4960741"
brainusers_dict[ "ModificationDateTime" ] = "2018-08-14T19:17:07.4960741"
brainusers_dict[ "BrainId" ]              = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
brainusers_dict[ "Id" ]                   = "c274c674-35e7-4fdb-8a6b-f1d6ad1b99fc"'''


try:
    #list_brainusers = []
    input = open( REF_dir + filename_brainusers, encoding='utf-8-sig' )
    test_input = input.readline()
    while test_input:
        data_brainusers = json.loads(test_input.strip('\n'))
        list_brainusers.append( data_brainusers )
        #print("data_brainusers = ", data_brainusers )
        '''for p in data_brainusers:
            #print(p , data_brainusers[p])
            if first_time_flag == 0:
                keys_set.add(p + '_' + filename_brainusers)
                values_set.add(data_brainusers[p])
            else:
                #values_dict[ data_brainusers[p] ].add( p + '_' + filename_brainusers )
                values_dict[ str(data_brainusers[p]) ].add( p + '_' + filename_brainusers )
            if p == "BrainId" and i_BrainId_NEW_flag == 1:
                #print(p , data_access[p])
                data_brainusers[p] = BrainId_NEW
                #print(p , data_access[p])'''
                #sys.exit(0)
        #sys.exit(0)
        test_input = input.readline()
    input.close()
except:
    pass

brainusers_dict = defaultdict()  
brainusers_dict[ "UserId" ]               = data_brainusers[ "UserId" ]
brainusers_dict[ "Username" ]             = data_brainusers[ "Username" ]
brainusers_dict[ "EmailAddress" ]         = data_brainusers[ "EmailAddress" ]
brainusers_dict[ "FirstName" ]            = data_brainusers[ "FirstName" ]
brainusers_dict[ "LastName" ]             = data_brainusers[ "LastName" ]
brainusers_dict[ "CreationDateTime" ]     = data_brainusers[ "CreationDateTime" ]
brainusers_dict[ "ModificationDateTime" ] = data_brainusers[ "ModificationDateTime" ]
brainusers_dict[ "BrainId" ]              = data_brainusers[ "BrainId" ]
brainusers_dict[ "Id" ]                   = data_brainusers[ "Id" ]
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source "brainusers" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++








#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source "calendarevents" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_calendarevents
#    <NONE>
try:
    #list_calendarevents = []
    input = open( REF_dir + filename_calendarevents, encoding='utf-8-sig' )
    test_input = input.readline()
    while test_input:
        data_calendarevents = json.loads(test_input.strip('\n'))
        list_calendarevents.append( data_calendarevents )
        #print("data_calendarevents = ", data_calendarevents )
        for p in data_calendarevents:
            #print(p , data_calendarevents[p])
            if first_time_flag == 0:
                keys_set.add(p + '_' + filename_calendarevents)
                values_set.add(data_calendarevents[p])
            else:
                #values_dict[ data_calendarevents[p] ].add( p + '_' + filename_calendarevents )
                values_dict[ str(data_calendarevents[p]) ].add( p + '_' + filename_calendarevents )
            if p == "BrainId" and i_BrainId_NEW_flag == 1:
                #print(p , data_access[p])
                data_calendarevents[p] = BrainId_NEW
                #print(p , data_access[p])
                #sys.exit(0)
        #sys.exit(0)
        test_input = input.readline()
    input.close()
except:
    pass
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source "calendarevents" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++







#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source "links" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_links
#   {"ThoughtIdA":"adc04f73-27d0-45fa-a35f-fab180ed667f",
#   "ThoughtIdB":"e39f3a4b-ad3c-4bae-9f09-573c16831ee3",
#   "Kind":1,
#   "Relation":1,
#   "Direction":-1,
#   "Meaning":1,
#   "Thickness":-1,
#   "CreationDateTime":"2018-08-14T19:18:32.4149312",
#   "ModificationDateTime":"2018-08-14T19:18:32.4149312",
#   "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "Id":"01784602-e955-4e0d-a6c4-f317c35f3e55"}
try:
    #list_links = []
    input = open( REF_dir + filename_links, encoding='utf-8-sig' )
    test_input = input.readline()
    while test_input:
        data_links = json.loads(test_input.strip('\n'))
        list_links.append( data_links )
        #print("data_links = ", data_links )
        for p in data_links:
            #print(p , data_links[p])
            if first_time_flag == 0:
                keys_set.add(p + '_' + filename_links)
                values_set.add(data_links[p])
            else:
                #values_dict[ data_links[p] ].add( p + '_' + filename_links )
                values_dict[ str(data_links[p]) ].add( p + '_' + filename_links )
            if p == "BrainId" and i_BrainId_NEW_flag == 1:
                #print(p , data_access[p])
                data_links[p] = BrainId_NEW
                #print(p , data_access[p])
                #sys.exit(0)
        #sys.exit(0)
        test_input = input.readline()
    input.close()
except:
    pass
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source "links" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++







#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source "meta" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_meta
#   {"BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "ExchangeFormatVersion":4,
#   "AttachmentFileStates":{"2355e239-50ab-41cc-84b2-b124dcfd5e3a":1}}
try:
    #list_meta = []
    input = open( REF_dir + filename_meta, encoding='utf-8-sig' )
    test_input = input.readline()
    while test_input:
        data_meta = json.loads(test_input.strip('\n'))
        list_meta.append( data_meta )
        #print("data_meta = ", data_meta )
        '''for p in data_meta:
            #print(p , data_meta[p])
            if first_time_flag == 0:
                keys_set.add(p + '_' + filename_meta)
                values_set.add(data_meta[p])
            else:
                #values_dict[ data_meta[p] ].add( p + '_' + filename_meta )
                values_dict[ str(data_meta[p]) ].add( p + '_' + filename_meta )
            if p == "BrainId" and i_BrainId_NEW_flag == 1:
                #print(p , data_access[p])
                data_meta[p] = BrainId_NEW
                #print(p , data_access[p])
                #sys.exit(0)'''
        #sys.exit(0)
        test_input = input.readline()
    input.close()
except:
    pass
#sys.exit(0)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source "meta" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++






#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source "modificationlogs" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_modificationlogs
#   {"SourceId":"3d6948d3-c906-5f08-9199-83b4214cbb53",
#   "SourceType":5,
#   "ExtraAId":"00000000-0000-0000-0000-000000000000",
#   "ExtraAType":-1,
#   "ExtraBId":"00000000-0000-0000-0000-000000000000",
#   "ExtraBType":-1,
#   "ModType":101,
#   "NewValue":"-2362881",
#   "UserId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "CreationDateTime":"2018-08-14T19:17:07.6330819",
#   "ModificationDateTime":"2018-08-14T19:17:07.6330819",
#   "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "Id":"166f6201-c36a-4812-b2a7-15de910c8f40"}
try:
    #list_modificationlogs = []
    input = open( REF_dir + filename_modificationlogs, encoding='utf-8-sig' )
    test_input = input.readline()
    while test_input:
        data_modificationlogs = json.loads(test_input.strip('\n'))
        list_modificationlogs.append( data_modificationlogs )
        #print("data_modificationlogs = ", data_modificationlogs )
        for p in data_modificationlogs:
            #print(p , data_modificationlogs[p])
            if first_time_flag == 0:
                keys_set.add(p + '_' + filename_modificationlogs)
                values_set.add(data_modificationlogs[p])
            else:
                #values_dict[ data_modificationlogs[p] ].add( p + '_' + filename_modificationlogs )
                values_dict[ str(data_modificationlogs[p]) ].add( p + '_' + filename_modificationlogs )
            if p == "BrainId" and i_BrainId_NEW_flag == 1:
                #print(p , data_access[p])
                data_modificationlogs[p] = BrainId_NEW
                #print(p , data_access[p])
                #sys.exit(0)
        #sys.exit(0)
        test_input = input.readline()
    input.close()
except:
    pass
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source "modificationlogs" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source "settings" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_settings
#   {"Value":"-1",
#   "CreationDateTime":"2018-08-14T19:17:07.7830905",
#   "ModificationDateTime":"2018-08-14T19:17:07.7830905",
#   "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "Id":"074d8805-aeb4-5814-8509-7ef66cb3e56c"}
try:
    #list_settings = []
    input = open( REF_dir + filename_settings, encoding='utf-8-sig' )
    test_input = input.readline()
    while test_input:
        data_settings = json.loads(test_input.strip('\n'))
        list_settings.append( data_settings )
        #print("data_settings = ", data_settings )
        for p in data_settings:
            #print(p , data_settings[p])
            if first_time_flag == 0:
                keys_set.add(p + '_' + filename_settings)
                values_set.add(data_settings[p])
            else:
                #values_dict[ data_settings[p] ].add( p + '_' + filename_settings )
                values_dict[ str(data_settings[p]) ].add( p + '_' + filename_settings )
            if p == "BrainId" and i_BrainId_NEW_flag == 1:
                #print(p , data_access[p])
                data_settings[p] = BrainId_NEW
                #print(p , data_access[p])
                #sys.exit(0)
        #sys.exit(0)
        test_input = input.readline()
    input.close()
except:
    pass
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source "settings" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source "syncpoints" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_syncpoints
#   {"CreationDateTime":"2018-08-14T19:17:07.3970684",
#   "ModificationDateTime":"2018-08-14T19:17:07.3970684",
#   "SyncUpdateId":"5d4ae0d1-b79a-47a2-8312-1aff59d514b6",
#   "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "Id":"5d4ae0d1-b79a-47a2-8312-1aff59d514b6"}
try:
    #list_syncpoints = []
    input = open( REF_dir + filename_syncpoints, encoding='utf-8-sig' )
    test_input = input.readline()
    while test_input:
        data_syncpoints = json.loads(test_input.strip('\n'))
        list_syncpoints.append( data_syncpoints )
        #print("data_syncpoints = ", data_syncpoints )
        for p in data_syncpoints:
            #print(p , data_syncpoints[p])
            if first_time_flag == 0:
                keys_set.add(p + '_' + filename_syncpoints)
                values_set.add(data_syncpoints[p])
            else:
                #values_dict[ data_syncpoints[p] ].add( p + '_' + filename_syncpoints )
                values_dict[ str(data_syncpoints[p]) ].add( p + '_' + filename_syncpoints )
            if p == "BrainId" and i_BrainId_NEW_flag == 1:
                #print(p , data_access[p])
                data_syncpoints[p] = BrainId_NEW
                #print(p , data_access[p])
                #sys.exit(0)
        #sys.exit(0)
        test_input = input.readline()
    input.close()
except:
    pass
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source "syncpoints" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source "thoughts" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_thoughts
#   {"Name":"test_export",
#   "ActivationDateTime":"2018-08-14T19:18:47.9528199",
#   "ACType":0,
#   "Kind":1,
#   "TagIds":[],
#   "ThoughtIconInfo":"1::0:False:False:0",
#   "CreationDateTime":"2018-08-14T19:17:07.3530659",
#   "ModificationDateTime":"2018-08-14T19:17:07.3530659",
#   "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
#   "Id":"0940d0f5-e467-4a8b-aaf8-407c7848aa1a"}
try:
#if 1==1:
    #list_thoughts = []
    #data_thoughts = defaultdict()
    input = open( REF_dir + filename_thoughts, encoding='utf-8-sig' )
    test_input = input.readline()
    while test_input:
        data_thoughts = json.loads(test_input.strip('\n'))
        list_thoughts.append( data_thoughts )
        #print("data_thoughts = ", data_thoughts )
        '''for p in data_thoughts:
            #print(p , data_thoughts[p])
            if first_time_flag == 0:
                keys_set.add(p + '_' + filename_thoughts)
                values_set.add(data_thoughts[p])
            else:
                #values_dict[ data_thoughts[p] ].add( p + '_' + filename_thoughts )
                values_dict[ str(data_thoughts[p]) ].add( p + '_' + filename_thoughts )
            if p == "BrainId" and i_BrainId_NEW_flag == 1:
                #print(p , data_access[p])
                data_thoughts[p] = BrainId_NEW
                #print(p , data_access[p])
                #sys.exit(0)'''
        #sys.exit(0)
        test_input = input.readline()
    input.close()
#if 1==1:
except:
    pass
#print("len(data_thoughts) = ", len(data_thoughts) )
#print("len(list_thoughts) = ", len(list_thoughts) )
#sys.exit(0)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source "thoughts" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: Read in Source "tombstones" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_tombstones
#    <NONE>
try:
    #list_tombstones = []
    input = open( REF_dir + filename_tombstones, encoding='utf-8-sig' )
    test_input = input.readline()
    while test_input:
        data_tombstones = json.loads(test_input.strip('\n'))
        list_tombstones.append( data_tombstones )
        #print("data_tombstones = ", data_tombstones )
        for p in data_tombstones:
            #print(p , data_tombstones[p])
            if first_time_flag == 0:
                keys_set.add(p + '_' + filename_tombstones)
                values_set.add(data_tombstones[p])
            else:
                #values_dict[ data_tombstones[p] ].add( p + '_' + filename_tombstones )
                values_dict[ str(data_tombstones[p]) ].add( p + '_' + filename_tombstones )
            if p == "BrainId" and i_BrainId_NEW_flag == 1:
                #print(p , data_access[p])
                data_tombstones[p] = BrainId_NEW
                #print(p , data_access[p])
                #sys.exit(0)
        #sys.exit(0)
        test_input = input.readline()
    input.close()
except:
    pass
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: Read in Source "tombstones" file
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 


output_tmp.write("len(keys_set) = " + str(len(keys_set)) + '\n' )
output_tmp.write("len(values_set) = " + str(len(values_set)) + '\n' )


        

if first_time_flag == 0:
    zpickle( keys_set , 'keys_set.zpkl' )
    zpickle( values_set , 'values_set.zpkl' )
else:
    '''for i in values_set:
        #output_tmp.write("values_set = " + str( i ) + '\n' )
        for j in keys_set:
            #output_tmp.write("keys_set = " + str( j ) + '\n' )
            values_dict[ i ].add( j )'''
            
    
    key = values_dict.keys()
    for k in key:
        if len(values_dict[ k ]) > 1:
            #output_tmp.write("k = " + str( values_dict[ k ] ) + '\n' )
            #output_tmp.write( str(len(values_dict[ k ])) + "  k = " + str( values_dict[ k ] ) + '\n' )
            #output_tmp.write( "k = " + str(k) + '    ' + str( values_dict[ k ] ) + '\n' )
            if not (isinstance(k, float)) and not (isinstance(k, int)):
                if len(k) == 36:
                    output_tmp.write( str(len(k))+ "    k = " + str(k) + '    ' + str( values_dict[ k ] ) + '\n' )





















#=======================================================================================================
#=======================================================================================================
#=======================================================================================================
# START: Ignore for now
#=======================================================================================================
#=======================================================================================================
#=======================================================================================================
#if 1 == 0:
if 1 == 1:
    '''    {"Name":"ROOT","ActivationDateTime":"2018-08-15T20:19:55.1573693",
        "ACType":0,
        "Kind":1,
        "TagIds":[],
        "ThoughtIconInfo":"1::0:False:False:0",
        "CreationDateTime":"2018-08-15T20:18:54.274887",
        "ModificationDateTime":"2018-08-15T20:18:54.274887",
        "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "Id":"244d5948-ae81-59b1-bc00-d3d6a1b917d9"}'''

    # filename_thoughts
    #   {"Name":"test_export",
    #   "ActivationDateTime":"2018-08-14T19:18:47.9528199",
    #   "ACType":0,
    #   "Kind":1,
    #   "TagIds":[],
    #   "ThoughtIconInfo":"1::0:False:False:0",
    #   "CreationDateTime":"2018-08-14T19:17:07.3530659",
    #   "ModificationDateTime":"2018-08-14T19:17:07.3530659",
    #   "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    #   "Id":"0940d0f5-e467-4a8b-aaf8-407c7848aa1a"}

    root = {"Name":"ROOT", \
        "ActivationDateTime":"2018-08-15T20:19:55.1573693", \
        "ACType":0, \
        "Kind":1, \
        "TagIds":[], \
        "ThoughtIconInfo":"1::0:False:False:0", \
        "CreationDateTime":"2018-08-15T20:18:54.274887", \
        "ModificationDateTime":"2018-08-15T20:18:54.274887", \
        "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", \
        "Id":"244d5948-ae81-59b1-bc00-d3d6a1b917d9"}

    #print("root[ 'Id' ] = ", root[ "Id" ])
    #print("type(root[ 'Id' ]) = ", type(root[ "Id" ]))
    #root_Id = "244d5948-ae81-59b1-bc00-d3d6a1b917d9"
    #root_Id = "244d5948-ae81-59b1-bc00-d3d6a1b917d0"
    #root_Id = str(uuid.uuid4())
    #print("type(root_Id) = ", type(root_Id))
    #print("root_Id = ", root_Id)
    #root[ "Name" ] = "AbCd"
    #root[ "Id" ] = root_Id
    #print("root[ 'Id' ] = ", root[ "Id" ])
    #sys.exit(0)

    '''root[ "Name" ]                 = "GITHUB (Public): afcarl"
    root[ "ActivationDateTime" ]   = root[ "ActivationDateTime" ]
    root[ "ACType" ]               = root[ "ACType" ]
    root[ "Kind" ]                 = root[ "Kind" ]
    root[ "TagIds" ]               = root[ "TagIds" ]
    root[ "ThoughtIconInfo" ]      = root[ "ThoughtIconInfo" ]
    root[ "CreationDateTime" ]     = root[ "CreationDateTime" ]
    root[ "ModificationDateTime" ] = root[ "ModificationDateTime" ]
    root[ "BrainId" ]              = root[ "BrainId" ]
    root[ "Id" ]                   = root[ "Id" ]'''

    list_thoughts_tmp = []
    for data_thoughts in list_thoughts:
        if data_thoughts[ "Name" ] == "ROOT":
            print("data_thoughts = ", data_thoughts)
            #sys.exit(0)
            #root[ "Name" ]                 = "GITHUB (Public): afcarl (By AUTHOR)"
            root[ "Name" ]                 = "Brain #2: Repos-By-Author:"
            root[ "ActivationDateTime" ]   = data_thoughts[ "ActivationDateTime" ]
            root[ "ACType" ]               = data_thoughts[ "ACType" ]
            root[ "Kind" ]                 = data_thoughts[ "Kind" ]
            root[ "TagIds" ]               = data_thoughts[ "TagIds" ]
            root[ "ThoughtIconInfo" ]      = data_thoughts[ "ThoughtIconInfo" ]
            root[ "CreationDateTime" ]     = data_thoughts[ "CreationDateTime" ]
            root[ "ModificationDateTime" ] = data_thoughts[ "ModificationDateTime" ]
            root[ "BrainId" ]              = data_thoughts[ "BrainId" ]
            root[ "Id" ]                   = data_thoughts[ "Id" ]
            
            data_thoughts_tmp = defaultdict()
            data_thoughts_tmp[ "Name" ]                 = root[ "Name" ]
            data_thoughts_tmp[ "ActivationDateTime" ]   = root[ "ActivationDateTime" ]
            data_thoughts_tmp[ "ACType" ]               = root[ "ACType" ]
            data_thoughts_tmp[ "Kind" ]                 = root[ "Kind" ]
            data_thoughts_tmp[ "TagIds" ]               = root[ "TagIds" ]
            data_thoughts_tmp[ "ThoughtIconInfo" ]      = root[ "ThoughtIconInfo" ]
            data_thoughts_tmp[ "CreationDateTime" ]     = root[ "CreationDateTime" ]
            data_thoughts_tmp[ "ModificationDateTime" ] = root[ "ModificationDateTime" ]
            data_thoughts_tmp[ "BrainId" ]              = root[ "BrainId" ]
            data_thoughts_tmp[ "Id" ]                   = root[ "Id" ]

            list_thoughts_tmp.append( data_thoughts_tmp )
        else:
            list_thoughts_tmp.append( data_thoughts )

    list_thoughts = []
    list_thoughts = deepcopy( list_thoughts_tmp )

    
    
    thoughts_attachments_link = defaultdict()
    thoughts_attachments_link[ "SourceId" ]             = root[ "Id" ]
    thoughts_attachments_link[ "Name" ]                 = "afcarl · GitHub"
    thoughts_attachments_link[ "Position" ]             = 1.0
    thoughts_attachments_link[ "Type" ]                 = 3
    thoughts_attachments_link[ "DataLength" ]           = 0
    thoughts_attachments_link[ "Location" ]             = "https://github.com/afcarl"
    thoughts_attachments_link[ "IsIcon" ]               = False
    thoughts_attachments_link[ "SourceType" ]           = 2
    thoughts_attachments_link[ "IsWallpaper" ]          = False
    thoughts_attachments_link[ "CreationDateTime" ]     = root[ "CreationDateTime" ]
    thoughts_attachments_link[ "ModificationDateTime" ] = root[ "ModificationDateTime" ]
    thoughts_attachments_link[ "BrainId" ]              = root[ "BrainId" ]
    thoughts_attachments_link[ "Id" ]                   = str(uuid.uuid4())

    #list_attachments = []
    list_attachments.append( thoughts_attachments_link )

    
    
    
    '''ChildA = {"Name":"Child A", \
        "ActivationDateTime":"2018-08-15T20:19:55.1573693", \
        "ACType":0, \
        "Kind":1, \
        "TagIds":[], \
        "ThoughtIconInfo":"1::0:False:False:0", \
        "CreationDateTime":"2018-08-15T20:18:54.274887", \
        "ModificationDateTime":"2018-08-15T20:18:54.274887", \
        "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", \
        "Id":"244d5948-ae81-59b1-bc00-d3d6a1b917da"}'''
    #ChildA_Id = str(uuid.uuid4())
    #ChildA[ "Id" ] = ChildA_Id

    ChildA = defaultdict()
    ChildA[ "Name" ]                 = "Child A"
    ChildA[ "ActivationDateTime" ]   = root[ "ActivationDateTime" ]
    ChildA[ "ACType" ]               = root[ "ACType" ]
    ChildA[ "Kind" ]                 = root[ "Kind" ]
    ChildA[ "TagIds" ]               = root[ "TagIds" ]
    ChildA[ "ThoughtIconInfo" ]      = root[ "ThoughtIconInfo" ]
    ChildA[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
    ChildA[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
    ChildA[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
    ChildA[ "Id" ]                   = str(uuid.uuid4())

    '''ChildB = {"Name":"Child B", \
        "ActivationDateTime":"2018-08-15T20:19:55.1573693", \
        "ACType":0, \
        "Kind":1, \
        "TagIds":[], \
        "ThoughtIconInfo":"1::0:False:False:0", \
        "CreationDateTime":"2018-08-15T20:18:54.274887", \
        "ModificationDateTime":"2018-08-15T20:18:54.274887", \
        "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", \
        "Id":"244d5948-ae81-59b1-bc00-d3d6a1b917db"}'''
    #ChildB_Id = str(uuid.uuid4())
    #ChildB[ "Id" ] = ChildB_Id

    ChildB = defaultdict()
    ChildB[ "Name" ]                 = "Child B"
    ChildB[ "ActivationDateTime" ]   = root[ "ActivationDateTime" ]
    ChildB[ "ACType" ]               = root[ "ACType" ]
    ChildB[ "Kind" ]                 = root[ "Kind" ]
    ChildB[ "TagIds" ]               = root[ "TagIds" ]
    ChildB[ "ThoughtIconInfo" ]      = root[ "ThoughtIconInfo" ]
    ChildB[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
    ChildB[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
    ChildB[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
    ChildB[ "Id" ]                   = str(uuid.uuid4())

    #list_links = []
    #list_attachments = []
    #list_modificationlogs = []

    #list_thoughts = []
    #list_thoughts.append( root )
    #list_thoughts.append( ChildA )
    #list_thoughts.append( ChildB )




    TAG_Similar_list = list( TAG_Similar_set )
    TAG_Similar_list.sort()

    cap_alphabet_list = ["(misc)","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    cap_alphabet_list_lower = ["(misc)","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    i_title_accum = 0

    # loop over alphabet soup
    for CHILD_name in cap_alphabet_list:
    
        if CHILD_name.isnumeric():
            continue
    
    
        Child = defaultdict()
        Child[ "Name" ]                 = CHILD_name
        Child[ "ActivationDateTime" ]   = root[ "ActivationDateTime" ]
        Child[ "ACType" ]               = root[ "ACType" ]
        Child[ "Kind" ]                 = root[ "Kind" ]
        Child[ "TagIds" ]               = root[ "TagIds" ]
        Child[ "ThoughtIconInfo" ]      = root[ "ThoughtIconInfo" ]
        Child[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
        Child[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
        Child[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
        Child[ "Id" ]                   = str(uuid.uuid4())

        list_thoughts.append( Child )

        root_to_Child = defaultdict()
        root_to_Child[ "ThoughtIdA" ]           = root[ "Id" ]
        root_to_Child[ "ThoughtIdB" ]           = Child[ "Id" ]
        root_to_Child[ "Kind" ]                 = 1
        root_to_Child[ "Relation" ]             = 1
        root_to_Child[ "Direction" ]            = -1
        root_to_Child[ "Meaning" ]              = 1
        root_to_Child[ "Thickness" ]            = -1
        root_to_Child[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
        root_to_Child[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
        root_to_Child[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
        root_to_Child[ "Id" ]                   = str(uuid.uuid4())

        list_links.append( root_to_Child )
    
        #print("#1: len(list_links) = ", len(list_links))


        '''thoughts_attachments_link = defaultdict()
        thoughts_attachments_link[ "SourceId" ]             = Child[ "Id" ]
        thoughts_attachments_link[ "Name" ]                 = Child[ "Name" ]
        thoughts_attachments_link[ "Position" ]             = 1.0
        thoughts_attachments_link[ "Type" ]                 = 3
        thoughts_attachments_link[ "DataLength" ]           = 0
        #thoughts_attachments_link[ "Location" ]             = "https://github.com/afcarl/" + Child[ "Name" ]
        thoughts_attachments_link[ "Location" ]             = ""
        thoughts_attachments_link[ "IsIcon" ]               = False
        thoughts_attachments_link[ "SourceType" ]           = 2
        thoughts_attachments_link[ "IsWallpaper" ]          = False
        thoughts_attachments_link[ "CreationDateTime" ]     = root[ "CreationDateTime" ]
        thoughts_attachments_link[ "ModificationDateTime" ] = root[ "ModificationDateTime" ]
        thoughts_attachments_link[ "BrainId" ]              = root[ "BrainId" ]
        thoughts_attachments_link[ "Id" ]                   = str(uuid.uuid4())

        list_attachments.append( thoughts_attachments_link )'''


        # Above is ROOT to alphabet soup








        # loop over AUTHOR list
        #print("repo_names_list = ",repo_names_list)
        #print("len(repo_names_list )= ", len(repo_names_list) )
        #sys.exit(0)
        #for TITLE_name in repo_names_list:
        for AUTHOR_name in forked_author_list:
            #print(type(forked_author_list))
            #print(type(AUTHOR_name))
            #print(AUTHOR_name, AUTHOR_name[0], AUTHOR_name[0][0].lower())
            #if AUTHOR_name[0] == "EricSchles":
            #    print(AUTHOR_name, AUTHOR_name[0], AUTHOR_name[0][0].lower())
            #    sys.exit(0)
            #sys.exit(0)

            #print("0#: AUTHOR_name = ",AUTHOR_name)
            #print("0#: CHILD_name = ",CHILD_name)
            #if CHILD_name[0].lower() == TAG_name[0].lower():
            #if CHILD_name[0].lower() == TITLE_name[0].lower():
            #if CHILD_name[0].lower() == AUTHOR_name[0].lower():
            if CHILD_name[0].lower() == AUTHOR_name[0][0].lower():
                #print("AUTHOR_name = ",AUTHOR_name)
                #print("CHILD_name = ",CHILD_name)
                #CHILD_X_name = TITLE_name
                CHILD_X_name = CHILD_name
                #print("#1: CHILD_X_name = ",CHILD_X_name)
                #continue
        
            #elif ( TAG_name[0].lower() not in cap_alphabet_list_lower[1:] ) and ( CHILD_name[0] == "(" ):
            #elif ( TITLE_name[0].lower() not in cap_alphabet_list_lower[1:] ) and ( CHILD_name[0] == "(" ):
            #elif ( AUTHOR_name[0].lower() not in cap_alphabet_list_lower[1:] ) and ( CHILD_name[0] == "(" ):
            elif ( AUTHOR_name[0][0].lower() not in cap_alphabet_list_lower[1:] ) and ( CHILD_name[0] == "(" ):
                #print("#2: AUTHOR_name = ",AUTHOR_name,AUTHOR_name[0].lower())
                #print("#2: CHILD_name = ",CHILD_name)
                CHILD_X_name = "(misc)"
                #print("#2: CHILD_X_name = ",CHILD_X_name)
                #continue
        
            else:
                #print("#3 ERROR: CHILD_name / TITLE_name = ", CHILD_name , TITLE_name )
                #sys.exit(0)
                continue
                #pass

            i_title_accum += 1
            #print( i_title_accum , "CHILD_name / TITLE_name = ", CHILD_name , TITLE_name)
            #print("#4:", i_title_accum , "CHILD_name / AUTHOR_name = ", CHILD_name , AUTHOR_name[0])
        

            ChildA = defaultdict()
            ChildA[ "Name" ]                 = Child[ "Name" ]
            ChildA[ "ActivationDateTime" ]   = Child[ "ActivationDateTime" ]
            ChildA[ "ACType" ]               = Child[ "ACType" ]
            ChildA[ "Kind" ]                 = Child[ "Kind" ]
            ChildA[ "TagIds" ]               = Child[ "TagIds" ]
            ChildA[ "ThoughtIconInfo" ]      = Child[ "ThoughtIconInfo" ]
            ChildA[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
            ChildA[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
            ChildA[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
            ChildA[ "Id" ]                   = Child[ "Id" ]

            #list_thoughts.append( ChildA )


            # check to see if current author has already been processed
            if AUTHOR_name[0] in author_already_included_set:
                continue
            else:
                author_already_included_set.add( AUTHOR_name[0] )

    
            ChildB = defaultdict()
            #ChildB[ "Name" ]                 = TITLE_name
            ChildB[ "Name" ]                 = AUTHOR_name[0]
            
            ChildB[ "ActivationDateTime" ]   = Child[ "ActivationDateTime" ]
            ChildB[ "ACType" ]               = Child[ "ACType" ]
            ChildB[ "Kind" ]                 = Child[ "Kind" ]
            ChildB[ "TagIds" ]               = Child[ "TagIds" ]
            ChildB[ "ThoughtIconInfo" ]      = Child[ "ThoughtIconInfo" ]
            ChildB[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
            ChildB[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
            ChildB[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
            ChildB[ "Id" ]                   = str(uuid.uuid4())

            list_thoughts.append( ChildB )

            root_to_Child = defaultdict()
            root_to_Child[ "ThoughtIdA" ]           = ChildA[ "Id" ]
            root_to_Child[ "ThoughtIdB" ]           = ChildB[ "Id" ]
            root_to_Child[ "Kind" ]                 = 1
            root_to_Child[ "Relation" ]             = 1
            root_to_Child[ "Direction" ]            = -1
            root_to_Child[ "Meaning" ]              = 1
            root_to_Child[ "Thickness" ]            = -1
            root_to_Child[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
            root_to_Child[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
            root_to_Child[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
            root_to_Child[ "Id" ]                   = str(uuid.uuid4())

            list_links.append( root_to_Child )
        
            #print("#2: len(list_links) = ", len(list_links))


            # add link for author's GITHUB home page
            thoughts_attachments_link = defaultdict()
            thoughts_attachments_link[ "SourceId" ]             = ChildB[ "Id" ]
            thoughts_attachments_link[ "Name" ]                 = AUTHOR_name[0] + " · GitHub"
            thoughts_attachments_link[ "Position" ]             = 1.0
            thoughts_attachments_link[ "Type" ]                 = 3
            thoughts_attachments_link[ "DataLength" ]           = 0
            thoughts_attachments_link[ "Location" ]             = "https://github.com/" + AUTHOR_name[0]
            thoughts_attachments_link[ "IsIcon" ]               = False
            thoughts_attachments_link[ "SourceType" ]           = 2
            thoughts_attachments_link[ "IsWallpaper" ]          = False
            thoughts_attachments_link[ "CreationDateTime" ]     = root[ "CreationDateTime" ]
            thoughts_attachments_link[ "ModificationDateTime" ] = root[ "ModificationDateTime" ]
            thoughts_attachments_link[ "BrainId" ]              = root[ "BrainId" ]
            thoughts_attachments_link[ "Id" ]                   = str(uuid.uuid4())

            #list_attachments = []
            list_attachments.append( thoughts_attachments_link )


            #if len( forked_author_to_titles_dict[ AUTHOR_name[0] ] ) == 0:
            #    #print("#A: forked_author_to_titles_dict[ AUTHOR_name[0] ] = ", forked_author_to_titles_dict[ AUTHOR_name[0] ])
            #    #print("#A: len(forked_author_to_titles_dict[ AUTHOR_name[0] ]) = ", len(forked_author_to_titles_dict[ AUTHOR_name[0] ]))
            #    continue
            #else:
            #    #print("#B: len(forked_author_to_titles_dict[ AUTHOR_name[0] ]) = ", len(forked_author_to_titles_dict[ AUTHOR_name[0] ]))
            #    pass
            #print("#C: forked_author_to_titles_dict[ AUTHOR_name[0] ] = ", forked_author_to_titles_dict[ AUTHOR_name[0] ])
            #forked_author_to_titles_dict_tmp = defaultdict( list )
            #for TITLE_name in forked_author_to_titles_dict[ AUTHOR_name[0] ]:
            #    if len(TITLE_name) > 0:
            #        forked_author_to_titles_dict_tmp[ AUTHOR_name[0] ].append( TITLE_name )
            ##forked_author_to_titles_dict = deepcopy( forked_author_to_titles_dict_tmp )
            #print("#D: forked_author_to_titles_dict_tmp[ AUTHOR_name[0] ] = ", forked_author_to_titles_dict_tmp[ AUTHOR_name[0] ])
            #sys.exit(0)

            # loop over TITLE list for current author
            for TITLE_name in forked_author_to_titles_dict[ AUTHOR_name[0] ]:
            #for TITLE_name in forked_author_to_titles_dict_tmp[ AUTHOR_name[0] ]:
                #print("AUTHOR_name = ", AUTHOR_name)
                #print("AUTHOR_name[0] = ", AUTHOR_name[0])
                #print("CHILD_name[0] = ", CHILD_name[0])
                #print("CHILD_name = ", CHILD_name)
                #print("TITLE_name = ", TITLE_name)
                #print("TITLE_name[0] = ", TITLE_name[0])
                #sys.exit(0)
                '''if AUTHOR_name[0] == "EricSchles":
                    print("#1 EricSchles: ", AUTHOR_name, AUTHOR_name[0], AUTHOR_name[0][0].lower())
                    print("#2 EricSchles: ", forked_author_to_titles_dict[ AUTHOR_name[0] ])
                    print("#3 EricSchles: ", len(forked_author_to_titles_dict[ AUTHOR_name[0] ]))
                    sys.exit(0)'''




                '''#print("0#: TITLE_name = ",TITLE_name)
                #print("0#: CHILD_name = ",CHILD_name)
                #if CHILD_name[0].lower() == TAG_name[0].lower():
                if CHILD_name[0].lower() == TITLE_name[0].lower():
                    #print("TITLE_name = ",TITLE_name)
                    #print("CHILD_name = ",CHILD_name)
                    CHILD_X_name = TITLE_name
                    #print("#1: CHILD_X_name = ",CHILD_X_name)
                    #continue
        
                #elif ( TAG_name[0].lower() not in cap_alphabet_list_lower[1:] ) and ( CHILD_name[0] == "(" ):
                elif ( TITLE_name[0].lower() not in cap_alphabet_list_lower[1:] ) and ( CHILD_name[0] == "(" ):
                    #print("TITLE_name = ",TITLE_name)
                    #print("CHILD_name = ",CHILD_name)
                    CHILD_X_name = "(misc)"
                    #print("#2: CHILD_X_name = ",CHILD_X_name)
                    #continue
        
                else:
                    #print("#3 ERROR: CHILD_name / TITLE_name = ", CHILD_name , TITLE_name )
                    #sys.exit(0)
                    continue
                    #pass'''

                i_title_accum += 1
                #print( i_title_accum , "CHILD_name / TITLE_name = ", CHILD_name , TITLE_name)
        

                ChildC = defaultdict()
                ChildC[ "Name" ]                 = ChildB[ "Name" ]
                ChildC[ "ActivationDateTime" ]   = ChildB[ "ActivationDateTime" ]
                ChildC[ "ACType" ]               = ChildB[ "ACType" ]
                ChildC[ "Kind" ]                 = ChildB[ "Kind" ]
                ChildC[ "TagIds" ]               = ChildB[ "TagIds" ]
                ChildC[ "ThoughtIconInfo" ]      = ChildB[ "ThoughtIconInfo" ]
                ChildC[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
                ChildC[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
                ChildC[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
                ChildC[ "Id" ]                   = ChildB[ "Id" ]

                #list_thoughts.append( ChildC )

    
                ChildD = defaultdict()
                ChildD[ "Name" ]                 = TITLE_name
                ChildD[ "ActivationDateTime" ]   = ChildB[ "ActivationDateTime" ]
                ChildD[ "ACType" ]               = ChildB[ "ACType" ]
                ChildD[ "Kind" ]                 = ChildB[ "Kind" ]
                ChildD[ "TagIds" ]               = ChildB[ "TagIds" ]
                ChildD[ "ThoughtIconInfo" ]      = ChildB[ "ThoughtIconInfo" ]
                ChildD[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
                ChildD[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
                ChildD[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
                ChildD[ "Id" ]                   = str(uuid.uuid4())

                list_thoughts.append( ChildD )

                root_to_Child = defaultdict()
                root_to_Child[ "ThoughtIdA" ]           = ChildC[ "Id" ]
                root_to_Child[ "ThoughtIdB" ]           = ChildD[ "Id" ]
                root_to_Child[ "Kind" ]                 = 1
                root_to_Child[ "Relation" ]             = 1
                root_to_Child[ "Direction" ]            = -1
                root_to_Child[ "Meaning" ]              = 1
                root_to_Child[ "Thickness" ]            = -1
                root_to_Child[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
                root_to_Child[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
                root_to_Child[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
                root_to_Child[ "Id" ]                   = str(uuid.uuid4())

                list_links.append( root_to_Child )
        
                #print("#2: len(list_links) = ", len(list_links))


                if 1 == 1:
                    if 1 == 1:
                        
                        # attachement for URL entry
                        thoughts_attachments_link = defaultdict()
                        thoughts_attachments_link[ "SourceId" ]             = ChildD[ "Id" ]
                        #thoughts_attachments_link[ "SourceId" ]             = ChildB[ "Id" ]
                        
                        thoughts_attachments_link[ "Name" ]                 = ChildD[ "Name" ]
                        #thoughts_attachments_link[ "Name" ]                 = ChildB[ "Name" ]
                        
                        thoughts_attachments_link[ "Position" ]             = 1.0
                        thoughts_attachments_link[ "Type" ]                 = 3
                        thoughts_attachments_link[ "DataLength" ]           = 0
                        thoughts_attachments_link[ "Location" ]             = "https://github.com/afcarl/" + ChildD[ "Name" ]
                        #thoughts_attachments_link[ "Location" ]             = ""
                        thoughts_attachments_link[ "IsIcon" ]               = False
                        thoughts_attachments_link[ "SourceType" ]           = 2
                        thoughts_attachments_link[ "IsWallpaper" ]          = False
                        thoughts_attachments_link[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
                        thoughts_attachments_link[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
                        thoughts_attachments_link[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
                        thoughts_attachments_link[ "Id" ]                   = str(uuid.uuid4())

                        list_attachments.append( thoughts_attachments_link )

                        #break
                        
                        
                        #if 1 == 0:
                        if 1 == 1:

                            # attachement for "notes.html" entry: "SourceId" corresponds to folder ID also!!!
                            #{"SourceId":"3e5a1240-60c1-4a9a-a0d7-7242cba5593f",
                            #"Name":"notes.html",
                            #"Position":0.0,
                            #"FileModificationDateTime":"2018-09-21T00:12:41.5285687",
                            #"Type":4,
                            #"DataLength":80,
                            #"Location":"notes.html",
                            #"IsIcon":false,
                            #"SourceType":2,
                            #"NoteType":2,
                            #"IsWallpaper":false,
                            #"CreationDateTime":"2018-09-21T00:12:41.5285687",
                            #"ModificationDateTime":"2018-09-21T00:12:41.5285687",
                            #"BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                            #"Id":"1ccb2f1a-4a98-47c4-a2e1-2b0819ea07a5"}
                            thoughts_attachments_link = defaultdict()
                            thoughts_attachments_link[ "SourceId" ]                 = ChildD[ "Id" ]
                            #thoughts_attachments_link[ "SourceId" ]                 = ChildB[ "Id" ]
                            
                            thoughts_attachments_link[ "Name" ]                     = "notes.html"
                            thoughts_attachments_link[ "Position" ]                 = 0.0
                            thoughts_attachments_link[ "FileModificationDateTime" ] = root[ "ModificationDateTime" ]
                            thoughts_attachments_link[ "Type" ]                     = 4
                            thoughts_attachments_link[ "DataLength" ]               = 80
                            thoughts_attachments_link[ "Location" ]                 = "notes.html"
                            thoughts_attachments_link[ "IsIcon" ]                   = False
                            thoughts_attachments_link[ "SourceType" ]               = 2
                            thoughts_attachments_link[ "NoteType" ]                 = 2
                            thoughts_attachments_link[ "IsWallpaper" ]              = False
                            thoughts_attachments_link[ "CreationDateTime" ]         = brainusers_dict[ "CreationDateTime" ]
                            thoughts_attachments_link[ "ModificationDateTime" ]     = brainusers_dict[ "ModificationDateTime" ]
                            thoughts_attachments_link[ "BrainId" ]                  = brainusers_dict[ "BrainId" ]
                            thoughts_attachments_link[ "Id" ]                       = str(uuid.uuid4())

                            list_attachments.append( thoughts_attachments_link )


                            #print("ChildD[ 'Name' ] = ", ChildD[ "Name" ])


                            #forked_author_dict = zunpickle( 'forked_author_dict.zpkl' )
                            keys_forked_author_dict = forked_author_dict.keys()



                            #doc_title_Similar_dict = zunpickle( 'doc_title_Similar_dict.zpkl' )
                            keys_doc_title_Similar = doc_title_Similar_dict.keys()

                            #doc_title_Similar_TAGS_dict = zunpickle( 'doc_title_Similar_TAGS_dict.zpkl' )
                            keys_doc_title_Similar_TAGs = doc_title_Similar_TAGS_dict.keys()

                            #doc_title_Similar_TAGS_dict_all = zunpickle( 'doc_title_Similar_TAGS_dict_all.zpkl' )
                            keys_doc_title_Similar_TAGs_all = doc_title_Similar_TAGS_dict_all.keys()

                            #if ChildD[ "Name" ] in keys_doc_title_Similar:
                            #    print("doc_title_Similar_dict[ ChildD[ 'Name' ] ] = ", doc_title_Similar_dict[ ChildD[ 'Name' ] ] )

                            #if ChildD[ "Name" ] in keys_doc_title_Similar_TAG:
                            #    print("doc_title_Similar_TAGS_dict[ ChildD[ 'Name' ] ] = ", doc_title_Similar_TAGS_dict[ ChildD[ 'Name' ] ] )


                            #zpickle( doc_title_DisSimilar_dict , 'doc_title_DisSimilar_dict.zpkl' )
                            #doc_title_DisSimilar_dict = zunpickle( 'doc_title_DisSimilar_dict.zpkl' )
                            keys_doc_title_DisSimilar = doc_title_DisSimilar_dict.keys()
                        
                            #zpickle( doc_title_DisSimilar_TAGS_dict , 'doc_title_DisSimilar_TAGS_dict.zpkl' )
                            #doc_title_DisSimilar_TAGS_dict = zunpickle( 'doc_title_DisSimilar_TAGS_dict.zpkl' )
                            keys_doc_title_DisSimilar_TAGS = doc_title_DisSimilar_TAGS_dict.keys()

                            #if ChildD[ "Name" ] in keys_doc_title_DisSimilar:
                            #    print("doc_title_DisSimilar_dict[ ChildD[ 'Name' ] ] = ", doc_title_DisSimilar_dict[ ChildD[ 'Name' ] ] )

                            #if ChildD[ "Name" ] in keys_doc_title_DisSimilar_TAGS:
                            #    print("doc_title_DisSimilar_TAGS_dict[ ChildD[ 'Name' ] ] = ", doc_title_DisSimilar_TAGS_dict[ ChildD[ 'Name' ] ] )


                            #doc_title_Similar_list_tmp = []
                            #for (name,simularity,none) in doc_title_Similar_dict[ ChildD[ 'Name' ] ]:
                            #    doc_title_Similar_list_tmp.append( ( name , simularity ) )


                            #doc_title_DisSimilar_list_tmp = []
                            #for (name,simularity,none) in doc_title_DisSimilar_dict[ ChildD[ 'Name' ] ]:
                            #    doc_title_DisSimilar_list_tmp.append( ( name , simularity ) )

                            #sys.exit(0)


                            folder_name = results_dir + ChildD[ "Id" ]
                            #print("folder_name = ", folder_name )
                            if not os.path.exists( folder_name ):
                                os.makedirs( folder_name )

                            folder_name = results_dir + ChildD[ "Id" ] + "/Notes"
                            #print("folder_name = ", folder_name )
                            if not os.path.exists( folder_name ):
                                os.makedirs( folder_name )

                            file_name = results_dir + ChildD[ "Id" ] + "/Notes/notes.html"
                            #print("file_name = ", file_name )
                            if not os.path.exists( file_name ):
                                input_file_name = open( file_name , 'w' )

                                # Title:
                                #input_file_name.write( '<p>"' + str( ChildD[ "Name" ] ).upper() + '" Repo TAGS:</p>' + '\n' )
                                #input_file_name.write( '<p>GITHUB REPRO NAME: "' + str( ChildD[ "Name" ] ).upper() + '"</p>' + '\n' )
                                input_file_name.write( '<p><b><mark>GITHUB REPRO NAME: "' + str( ChildD[ "Name" ] ).upper() + '"</mark></b></p>' + '\n' )

                                #input_file_name.write( "<p> </p>" + '\n' )
                                
                                
                                if ChildD[ "Name" ] in keys_forked_author_dict:
                                    REPRO_AUTHOR = next( iter( forked_author_dict[ ChildD[ "Name" ] ] ) )
                                    #input_file_name.write( '<p><b><mark>REPRO AUTHOR: "' + str( forked_author_dict[ ChildD[ "Name" ] ] ).upper() + '"</mark></b></p>' + '\n' )
                                    #input_file_name.write( '<p><b><mark>REPRO AUTHOR: "' + ( forked_author_dict[ ChildD[ "Name" ] ] ).upper() + '"</mark></b></p>' + '\n' )
                                    input_file_name.write( '<p><b><mark>REPRO AUTHOR: "' + str( REPRO_AUTHOR ).upper() + '"</mark></b></p>' + '\n' )

                                    #input_file_name.write( "<p> </p>" + '\n' )
                                
                                # Repo TAGS:
                                #input_file_name.write( "<p>REPO TAGS: " + str( doc_title_Similar_TAGS_dict[ ChildD[ 'Name' ] ] ).upper() + "</p>" + '\n' )
                                input_file_name.write( "<p><b><mark>REPO TAGS:</mark></b></p>" + '\n' )
                                input_file_name.write( "<p>" + str( doc_title_Similar_TAGS_dict[ ChildD[ 'Name' ] ] ).upper() + "</p>" + '\n' )
                                #input_file_name.write( "<p> </p>" + '\n' )


                                try:
                                    doc_title_Similar_list_tmp = []
                                    for (name,simularity,none) in doc_title_Similar_dict[ ChildD[ 'Name' ] ]:
                                        doc_title_Similar_list_tmp.append( ( name , simularity ) )

                                    # Most Similar Repos:
                                    #input_file_name.write( '<p>"' + str( ChildD[ "Name" ] ).upper() + '" ArgMin(10,Score>0.5) Most Similar Repos:</p>' + '\n' )
                                    #input_file_name.write( "<p>" + str( doc_title_Similar_dict[ ChildD[ 'Name' ] ] ).upper() + "</p>" + '\n' )
                                    #input_file_name.write( "<p>" + str( doc_title_Similar_list_tmp ).upper() + "</p>" + '\n' )
                                    #input_file_name.write( "<p>MOST SIMILAR REPOS ArgMin(10,Score>0.5): " + str( doc_title_Similar_list_tmp ).upper() + "</p>" + '\n' )
                                    input_file_name.write( "<p><b><mark>MOST SIMILAR REPOS ArgMin(10,Score>0.5):</mark></b></p>" + '\n' )
                                    input_file_name.write( "<p>" + str( doc_title_Similar_list_tmp ).upper() + "</p>" + '\n' )
                                    #input_file_name.write( "<p> </p>" + '\n' )
                                except:
                                    pass

                                
                                # Most Similar Repos TAGS:
                                #input_file_name.write( "<p>REPO TAGS: " + str( doc_title_Similar_TAGS_dict[ ChildD[ 'Name' ] ] ).upper() + "</p>" + '\n' )
                                input_file_name.write( "<p><b><mark>MOST SIMILAR REPOS TAGS:</mark></b></p>" + '\n' )
                                input_file_name.write( "<p>" + str( doc_title_Similar_TAGS_dict_all[ ChildD[ 'Name' ] ] ).upper() + "</p>" + '\n' )
                                #input_file_name.write( "<p> </p>" + '\n' )


                                try:
                                    doc_title_DisSimilar_list_tmp = []
                                    for (name,simularity,none) in doc_title_DisSimilar_dict[ ChildD[ 'Name' ] ]:
                                        doc_title_DisSimilar_list_tmp.append( ( name , simularity ) )

                                    #input_file_name.write( '<p>"' + str( ChildD[ "Name" ] ).upper() + '" ArgMin(20,Score<0.05) Most DisSimilar Repos:</p>' + '\n' )
                                    #input_file_name.write( "<p>" + str( doc_title_DisSimilar_dict[ ChildD[ 'Name' ] ] ).upper() + "</p>" + '\n' )
                                    #input_file_name.write( "<p>" + str( doc_title_DisSimilar_list_tmp ).upper() + "</p>" + '\n' )
                                    #input_file_name.write( "<p>MOST DISSIMILAR REPOS ArgMin(20,Score<0.05): " + str( doc_title_DisSimilar_list_tmp ).upper() + "</p>" + '\n' )
                                    #input_file_name.write( "<p><b><mark>MOST DISSIMILAR REPOS ArgMin(20,Score<0.05):</mark></b></p>" + '\n' )
                                    input_file_name.write( "<p><b><mark>MOST DISSIMILAR REPOS ArgMin(10,Score<0.05):</mark></b></p>" + '\n' )
                                    input_file_name.write( "<p>" + str( doc_title_DisSimilar_list_tmp ).upper() + "</p>" + '\n' )
                                except:
                                    pass


                                #input_file_name.write( '<p>"' + str( ChildD[ "Name" ] ).upper() + '" Most DisSimilar Repo TAGS:</p>' + '\n' )
                                #input_file_name.write( "<p>" + str( doc_title_DisSimilar_TAGS_dict[ ChildD[ 'Name' ] ] ).upper() + "</p>" + '\n' )
                                #input_file_name.write( "<p>MOST DISSIMILAR REPO TAGS: " + str( doc_title_DisSimilar_TAGS_dict[ ChildD[ 'Name' ] ] ).upper() + "</p>" + '\n' )
                                input_file_name.write( "<p><b><mark>MOST DISSIMILAR REPOS TAGS:</mark></b></p>" + '\n' )
                                input_file_name.write( "<p>" + str( doc_title_DisSimilar_TAGS_dict[ ChildD[ 'Name' ] ] ).upper() + "</p>" + '\n' )

                                #input_file_name.write( "<p> </p>" + '\n' )

                                input_file_name.close()




                            #if 1 == 0:
                            if 1 == 1:



                                # modificationlogs for "notes.html" entry: 
                                #      "SourceId" corresponds to attachments ID also!!!
                                #      "ExtraAId" corresponds to thought ID also!!!
                                # {"SourceId":"abac8c7e-1eb2-40c5-b47c-7434b933cb3c",
                                # "SourceType":4,
                                # "ExtraAId":"5343db3f-fc70-47d9-8731-6a69f60797e2",
                                # "ExtraAType":2,
                                # "ExtraBId":"00000000-0000-0000-0000-000000000000",
                                # "ExtraBType":-1,
                                # "ModType":801,
                                # "UserId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                # "CreationDateTime":"2018-09-21T00:11:16.5267069",
                                # "ModificationDateTime":"2018-09-21T00:11:16.5267069",
                                # "BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                # "Id":"521468d8-7f9a-4f3a-865a-ac3e546f6e6e"}
                                modificationlogs_link = defaultdict()
                                modificationlogs_link[ "SourceId" ]             = thoughts_attachments_link[ "Id" ]
                                modificationlogs_link[ "SourceType" ]           = 4
                                modificationlogs_link[ "ExtraAId" ]             = thoughts_attachments_link[ "SourceId" ]
                                modificationlogs_link[ "ExtraAType" ]           = 2
                                modificationlogs_link[ "ExtraBId" ]             = "00000000-0000-0000-0000-000000000000"
                                modificationlogs_link[ "ExtraBType" ]           = -1
                                modificationlogs_link[ "ModType" ]              = 801
                                modificationlogs_link[ "UserId" ]               = brainusers_dict[ "UserId" ]
                                modificationlogs_link[ "CreationDateTime" ]     = brainusers_dict[ "CreationDateTime" ]
                                modificationlogs_link[ "ModificationDateTime" ] = brainusers_dict[ "ModificationDateTime" ]
                                modificationlogs_link[ "BrainId" ]              = brainusers_dict[ "BrainId" ]
                                modificationlogs_link[ "Id" ]                   = str(uuid.uuid4())


                                list_modificationlogs.append( modificationlogs_link )






                                # meta

                                #{"BrainId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", 
                                # "ExchangeFormatVersion": 4, 
                                # "AttachmentFileStates": {"1ccb2f1a-4a98-47c4-a2e1-2b0819ea07a5": 1, 
                                #                          "568ec224-268e-4ce5-8270-d36c7e208212": 1, 
                                #                          "7f112f10-4c25-4d82-b235-eecd03a2f85d": 1, 
                                #                          "a5da676c-b89b-4862-baf7-f52dfba2cb57": 1, 
                                #                          "abac8c7e-1eb2-40c5-b47c-7434b933cb3c": 1, 
                                #                          "191947c1-9b55-4288-9ff2-a9c030a8d536": 1  }  }

                                #try:
                                #    #list_meta = []
                                #    input = open( REF_dir + filename_meta, encoding='utf-8-sig' )
                                #    test_input = input.readline()
                                #    while test_input:
                                #        data_meta = json.loads(test_input.strip('\n'))
                                #        #list_meta.append( data_meta )
                                #        print("data_meta = ", data_meta )
                                #        #for p in data_meta:
                                #        #    #print(p , data_meta[p])
                                #        #    if first_time_flag == 0:
                                #        #        keys_set.add(p + '_' + filename_meta)
                                #        #        values_set.add(data_meta[p])
                                #        #    else:
                                #        #        #values_dict[ data_meta[p] ].add( p + '_' + filename_meta )
                                #        #        values_dict[ str(data_meta[p]) ].add( p + '_' + filename_meta )
                                #        #    if p == "BrainId" and i_BrainId_NEW_flag == 1:
                                #        #        #print(p , data_access[p])
                                #        #        data_meta[p] = BrainId_NEW
                                #        #        #print(p , data_access[p])
                                #        #        #sys.exit(0)
                                #        #sys.exit(0)
                                #        test_input = input.readline()
                                #    input.close()
                                #except:
                                #    pass
    
                                # filename_meta
                                #   {"BrainId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                #   "ExchangeFormatVersion":4,
                                #   "AttachmentFileStates":{"2355e239-50ab-41cc-84b2-b124dcfd5e3a":1}}
                                #data_meta[ "BrainId" ]                 = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                                #data_meta[ "ExchangeFormatVersion" ]   = 4
                                #data_meta[ "AttachmentFileStates" ]    = {"2355e239-50ab-41cc-84b2-b124dcfd5e3a":1}}

                                list_meta_tmp = []
                                for data_meta in list_meta:
                                    if data_meta[ "BrainId" ] == brainusers_dict[ "BrainId" ]:
                                        #print("data_meta = ", data_meta)
                                        #sys.exit(0)
                                        data_meta_tmp = defaultdict()
                                        data_meta_tmp[ "BrainId" ]               = data_meta[ "BrainId" ]
                                        data_meta_tmp[ "ExchangeFormatVersion" ] = data_meta[ "ExchangeFormatVersion" ]
                                        AttachmentFileStates_dict                = data_meta[ "AttachmentFileStates" ]
                                        #print("AttachmentFileStates_dict = ", AttachmentFileStates_dict )
                                        #print("thoughts_attachments_link[ 'Id' ] = ", thoughts_attachments_link[ "Id" ] )
                                        AttachmentFileStates_dict[ thoughts_attachments_link[ "Id" ] ] = 1
                                        #print("AttachmentFileStates_dict = ", AttachmentFileStates_dict )
                                        data_meta_tmp[ "AttachmentFileStates" ] = AttachmentFileStates_dict
                                        #print("data_meta = ", data_meta )
                                        #list_meta = []
                                        list_meta_tmp.append( data_meta_tmp )
                                        #sys.exit(0)
                                list_meta = []
                                list_meta = deepcopy( list_meta_tmp )


#=======================================================================================================
#=======================================================================================================
#=======================================================================================================
# END: Ignore for now
#=======================================================================================================
#=======================================================================================================
#=======================================================================================================























#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: filename_access
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_access
try:
    #input = open( filename_access, encoding='utf-8-sig' )
    with open( results_dir + filename_access , 'w') as outfile:  
        for data_access in list_access:
            json.dump( data_access , outfile )
            outfile.write('\n')
except:
    pass
#copyfile( REF_dir + filename_access , results_dir + filename_access )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: filename_access
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#sys.exit(0)        


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: filename_attachments
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_attachments
try:
    #input = open( filename_attachments, encoding='utf-8-sig' )
    with open( results_dir + filename_attachments , 'w') as outfile:  
        for data_attachments in list_attachments:
            json.dump( data_attachments , outfile )
            outfile.write('\n')
except:
    pass
#copyfile( REF_dir + filename_attachments , results_dir + filename_attachments )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: filename_attachments
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#sys.exit(0)        


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: filename_brainusers
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_brainusers
try:
    #input = open( filename_brainusers, encoding='utf-8-sig' )
    with open( results_dir + filename_brainusers , 'w') as outfile:  
        for data_brainusers in list_brainusers:
            json.dump( data_brainusers , outfile )
            outfile.write('\n')
except:
    pass
#copyfile( REF_dir + filename_brainusers , results_dir + filename_brainusers )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: filename_brainusers
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  

#sys.exit(0)        


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: filename_calendarevents
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_calendarevents
#    <NONE>
try:
    #input = open( filename_calendarevents, encoding='utf-8-sig' )
    with open( results_dir + filename_calendarevents , 'w') as outfile:  
        for data_calendarevents in list_calendarevents:
            json.dump( data_calendarevents , outfile )
            outfile.write('\n')
except:
    pass
#copyfile( REF_dir + filename_calendarevents , results_dir + filename_calendarevents )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: filename_calendarevents
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  

#sys.exit(0)        
 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: filename_links
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_links
try:
    #print("#3: len(list_links) = ", len(list_links))
    #input = open( filename_links, encoding='utf-8-sig' )
    with open( results_dir + filename_links , 'w') as outfile:  
        for data_links in list_links:
            json.dump( data_links , outfile )
            outfile.write('\n')
except:
    pass
#copyfile( REF_dir + filename_links , results_dir + filename_links )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: filename_links
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  

#sys.exit(0)        
 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: filename_meta
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_meta
try:
    #input = open( filename_meta, encoding='utf-8-sig' )
    with open( results_dir + filename_meta , 'w') as outfile:  
        for data_meta in list_meta:
            json.dump( data_meta , outfile )
            outfile.write('\n')
except:
    pass
#copyfile( REF_dir + filename_meta , results_dir + filename_meta )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: filename_meta
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   
 
#sys.exit(0)        


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: filename_modificationlogs
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_modificationlogs
try:
    #input = open( filename_modificationlogs, encoding='utf-8-sig' )
    with open( results_dir + filename_modificationlogs , 'w') as outfile:  
        for data_modificationlogs in list_modificationlogs:
            json.dump( data_modificationlogs , outfile )
            outfile.write('\n')
except:
    pass
#copyfile( REF_dir + filename_modificationlogs , results_dir + filename_modificationlogs )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: filename_modificationlogs
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   
 
#sys.exit(0)        
    

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: filename_settings
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_settings
try:
    #input = open( filename_settings, encoding='utf-8-sig' )
    with open( results_dir + filename_settings , 'w') as outfile:  
        for data_settings in list_settings:
            json.dump( data_settings , outfile )
            outfile.write('\n')
except:
    pass
#copyfile( REF_dir + filename_settings , results_dir + filename_settings )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: filename_settings
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    

#sys.exit(0)        
    

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: filename_syncpoints
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_syncpoints
try:
    #input = open( filename_syncpoints, encoding='utf-8-sig' )
    with open( results_dir + filename_syncpoints , 'w') as outfile:  
        for data_syncpoints in list_syncpoints:
            json.dump( data_syncpoints , outfile )
            outfile.write('\n')
except:
    pass
#copyfile( REF_dir + filename_syncpoints , results_dir + filename_syncpoints )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: filename_syncpoints
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#sys.exit(0)        
    

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: filename_thoughts
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# filename_thoughts
try:
    #input = open( filename_thoughts, encoding='utf-8-sig' )
    with open( results_dir + filename_thoughts , 'w') as outfile:  
        for data_thoughts in list_thoughts:
            json.dump( data_thoughts , outfile )
            outfile.write('\n')
except:
    pass
#copyfile( REF_dir + filename_thoughts , results_dir + filename_thoughts )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: filename_thoughts
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#sys.exit(0)        
    

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# START: filename_tombstones
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    <NONE>
'''try:
    input = open( filename_tombstones, encoding='utf-8-sig' )
    with open( results_dir + filename_tombstones , 'w') as outfile:  
        for data_tombstones in list_tombstones:
            json.dump( data_tombstones , outfile )
            outfile.write('\n')
except:
    pass'''
copyfile( REF_dir + filename_tombstones , results_dir + filename_tombstones )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# END: filename_tombstones
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#make_archive( results_dir + 'results' , 'zip', results_dir)
#time.sleep(1)
#os.rename( results_dir + 'results.zip' , results_dir + 'results.brz' )



output_tmp.close()

print("DONE:")




