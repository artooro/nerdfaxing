# Author: Arthur Wiebe <arthur@artooro.com>

import poplib
import email
import os
import subprocess

attachment_dir = "C:/nerds/faxes/"
mailboxes = [
        ('A Printer Name', 'pop.mailserver.com', 'fax1@domain.com', 'mailpassword'),
        ('Another printer', 'pop.mailserver.com', 'fax2@domain.com', 'mailpassword')
    ]

for name, server, user, pwd in mailboxes:
    print "Checking for attachments at %s" % name
    m = poplib.POP3_SSL(server, 995)
    m.user(user)
    m.pass_(pwd)
    numMessages = len(m.list()[1])
    for i in range(numMessages):
        response = m.retr(i+1)
        raw_message = response[1]
        msg = email.message_from_string("\n".join(raw_message))
        print "Checking message for attachments from %s" % msg.get('From')
        for part in msg.walk():
            print "Found file of type %s" % part.get_content_type()
            if part.get_content_type() == 'application/pdf':
                # Save and print the PDF
                print "Saving attachment"
                filename = part.get_filename()
                if not(filename): filename = "unknown.pdf"
                fp = open(attachment_dir + filename, 'wb')
                fp.write(part.get_payload(decode=1))
                fp.close()
                print "Sending PDF to printer."
                subprocess.call([
                    "C:/Program Files/Ghostgum/gsview/gsprint.exe",
                    "-printer",
                    name,
                    attachment_dir + filename
                    ])
                os.remove(attachment_dir + filename)
                
    m.quit()
