

# cred_obj = firebase_admin.credentials.Certificate('dialogue-summary-platform-firebase-adminsdk-2hjle-ae40e973e7.json')
# default_app = firebase_admin.initialize_app(cred_object, {
# 	'databaseURL':databaseURL
# 	})
# firebase_admin.initialize_app(cred)

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Use the application default credentials
cred = credentials.ApplicationDefault()
cred_obj = firebase_admin.credentials.Certificate('dialogue-summary-platform-firebase-adminsdk-2hjle-ae40e973e7.json')
l = ['Salesforce/bart-large-xsum-samsum', 'philschmid/distilbart-cnn-12-6-samsum', 'henryu-lin/t5-large-samsum-deepspeed', 'linydub/bart-large-samsum', 'knkarthick/meeting-summary-samsum']
firebase_admin.initialize_app(cred_obj, {
  'projectId': 'dialogue-summary-platform',
})

db = firestore.client()

# users_ref = db.collection('responses')
annotators_ref = db.collection('annotators')
docs = annotators_ref.stream()
count=0
results = {}

for doc in docs:
#     count+=1
    response = doc.to_dict()

    results[response['name']] = response
#     s = doc.to_dict()['summary']
#     # print(s.path.split('/')[-1])
#     summary = s.get().to_dict()
#     results[summary['fname']] = {}
#     results[summary['fname']]['dialogue'] = summary['dialogue']
#     if 'response' not in results[summary['fname']]:
#       results[summary['fname']]['response'] = []
#     if 'scores' not in results[summary['fname']]:
#       results[summary['fname']]['scores'] = {}

#     for score in response['scores']:
#       if score not in results[summary['fname']]['scores']:
#         results[summary['fname']]['scores'][score] = [] 
#       results[summary['fname']]['scores'][score].append(response['scores'][score])

#     results[summary['fname']]['response'].append({
#       'salientInfo': response['salientInfo'],
#       'annotatorName': response['name'],
#       'scores': response['scores'],
#     })
# for key in results:
#     print(key)
# print(results)

with open("agreementresults.json", "w") as outfile:
    json.dump(results, outfile)
