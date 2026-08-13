with open("Security_Log_Analyzer/security.log", "r") as file:
    
    failed_logins = 0
    
    for line in file:

        # This gives Event Data

        parts = line.split()
        event = parts[0]

        # this Gives User Data
        
        user = parts[1].split("=")[1]
    
        # This Gives IP Data

        ip = parts[2].split("=")[1]
        
        print()
        print("===================")
        print()
        print("Event:", event)
        print("User:", user)
        print("IP:", ip)


        if "LOGIN_FAILED" in line:
            failed_logins = failed_logins + 1
            print("⚠ Failed Login Detected:", line)


    print()
    print("Total Failed Attempts:", failed_logins)
    print()