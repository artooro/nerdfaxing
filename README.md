nerdfaxing
==========

Will download PDF email attachments from a mail server and send them to a Windows printer.

## Dependencies

* GSview: http://pages.cs.wisc.edu/~ghost/gsview/
* Ghostscript: http://www.ghostscript.com/download/gsdnld.html
* Python 2.7: https://www.python.org/download/releases/2.7 (Download Windows MSI Installer)

**This script is not compatible with Python 3**

## Configuration and Setup


Edit fax_processor.py and you'll find a couple configurations that you will need to update:

> attachment_dir = "C:/nerds/faxes/"

Set the path to the folder you want the PDFs to be saved temporarily as they are sent to the printer. The files are deleted as soon as they are printed successfully. Note that even on Windows you should use / instead of \ in the path. Python automatically converts the / to \ when executing.

Modify the mailboxes section to include the Windows printer name, POP server, and the username, and password for the POP server.
The POP server needs to support SSL. This has been tested with Google's Gmail POP server at pop.gmail.com.

An example configuration for Gmail and a printer named "Main Office Printer" would be:

> mailboxes = [
        ('Main Office Printer', 'pop.gmail.com', 'myfaxes@gmail.com', 'thegmailpassword')
    ]

You can have multiple mailboxes setup to print to different printers. For example you can have 3 fax numbers going to different email accounts and have each email account print to a different networked printer.

**The final step** is to create a Windows scheduled task that executes the python script every 10-15 minutes or whatever you choose. The scheduled task should run C:\Python27\python.exe and have arguments set to the path of the python script, for example: C:\nerds\fax_processor.py

