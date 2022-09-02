import pyrebase
from django.shortcuts import render

firebaseConfig = {
    "apiKey": "AIzaSyAFUxhJFDDx2Jb3CGGSbu0yCejKB7L2Caw",
    "authDomain": "onamscore.firebaseapp.com",
    "projectId": "onamscore",
    "storageBucket": "onamscore.appspot.com",
    "messagingSenderId": "106855565335",
    "appId": "1:106855565335:web:092921501950ca760eb452",
    "databaseURL": "https://onamscore-default-rtdb.firebaseio.com"

}

firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()


def index(request):
    stark = database.child("stark").get().val()
    lan = database.child("lan").get().val()
    bar = database.child("bar").get().val()
    tar = database.child("tar").get().val()
    stark1 = database.child("vote").child("stark").get().val()
    lan1 = database.child("vote").child("lan").get().val()
    bar1 = database.child("vote").child("bar").get().val()
    tar1 = database.child("vote").child("tar").get().val()
    print(stark,bar,tar,lan)
    return render(request, 'index.html', {'stark': stark,
                                          'lan': lan,
                                          'bar': bar,
                                          'tar': tar,
                                          'stark1': stark1,
                                          'lan1': lan1,
                                          'bar1': bar1,
                                          'tar1': tar1,
    })
