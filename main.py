from flask import Flask, jsonify
from googleapiclient.discovery import build
import json
import threading

app = Flask(__name__)

api_key = 'AIzaSyCDpDYJbTsKPD4tFWOzNxSSS5GeWM_Wzds'

ser = build('youtube', 'v3', developerKey=api_key)


# class start


class video:
    def __init__(self, title, description, publishDateTime, thumbnailURL):
        self.title = title
        self.description = description
        self.publishDateTime = publishDateTime
        self.thumbnailURL = thumbnailURL
# class end


def obj_dict(obj):
    return obj.__dict__


queryName = "programming"  # help of get videos data of a specific type

# This method will call updateList methode on every 20 seconds interval
def updateList():
    req = ser.search().list(q=queryName, part='snippet', type='video', maxResults=2,
                            order='date', publishedAfter='2020-01-01T00:00:00Z')
    dictionary = req.execute()

    del dictionary['etag']
    del dictionary['kind']
    del dictionary['nextPageToken']
    del dictionary['pageInfo']
    del dictionary['regionCode']

    for x in dictionary['items']:
        del x['etag']
        del x['kind']
        del x['snippet']['channelId']
        del x['snippet']['liveBroadcastContent']

    print(type(dictionary), len(dictionary))
    dic = dictionary
    print(type(dic), len(dic))
    return dictionary


dic = updateList()


@app.route('/')
def hello_word():
    return "hello world"


# call after 10 second
# This methode help to get updated youtube video details from youtube api



def callGoogleAPI():
    threading.Timer(20, dic=updateList).start()


# /api/videos/<type of video> path get json response which contains video details
# like (title, description, publishdatetime, thumbnailurl)
@app.route("/api/videos/")
def api_video():
    dic = updateList()

    return dic

# /api/videos/<title> path get json response which contains videos details
# which has same video title
@app.route("/api/videos/title/<string:title>")
def searchVideoByTitle(title):
    title = title.replace('-', ' ')
    tempList = {}
    for x in dic['items']:
        print(title)
        if x['snippet']['title'] == title:
            print("entered....")
            tempList = x

    return tempList

# /api/videos/<description> path get json response which contains videos details
# which has same video description
@app.route("/api/videos/description/<string:description>")
def searchVideoByDescription(description):
    description = description.replace('-', ' ')
    tempList = {}
    for x in dic['items']:
        mdescription = x['snippet']['description']
        print(mdescription, description)
        print(mdescription.startswith(description))
        if mdescription.startswith(description) == True:

            tempList = x

    return tempList


if __name__ == "__main__":
    callGoogleAPI()
    #dic = updateList()
    app.run(debug=True)
