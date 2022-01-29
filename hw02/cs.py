def protected_secret(password, secret, num_attempts):
    """
    Returns a function which takes in a password and prints the SECRET if the password entered matches
    the PASSWORD given to protected_secret. Otherwise it prints "INCORRECT PASSWORD". After NUM_ATTEMPTS
    incorrect passwords are entered, the secret is locked and the function should print "SECRET LOCKED".

    >>> my_secret = protected_secret("correcthorsebatterystaple", "I love UCB", 2)
    >>> my_secret = my_secret("hax0r_1") # 2 attempts left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("correcthorsebatterystaple")
    I love UCB
    >>> my_secret = my_secret("hax0r_2") # 1 attempt left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("hax0r_3") # No attempts left
    SECRET LOCKED
    >>> my_secret = my_secret("correcthorsebatterystaple")
    SECRET LOCKED
    """
    
    p="SECRET LOCKED"
    def get_secret(password_attempt):
        while num_attempts>0:

            if password_attempt==password:
                print (secret)
                return get_secret
            else:
                m="INCORRECT PASSWORD"
                
                print(m)
                return get_secret
        return p
    if get_secret=="INCORRECT PASSWORD":
        num_attempts-=1
    


    return get_secret

##########################
# Just for fun Questions #
##########################