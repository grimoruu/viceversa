from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]

    count_of_number = len(user_text.split(' '))
    return render(request, 'reverse.html', {'usertext': user_text, 'reversetext': reversed_text, 'count_of_words': count_of_number})
