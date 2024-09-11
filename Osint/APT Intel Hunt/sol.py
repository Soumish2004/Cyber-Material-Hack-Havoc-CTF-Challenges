import re
given='''Compromising their systems will involve a convincing phishing campaign. Ensure it's believable enough to deceive even the most vigilant employees.
 
Operations will commence once our custom malware is ready. 43 Four of our top coders are working tirelessly to craft malware capable of bypassing all known security protocols.
 
Planning for persistence within their systems is crucial. 4d We must ensure our foothold remains undetected and irremovable.
 
Thorough analysis of entry points is essential for lateral movement. 7b With multiple access routes, we'll infiltrate deeper into their network.
 
Executing the extraction phase demands precision. 34 Additional tools will be deployed to gather sensitive data and obscure our tracks.
 
Gathering unauthorized access requires coordination. 70 Every team member must be fully briefed and aware of their responsibilities.
 
Retaining the element of surprise is critical. 54 Our malware must evade detection to maintain operational secrecy.
 
Observation is key during the operation. 5f Continuous monitoring of their network activity will allow us to adapt swiftly.
 
Uninterrupted manipulation of their financial systems is necessary. 47 Success hinges on our ability to alter transactions undetected.
 
Preparation before launch is non-negotiable. 72 All systems must undergo rigorous testing to prevent any mishaps.
 
Senior members are overseeing the final stages. 30 They've provided invaluable guidance and support throughout the planning process.
 
Navigating through their systems will be challenging. 75 Once inside, we'll extract the data we need and erase all traces of our presence.
 
Laundering the stolen funds requires strategic planning. 50 By leveraging our connections, we'll ensure the money remains untraceable.
 
Final preparations are almost complete. 35 The final checks are underway to ensure no loose ends remain.
 
Zero room for error exists in this mission. 5f Our success depends on flawless execution and absolute precision.
 
Activating all stealth protocols is the last step. 4c Any lapse in judgment could compromise the entire operation.
 
Ready to proceed with the final phase. 34 Let’s make sure every team member is prepared to carry out their role.
 
Ultimate success will be achieved through careful planning. 7a We aim to maximize impact while minimizing our risk exposure.
 
System checks are concluding. 34 With all team members in position, the operation is set to launch.
 
Contingency plans are in place for unexpected complications. 52 Any deviation from the plan will be addressed promptly to ensure mission success.
 
Final adjustments to the malware are being completed. 75 Our tools will be optimized to ensure seamless execution during the operation.
 
Deployment of phishing campaigns is scheduled to begin. 35 This will initiate the infiltration phase and set the stage for subsequent actions.
 
Surveillance of target communications is underway. 7d Monitoring their interactions will provide insights into potential vulnerabilities.
 '''
given = given.replace('\n', ' ')
hex_codes = re.findall(r'\. ([0-9a-f][0-9a-f])', given)
for i in hex_codes:
    print(chr(int(i, 16)), end='')

