#get email id

email = input("what is your email address?:" ).strip()

#slice username

username= email[:email.index("@")]
print(username)

#slice domainname

domain = email[email.index("@")+1:]

#format message

output = "Your username is {} and domain name is {}".format(username,domain)

#dislplay output  message

print (output)


