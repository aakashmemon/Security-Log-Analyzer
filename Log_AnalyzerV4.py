with open("03 - Security_Log_Analyzer/security.log", "r") as file:

 # This here initialize Events

    failed_logins = 0
    successful_logins = 0
    logout = 0
    total_events = 0
    other_events = 0
    suspicious_users = []
    suspicious_ips = []

# V3 Tracks failed logins for each users

    failed_by_user = {}

# This tracks suspecious IPs

    failed_by_ip = {}

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

# Track By User

            if user in failed_by_user:
                failed_by_user[user] = failed_by_user[user] + 1
            else:
                failed_by_user[user] = 1

# Track By IP

            if ip in failed_by_ip:
                failed_by_ip[ip] = failed_by_ip[ip] + 1
            else:
                failed_by_ip[ip] = 1
        

        elif  "LOGIN_SUCCESS" in line:
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

# User Failure Track Output

    print("=======================")
    print(" Failed Logins By User ")
    print("=======================")
    print()

    for user in failed_by_user:
        
        print("User:", user)
        print("Failed Attempts:", failed_by_user[user])
        
        if failed_by_user[user] >= 3:
            print("⚠ Suspicious Activity Detected!")
            suspicious_users.append(user)
        
        print()

# IP by failure track

    print("=====================")
    print(" Failed Logins By IP ")
    print("=====================")
    print()
    
    for ip in failed_by_ip:
        print("IP:", ip)
        print("Failed Attempts:", failed_by_ip[ip])

        if failed_by_ip[ip] >= 3:
            print("⚠ Suspicious IP Detected!")
            suspicious_ips.append(ip)

        print()
        
    print()
    print("============================")
    print(" Suspicious Activity Report ")
    print("============================")
    print()

    print("Suspicious Users:")
    print()


    for user in suspicious_users:
        print("-", user)
    print()
    print("Suspicious IPs:")
      
        
    for ip in suspicious_ips:
        print("-", ip)
    print()