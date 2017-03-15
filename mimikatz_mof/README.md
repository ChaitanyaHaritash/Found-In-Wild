# MimiKatz Injection Silently

    While roaming in wild, i found this script on internet which stealthly injects mimikatz into target windows box with 
    the help of powershell onliner.
    
    Powershell oneliner is designed in such a way that it downloads invoke-mimikatz.ps1 from Powersploit's github repo and
    automatically executes it ... 
    
    Also ps oneliner will create a registery key "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\WDigest"
    with NT privs .. now when system is rebooted, attacker will get results in Apache logs(error.log) as POST data.
    
    All attacker need is to set his IP of running apache server in the script.
    
    I haven't tested it yet tho ... but if it works somehow then its one of best method i've seen so far for stealthly 
    credentials collection.
    
    # thanks to unknown researcher who wrote this script :) for this such an awesome method <3 ...
    
## Usage

    1. Save file as some.txt
    2. Open shell with privileged session and compile mof script with mofcomp (C:\>mofcomp file.txt)
    3. Reboot
