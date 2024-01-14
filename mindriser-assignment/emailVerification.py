def email_verification(email):
    email=input("Enter Your Email Here:- ")
    a=0
    b=0
    c=0
    if len(email)>=7:
        if email[0].isalpha():
            if ("@" in email)and(email.count("@")==1):
                if (email[-4]==".") ^ (email[-3]=="."):
                    for i in email:
                        if i.isspace():
                            a=1
                        elif i.isalpha():
                            if i==i.upper():
                                b=1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="@" or i==".":
                            continue
                        else:
                            c=1
                    if a==1 or b==1 or c==1:
                        print("Invalid Email 5")
                    else:
                        print(" Your Email is right")
                else:
                    print("Invalid Email 4")
            else:
                print("Invalid Email 3")
        else:
            print("Invalid Email 2")
    else:
        print("Invalid Email 1")
email_verification()