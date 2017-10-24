print "Let's make a cake!"
print
print "We can make #1 a sweet cake or #2 a salty cake."

choose_cake = raw_input("Press 1 for sweet or 2 for salty: ")

if choose_cake == "1":
    print "OK, everybody likes sweet cakes."
    print "1. Will it be with chocolate?"
    print "2. Will it be vanilla one?"
    choco_vanilla = raw_input("??? ")

    if choco_vanilla == "1":
        print "Yeah! We eat choco only!"
        print "But it's missing something. Will you add strawberries or bananas?"
        straw_ban = raw_input("Pick 1 for strawberries or 2 for bananas: ")

        if straw_ban == "1":
            print "Nice, now we have a sweet chocolate cake with strawberries."
            
        elif straw_ban == "2":
            print "Even better! We have a sweet chocolate cake with bananas!"
            
        else:
            print "%s may work, but I don't know." % straw_ban
        
    elif choco_vanilla == "2":
        print "Oh, boy! We have white delicious cake! But we need more."
        print "Pick 1 for cherries."
        print "Pick 2 for apples."
        cher_app = raw_input("What should we put on our vanilla cake? ")
        
        if cher_app == "1":
            print "Extra combo there! Vanilla cake with cherries!"
        elif cher_app == "2":
            print "Nice choise! Vanilla plus apples is yummy."
        else:
            print "I am not sure about %s. I am not sure at all." % cher_app
    else:
        print "I dont like to experiment with cakes.",
        print "Vanilla and chocolate are the best."

elif choose_cake == "2":
    print "That will be interesting."
    print "Will the cake be with #1 cheese or #2 cream?"
    cheese_or_cream = raw_input("Pick 1 or 2: ")
    
    if cheese_or_cream == "1":
        print "Now we have tasty salty cake with cheese. But what kind?"
        print "1. White cheese?"
        print "2. Or blue cheese?"
        kind_of_cheese = raw_input("1 for white or 2 for blue? ")
        
        if kind_of_cheese == "1":
            print "I like white cheese. Nice choise. We will have a great cake."
        elif kind_of_cheese == "2":
            print "This will be exotic salty cake with blue cheese. Viva la France!"
        else:
            print "I had cheese in mind. I am not sure about %s." % kind_of_cheese
    
    elif cheese_or_cream == "2":
        print "I like creams. What kind this one will be?"
        print "1. Mushroom cream?"
        print "2. Tomato cream?"
        kind_of_cream = raw_input("1 or 2? Hmmm... ")
        
        if kind_of_cream == "1":
            print "This will be great! Salty cake with mushroom cream. Daaaaamn!"
        elif kind_of_cream == "2":
            print "Quite the cake! Salty one with tomato cream. Will it look red?"
        else:
            print "This %s kind of cream is unknown to me. I am not sure about it." % kind_of_cream
    
    else:
        print "Salty cake with %s. But I had so many choices if you chose cream or cheese. Pitty." % cheese_or_cream

else:
    print "What kind of cake this %s will be? You've ruined everything." % choose_cake

