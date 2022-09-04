import pyrebase
from django.shortcuts import render

firebaseConfig = {
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "databaseURL": ""

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
