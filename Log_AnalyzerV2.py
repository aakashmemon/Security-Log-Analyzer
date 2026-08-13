with open("Security_Log_Analyzer/security.log", "r") as file:

 # This here initialize Events

    failed_logins = 0
    successful_logins = 0
    logout = 0
    total_events = 0
    other_events = 0

    for line in file:

        # Total Events Counter

        total_events = total_events + 1

        # Event Data

        parts = line.split()
        event = parts[0]

        # User Data
        
        user = parts[1].split("=")[1]
    
        # IP Data

        ip = parts[2].split("=")[1]
        
    #    print()
    #    print("===================")
    #    print()
    #    print("Event:", event)
    #    print("User:", user)
    #    print("IP:", ip)


        if "LOGIN_FAILED" in line:
            failed_logins = failed_logins + 1
#           print("⚠ Failed Login Detected:", line)

        
        elif "LOGIN_SUCCESS" in line:
            successful_logins = successful_logins + 1
#           print("Successful Login Detected:", line)

        elif "LOGOUT" in line:
           logout = logout + 1
#          print("⚠ Logout Detected:", line)

        else:
            other_events = other_events + 1
#           print("Other Events Detected:", line)
            


    # Total Final Statics 

    print()
    print("==========================")
    print(" Security Log Statistics ")
    print("==========================")
    print()
    print("Total Events:", total_events)
    print("Total Failed Attempts:", failed_logins)
    print("Total Successful Attempts:", successful_logins)
    print("Total Logout:", logout)
    print("Total Other Events:", other_events)
    print()