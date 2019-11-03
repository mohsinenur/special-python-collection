from os import walk
import json

res = {
  "name": "",
  "displayName": "",
  "webhookState": "WEBHOOK_STATE_UNSPECIFIED",
  "trainingPhrases": [],
  "buttons": [],
  "rootFollowupIntentName": "",
  "parentFollowupIntentName": "",
  "messages": [
    {
      "platform": "PLATFORM_UNSPECIFIED",
      "text": {
        "text": []
      }
    }
  ]
}

mypath = "small-talk"

for (dirpath, dirnames, filenames) in walk(mypath):
    for files in filenames:
        # opening json file
        with open(mypath +"/" + files) as json_file:
            data = json.load(json_file)
            
            # insert data
            if 'name' in data:
                res['displayName'] = data['name']
            if 'userSays' in data:
                res['trainingPhrases'] = []
                for says in data['userSays']:
                    if len(says['data']) > 1:
                        text = ""
                        for item in says['data']:
                            moreText = str(item['text']) 
                            text += moreText
                        res['trainingPhrases'].append(text)
                    else:
                        res['trainingPhrases'].append(says['data'][0]['text'])
            if 'responses' in data:
                res['messages'][0]['text']['text'] = data['responses'][0]['messages'][0]['speech']
        
        # updating json file
        with open(mypath +"/" + files, 'w') as outfile:
            json.dump(res, outfile)
    break


