import os.path

from django.shortcuts import render, redirect

# CONSTANTS
PATH_TO_VIDEOS = 'sl_videos'


def home(request):
    if request.method == "POST":
        word = request.POST['name_textarea']
        word = word.strip()
        return redirect('translate_word', word=word)
    else:
        return render(request, 'home.html', {'valid': 0})


def translate_word(request, word):
    if request.method == "POST":
        word = request.POST['name_textarea']
        word = word.strip()
        return redirect('translate_word', word=word)

    else:
        path_to_word = ""
        valid = 0

        user = request.user
        print(user, "Translated: ", word)

        # TODO: Check if word in database
        database = ['area', 'book']
        if word in database:
            valid = 1
            # TODO: add to translations database that user X translated word Y
            word_ext = word + '.mp4'
            path_to_word = os.path.join(PATH_TO_VIDEOS, word_ext)
            print('pss')

        else:
            # TODO: fuzzywuzzy
            valid = 2
            word = "area"
            print("not pss")

        return render(request, 'home.html', {'word': word, 'path_to_word': path_to_word, 'valid': valid})
