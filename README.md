# Get-Sysmon-Access-Rights
The Get-Sysmon-Access-Rights Splunk App has a function for creating and parsing mask strings. you can use it with "showaccessright" spl command in your SPL

# Installation Process
1- Copy Sysmon_Access_Right to splunk app directory
For example: cp -r Sysmon_Access_Right /opt/splunk/etc/apps/ 

2- Go to Sysmon_Access_Right bin directory 
For example: cd /opt/splunk/etc/apps/Sysmon_Access_Right/bin

3- Install splunk-sdk in Sysmon_Access_Right/bin directory
For example: pip install -t . splunk-sdk

4- Restart the Splunk Server
For example: /opt/splunk/bin/./splunk restart

5- Change the Get-Sysmon-Access-Rights app permission to all apps (system)
For example: Go to the Manage Apps section then search for Get-Sysmon-Access-Rights, then from sharing section choose Permissions then select all apps
