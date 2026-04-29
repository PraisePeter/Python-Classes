"""

Step 1
In this workshop, you are going to build an Email Simulator that simulates sending, receiving, and managing emails between different users. You'll learn about classes, objects, and how to organize code in an object-oriented way.

Begin by creating a class named Email using the class keyword.

ANS:
class Email:
    pass

Step 2
Your Email class needs to store information about each email when it's created.

Inside your Email class, remove the existing pass keyword and create the __init__ method that takes self, sender, receiver, subject, and body as parameters.

ANS:
class Email:
    def __init__ (self, sender, receiver, subject, body ):
        pass

Step 3
Inside the __init__ method, you need to assign the parameter values to the object's attributes so each email can store its information.

Inside your __init__ method, remove the pass keyword and assign the parameters to self.sender, self.receiver, self.subject, and self.body.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

Step 4
Now let's test the Email class by creating an email object and checking that it stores information correctly. You'll print a couple of attributes to verify everything works.

Create an email object named email_obj with alice@example.com as the sender, bob@example.com as the receiver, Hello as the subject, and Hi Bob! as the body. Then print the sender and subject attributes as separate print statements to verify they are stored correctly.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

email_obj = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob!")
print(email_obj.sender)
print(email_obj.subject)

Step 5
Emails should track whether they've been read or not. Add a read attribute to the __init__ method and set it to False by default, since new emails start as unread.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
email_obj = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob!')
print(email_obj.sender)
print(email_obj.subject)


Step 6
Now let's test that the read attribute was added correctly to your Email class. Since you already have an email object from the previous steps, print the read attribute to see that it's now False by default.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

email_obj = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob!')
print(email_obj.sender)
print(email_obj.subject)
print(email_obj.read)

Step 7
Now you'll add a method to mark an email as read. When someone opens an email, you want to change its status from unread to read. This method will be simple - it just needs to set the read attribute to True.

Add a method called mark_as_read to your Email class. This method should take only self as a parameter and set the read attribute to True.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
    def mark_as_read(self):
        self.read = True
email_obj = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob!')
print(email_obj.sender)
print(email_obj.subject)
print(email_obj.read)


Step 8
Now, test the mark_as_read method you created in the Email class. Use the method on the existing Email object email_obj to change the status. After marking the email as read, print the read attribute of email_obj to confirm the change.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

email_obj = Email('alice@example.com', 'bob@example.com', 'Hello', 'Hi Bob!')
email_obj.mark_as_read()
print(email_obj.sender)
print(email_obj.subject)
print(email_obj.read)


Step 9
Remove the email_obj and the following print statements.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True


Step 10
Now that you have an initial setup of the Email class, it's time to create users who can send and receive emails. Each user will have a name and will be able to perform email operations.

Create a User class with an __init__ method that takes self and name as parameters. Within the class, assign the name parameter to self.name.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

class User :
    def __init__(self, name):
        self.name = name


Step 11
The User class needs a method to send emails to other users. When sending an email, you'll create a new Email object and add it to the receiver's inbox.

Create a method called send_email in your User class. This method should take parameters for receiver, subject, and body.

Inside the method, create a new Email object with the following parameter values and assign it to a variable named email:

sender: self (the current user)
receiver: receiver (the user receiving the email)
subject: subject (the subject of the email)
body: body (the body of the email

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

class User:
    def __init__(self, name):
        self.name = name
    def send_email(self, receiver,subject,body):
        email = Email(self,receiver,subject,body)


Step 12
Now that users can send emails, they need a way to store emails they receive. Each user should have an inbox to collect their emails.

Add an inbox attribute to the User class __init__ method and initialize it as an empty list []. This will store all emails that the user receives.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

class User:
    def __init__(self, name, inbox):
        self.name = name
        self.inbox = []
    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)


Step 13
While users can send emails and have inboxes, we need a dedicated class to manage inbox operations efficiently.

The Inbox class will store a list of emails and provide methods to add new emails, list all emails, and manage them.

Create a new class called Inbox with an __init__ method that initializes an empty list called emails.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = []

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)

class Inbox:
    def __init__(self):
        self.emails = []


Step 14
Now it's time to connect the User and Inbox classes so that emails can actually be delivered!

Users need to have proper Inbox objects instead of simple lists, and the send_email method should deliver emails to the receiver's inbox.

Update the User class __init__ in a way that each user gets an actual Inbox object instead of an empty list created earlier.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)

class Inbox:
    def __init__(self):
        self.emails = []


Step 15
Your inbox needs a way to receive new emails. When someone sends an email to a user, it should be added to their inbox.

Add a method called receive_email to your Inbox class that takes self and an email object email as parameters. Within the method body, add the email to the emails list using the append method.

ANS:
class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)


Step 16
Still within the send_email method, call the receive_email method of the receiver's inbox to add email to the receiver's inbox.

ANS:
def send_email(self, receiver, subject, body):
    email = Email(sender=self, receiver=receiver, subject=subject, body=body)
    receiver.inbox.receive_email(email)


Step 17
Now it's time to test our complete email system! Let's create some users and see the email functionality in action.

Create two User objects: alice with name "Alice" and bob with name "Bob". This will demonstrate how users can be created and interact with each other.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)

class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)

alice = User("Alice")
bob = User("Bob")


Step 18
Have Alice send an email to Bob to see if the email delivery works correctly.

Use Alice's send_email method to send Bob an email with subject "Hello" and body "Hi Bob, how are you?".

ANS:
alice = User("Alice")
bob = User("Bob")
alice.send_email(bob,"Hello","Hi Bob, how are you?")


Step 19
Now let's verify that the email was delivered successfully by printing the length of Bob's inbox emails.

ANS:
alice = User("Alice")
bob = User("Bob")

alice.send_email(bob, "Hello", "Hi Bob, how are you?")
print(len(bob.inbox.emails))


Step 20
Now that the email has been received, remove object creations, method calls, and print statements.

ANS:
class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)

class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)


Step 21
Users need a way to read their emails properly.

Add a display_full_email method to the Email class that takes only self as a parameter. Inside this method, call mark_as_read() method to mark the email as read when someone views it.

This method would be used to display the email's full content in a nicely formatted way.

ANS:
def mark_as_read(self):
    self.read = True
def display_full_email(self):
    self.mark_as_read()


Step 22
Now let's add a header to the email display. In the display_full_email method, after calling mark_as_read(), print \n--- Email --- to start the email display with a clear header.

ANS:
def display_full_email(self):
    self.mark_as_read()
    print("\n--- Email ---")


Step 23
Now let's display the sender and receiver information. To show who sent and received the email, add two print statements to the display_full_email method in this format:

From: sender where sender is replaced with the sender's name
To: receiver where receiver is replaced with the receiver's name

ANS:
def display_full_email(self):
    self.mark_as_read()
    print('\n--- Email ---')
    print(f"From: {self.sender.name}")
    print(f"To: {self.receiver.name}")

Step 24
Now add the subject line to the email display. In the display_full_email method, add a print statement to show the email's subject in this format:

Subject: subject where subject is replaced with the subject of the email

ANS:
def display_full_email(self):
    self.mark_as_read()
    print('\n--- Email ---')
    print(f'From: {self.sender.name}')
    print(f'To: {self.receiver.name}')
    print(f'Subject: {self.subject}')


Step 25
Now add the email body to complete the main content. In the display_full_email method, add another print statement in the format Body: body (where body is the content of the email) to show the email's content.

ANS:
def display_full_email(self):
    self.mark_as_read()
    print('\n--- Email ---')
    print(f'From: {self.sender.name}')
    print(f'To: {self.receiver.name}')
    print(f'Subject: {self.subject}')
    print(f'Body: {self.body}')


Step 26
Finally, let's add a footer to complete the email display format. Add a final print statement: print('------------\n') to close off the email display with a nice separator line.

ANS:
def display_full_email(self):
    self.mark_as_read()
    print('\n--- Email ---')
    print(f'From: {self.sender.name}')
    print(f'To: {self.receiver.name}')
    print(f'Subject: {self.subject}')
    print(f'Body: {self.body}')
    print('------------\n')


Step 27
Let's add a string representation to our Email class so we can display brief email summaries.

Add a __str__ method to the Email class that takes self as a parameter.

ANS:
def display_full_email(self):
    self.mark_as_read()
    print('\n--- Email ---')
    print(f'From: {self.sender.name}')
    print(f'To: {self.receiver.name}')
    print(f'Subject: {self.subject}')
    print(f'Body: {self.body}')
    print('------------\n')

def __str__(self):
    pass


Step 28
Within the __str__ method, you'll show whether an email has been read or not.

Conditional expressions allow you to assign a value based on a condition in a single line.

Here is an example:

Example Code
x = 10
y = 'Even' if x % 2 == 0 else 'Odd' # y will be Even
Within the method, before, use conditional expression to assign the string Read to a variable status if the email is read and Unread if it is not.

ANS:
def __str__(self):
    status = "Read" if self.read else "Unread"


Step 29
At the end of the __str__ method, return the email summary in this format:

Example Code
[status] From: sender | Subject: subject
Where status is the status of the email, sender is the sender's name and subject is the subject of the email.

ANS:
def __str__(self):
    status = 'Read' if self.read else 'Unread'
    return f"[{status}] From: {self.sender.name} | Subject: {self.subject}"


Step 30
Now you'll create a method to list all emails in the inbox. This method should handle the case where the inbox is empty and display a numbered list of emails when there are emails present.

Add a method called list_emails to your Inbox class that takes self as a parameter. First, create an if statement to check if the inbox is empty by testing the emails list. If it's empty, print the message Your inbox is empty.\n. Add a return statement to exit the method.

ANS:
def list_emails(self):
    if not self.emails:
        print("Your inbox is empty.\n")
        return


Step 31
After the empty inbox check, print the message \nYour Emails:. After that, iterate over all emails in the inbox using a for loop with enumeration. This is the syntax for enumeration with a starting number: enumerate(iterable, start=start_number).

Use enumeration to number the emails starting from 1. Use i (the index) and email (the email object) as the iteration variables.

Inside the loop, print an f-string with the iteration index followed by a ., then a space and the string representation of the email object in this format:

i. string_representation
Where i is the index and string_representation is the representation of the email object.

ANS:
def list_emails(self):
    if not self.emails:
        print('Your inbox is empty.\n')
        return
    print("\nYour Emails:")
    for i, email in enumerate(self.emails, start=1):
        print(f"{i}.{email}")


Step 32
The inbox needs a method to read a specific email. When a user wants to read an email, they'll specify which email number (starting from index 0) they want to see, and the method will display the full email content.

Add a method called read_email to your Inbox class that takes an index parameter. First, check if the inbox is empty and print the message Inbox is empty.\n if it is. Add a return statement after that to exit the method.

ANS:
def read_email(self, index):
    if not self.emails:
        print('Inbox is empty.\n')
        return

Step 33
When the inbox is not empty, you'll try to access the email at the given index and display it.

Remember in the list_emails method, you displayed email numbers starting from 1, but list indices in Python start from 0. So, you'll need to convert the 1-based index to a 0-based index by subtracting 1.

Within the read_email method, subtract 1 from the index parameter and store it in a variable called actual_index.

ANS:
def read_email(self, index):
    if not self.emails:
        print('Inbox is empty.\n')
        return
    actual_index = index - 1


Step 34
After getting the actual index, create an if statement to check if the actual_index is less than 0 or greater than or equal to the length of the self.emails list. If it is, print the message Invalid email number.\n and use return to exit the method.

ANS:
def read_email(self, index):
    if not self.emails:
        print('Inbox is empty.\n')
        return
    actual_index = index - 1
    if actual_index < 0 or actual_index >= len(self.emails):
        print("Invalid email number.\n")
        return


Step 35
When the email index is valid, access the email at actual_index, call its display_full_email method to show the email content.

ANS:
def read_email(self, index):
    if not self.emails:
        print('Inbox is empty.\n')
        return
    actual_index = index - 1
    if actual_index < 0 or actual_index >= len(self.emails):
        print('Invalid email number.\n')
        return
    self.emails[actual_index].display_full_email()


Step 36
Your inbox also needs a way to delete emails.

Python's del keyword can be used to delete items from a list by their index.

Add a method called delete_email to your Inbox class. Like read_email, it should:

Take an index parameter, check for an empty inbox, and print the message Inbox is empty.\n if it is. Use return to exit the method.

ANS:
def delete_email(self, index):
    if not self.emails:
        print('Inbox is empty.\n')
        return


Step 37
You should handle the case where the user tries to delete an email using an invalid index just like you did in the read_email method.

Within the delete_email method:

Convert the 1-based index parameter to a 0-based index by subtracting 1 and storing it in a variable called actual_index.
Create an if statement to check if the actual_index is less than 0 or greater than or equal to the length of the self.emails list. If it is, print the message Invalid email number.\n and use return to exit the method.

ANS:
def delete_email(self, index):
    if not self.emails:
        print('Inbox is empty.\n')
        return
    actual_index = index - 1
    if actual_index < 0 or actual_index >= len(self.emails):
        print('Invalid email number.\n')
        return


Step 38
When the inbox is not empty, and the email index is valid, delete the email at the given index using the del keyword and print a confirmation message Email deleted.\n.

ANS:
def delete_email(self, index):
    if not self.emails:
        print('Inbox is empty.\n')
        return
    actual_index = index - 1
    if actual_index < 0 or actual_index >= len(self.emails):
        print('Invalid email number.\n')
        return
    del self.emails[actual_index]
    print("Email deleted.\n")


Step 39
Now we're ready to add timestamps to our emails to track when they were sent and received.

First, import the datetime module at the top of your file.

ANS:
import datetime

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False


Step 40
Before integrating timestamps into our email system, let's practice working with datetime formatting. The datetime.datetime.now() function gives us the current date and time, and we can use the strftime() method to format it in different ways.

Here's how strftime() works with format codes:

Example Code
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d"))  # Output: 2024-03-15 (year-month-day with - separator)
The format codes like %Y (year), %m (month), %d (day) tell strftime() what to include, and you can add separators like - between them.

At the bottom of your code, create a variable called current_time and assign it datetime.datetime.now(). Then use strftime() to print the time in hours:minutes:seconds format using : as the separator.

Use these format codes: %H for hours (24-hour format), %M for minutes, and %S for seconds.

ANS:
current_time = datetime.datetime.now()
print(current_time.strftime("%H:%M:%S"))


Step 41
Great! Now that you've practiced datetime formatting, remove the current_time variable and the print statement from the bottom of your code. We'll integrate timestamps into the Email class in the next step.


Step 42
Now let's add timestamps to our emails. In the Email class __init__ method, create a timestamp attribute and assign the current time to it to automatically set a timestamp for when the email was created.

This is helpful for tracking when messages were sent and received.

ANS:
import datetime

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
        self.timestamp = datetime.datetime.now()


Step 43
Now let's show the timestamp when displaying the full email.

Below the subject, print the received timestamp using strftime to format it as '%Y-%m-%d %H:%M'. Use the following format:

Example Code
Received: date
Where date is formatted as '%Y-%m-%d %H:%M'.

ANS:
def display_full_email(self):
    self.mark_as_read()
    print('\n--- Email ---')
    print(f'From: {self.sender.name}')
    print(f'To: {self.receiver.name}')
    print(f'Subject: {self.subject}')
    print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
    print(f'Body: {self.body}')

Step 44
Now let's also show timestamps in the email listing. Update the __str__ method in the Email class to include the timestamp after the subject.

Modify the return statement to include the timestamp formatted as '%Y-%m-%d %H:%M' at the end, separated by | Time:.

The complete format should be:

Example Code
[status] From: sender | Subject: subject | Time: time 
Where status is the status of the email, sender is the sender's name, subject is the subject of the email, and time is in the format '%Y-%m-%d %H:%M'.

ANS:
def __str__(self):
    status = 'Read' if self.read else 'Unread'
    return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


Step 45
Users should get confirmation when they successfully send an email. Let's improve the user experience by adding feedback to the send_email method.

In the send_email method of the User class, add a print statement after the email is sent that shows confirmation. The message should be Email sent from [sender_name] to [receiver_name]!\n, where [sender_name] is replaced by the sender's name and [receiver_name] is replaced by the receiver's name.

ANS:
def send_email(self, receiver, subject, body):
    email = Email(sender=self, receiver=receiver, subject=subject, body=body)
    receiver.inbox.receive_email(email)
    print(f"Email sent from {self.name} to {receiver.name}!\n")


Step 46
Users should be able to check their inbox, read emails, and delete emails directly through their User object.

For checking the inbox, add a method called check_inbox to the User class. This method should print a personalized header with the user's name and then display all their emails.

The header should be formatted as: \nName's Inbox:, where Name is replaced with the name of the user.

After printing the header, call the list_emails() method on the user's inbox.

ANS:
class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

Step 47
For reading and deleting emails, add two methods to your User class: read_email and delete_email. Both should take an index parameter and call the corresponding method on self.inbox.

ANS:
    def check_inbox(self):
        print(f'\n{self.name}\'s Inbox:')
        self.inbox.list_emails()


    def read_email(self, index):
        self.inbox.read_email(index)


    def delete_email(self, index):
        self.inbox.delete_email(index)

Step 48
Now you'll create the main function that demonstrates your email simulator.

Create the main function and inside it, using the User class, create two users: Tory and Ramy and assign them to variables tory and ramy, respectively.

ANS:
def main() :
    tory = User("Tory")
    ramy = User("Ramy")


Step 49
Before sending the emails, add the standard Python idiom if __name__ == '__main__': followed by a call to main(). This ensures that the main function only runs when the script is executed directly, not when it's imported as a module.

ANS:
def main():
    tory = User('Tory')
    ramy = User('Ramy')

if __name__ == '__main__':
    main()


Step 50
Now you'll simulate sending some emails between the users.

In your main function, after creating the users, use the send_email method to:

Have Tory send an email to the ramy user object with subject Hello and body Hi Ramy, just saying hello!.
Have Ramy send an email to the tory user object with subject Re: Hello and body Hi Tory, hope you are fine.

ANS:
def main():
    tory = User('Tory')
    ramy = User('Ramy')
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
if __name__ == '__main__':
    main()


Step 51
Now you'll demonstrate the inbox functionality. Ramy will check his inbox, read the first email, delete the second email, and then check his inbox again to see the changes.

In your main function, after sending the emails, add code to:

Have Ramy check his inbox using the check_inbox method.
Have Ramy read the first email.
Have Ramy delete the first email.
Have Ramy check his inbox again.
With this, you have completed the email simulator!

ANS:


    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()
"""

import datetime


class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False

    def mark_as_read(self):
        self.read = True

    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class Inbox:
    def __init__(self):
        self.emails = []

    def receive_email(self, email):
        self.emails.append(email)

    def list_emails(self):
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')


class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        self.inbox.read_email(index)

    def delete_email(self, index):
        self.inbox.delete_email(index)


def main():
    tory = User('Tory')
    ramy = User('Ramy')

    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()


if __name__ == '__main__':
    main()