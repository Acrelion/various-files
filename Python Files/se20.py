print "Ok, lets play a game."
print "Think of a number. Dont say it to me."
print
print "Are you ready? Press Enter if you are."
raw_input()
print
print "Now, add 2 to your number."
print "Next, multiply it by 3."
print "OK. And now add 4."
print "Good. One more thing - substract 10 now."
print
print "What is the result of all this? ",
user = raw_input ()

user_result = int(user)
number = user_result / 3

print
print "I think your number is %s" % number
print

conf = raw_input("Did I guessed right? Enter Y or N. " ).lower()
if conf == "y" or "yes":
    print
    print "Yeah! I guessed it! I cant believe this."
elif conf == "n" or "no":
    print
    print "Are you sure? Check your math again. You are lying."
else:
    print
    print "Whatever, I know I am right. Dont try to mock me."

#number = ((((x + 2) * 3) + 4) - 10) / 3
