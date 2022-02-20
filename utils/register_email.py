from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from dt_one.settings import EMAIL_HOST_USER


def gmail_send_email(emailUser, password):
    subject = 'Welcome to DT One'
    context = {
        "email":emailUser,
        "password":password
    }
    html_message = render_to_string('email/welcome_email_template.html',context)
    # message = 'Visit the site and login with your email: {} and password: {}. You can change yor password after signing in.'.format(emailUser,password)
    plain_message = strip_tags(html_message)
    recepient = emailUser
    send_mail(subject, plain_message,
         EMAIL_HOST_USER, [recepient], fail_silently = False, html_message=html_message)


def loan_acknowledgement(emailUser):
    subject = 'Loan Acknowledgemet'

    html_message = render_to_string('email/acknowledgement.html')
    # message = 'Visit the site and login with your email: {} and password: {}. You can change yor password after signing in.'.format(emailUser,password)
    plain_message = strip_tags(html_message)
    recepient = emailUser
    send_mail(subject, plain_message,
         EMAIL_HOST_USER, [recepient], fail_silently = False, html_message=html_message)


def loan_approval(emailUser):
    subject = 'Loan Approval'

    html_message = render_to_string('email/approved.html')
    # message = 'Visit the site and login with your email: {} and password: {}. You can change yor password after signing in.'.format(emailUser,password)
    plain_message = strip_tags(html_message)
    recepient = emailUser
    send_mail(subject, plain_message,
         EMAIL_HOST_USER, [recepient], fail_silently = False, html_message=html_message)
         
        

def loan_denied(emailUser):
    subject = 'Loan Denied'

    html_message = render_to_string('email/denied.html')
    # message = 'Visit the site and login with your email: {} and password: {}. You can change yor password after signing in.'.format(emailUser,password)
    plain_message = strip_tags(html_message)
    recepient = emailUser
    send_mail(subject, plain_message,
         EMAIL_HOST_USER, [recepient], fail_silently = False, html_message=html_message)
