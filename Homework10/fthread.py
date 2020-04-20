import urllib.request as ur
import flags
import os
import time
import threading

#email
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def getGifs():
    if not os.path.exists('flags'):
        os.makedirs('flags')
    url = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/'
    for item in flags.flags:
        name = item + '-lgflag.gif'
        ur.urlretrieve(url + name, 'flags/' + name)
    ur.urlcleanup()

def main():
    print('Starting thread...')
    start = time.time()
    cpu = time.process_time()

    threads = []
    for n in range(4):
        thread = threading.Thread(target=getGifs)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()-start
    cpuEnd = time.process_time()-cpu

    with open('fthread.txt', 'w') as f:
        f.write(str(os.path.getsize('flags')) + ' bytes downloaded\n')
        f.write('It took ' + str(end) + ' seconds\n')
        f.write('It took the CPU ' + str(cpuEnd) + ' seconds\n')
    print('Finished')
    
    '''
    fromAdd = '**************************'
    toAdd = '************************'

    msg = MIMEMultipart()
    msg['Subject'] = 'Homework 10 Email Portion'
    msg['From'] = fromAdd
    msg['To'] = toAdd

    body = 'Here you go, Professor Durney!\nSincerely,\nMatthew Meyers'
    msg.attach(MIMEText(body, 'plain'))

    attachment = open('flags/us-lgflag.gif', 'rb').read()

    image = MIMEImage(attachment, name='us-lgflag.gif')
    image.add_header('content-disposition', 'attachment; filename = us-lgflag.gif')
    msg.attach(image)

    mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail.login(fromAdd, '********')
    mail.sendmail(fromAdd, toAdd, msg.as_string())
    mail.quit()
    '''

if __name__ == "__main__":
    main()