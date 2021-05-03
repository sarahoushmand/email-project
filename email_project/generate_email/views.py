from django.shortcuts import render
from .models import Email, Message
import requests


def home(request):
    return render(request, 'generate_email/master.html')


def generate(request):
    response = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
    model = Email(address=response.json()[0])
    model.save()
    request.session['email'] = response.json()[0]
    request.session['username'] = response.json()[0].split('@')[0]
    request.session['domain'] = response.json()[0].split('@')[1]
    data = response.json()[0]
    return render(request, 'generate_email/master.html', {
        'email': data
    })


def email(request):
    inbox = getInbox(request)
    return render(request, 'generate_email/email.html', {'inbox': inbox})


def getMessage(request, pk):
    inbox = getInbox(request)
    [username, domain] = [request.session['username'], request.session['domain']]
    response = requests.get('https://www.1secmail.com/api/v1/?action=readMessage',
                            params={'login': username, 'domain': domain, 'id': pk})
    message = response.json()
    email = Email.objects.get(address=username + '@' + domain)

    Message.objects.get_or_create(id=message['id'],
                                  defaults={'email_from': message['from'], 'subject': message['subject'],
                                            'date': message['date'],
                                            'body': message['body'], 'attachment': message['attachments'],
                                            'email_id': email.id})
    return render(request, 'generate_email/message.html', {'message': message, 'inbox': inbox})


def getInbox(request):
    [username, domain] = [request.session['username'], request.session['domain']]
    response = requests.get('https://www.1secmail.com/api/v1/?action=getMessages',
                            params={'login': username, 'domain': domain})
    message = response.json()

    return message
