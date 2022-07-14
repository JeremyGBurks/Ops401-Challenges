# Author - Jeremy Burks
# Date Last Revised - 07/14/22
# Purpose - Automates the detection of SMBv1 then subsequently disables this insecure service, then automates the set-up of hardened password policies as directed by CIS Benchamark 1.1.5

#detects if SMBv1 is enabled and running
Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
#disables SMBv1
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
#applies to currently logged in user, sets lockout duration, observation window, enables password complexity, and minimum password length
Get-ADDefaultDomainPasswordPolicy -Current LoggedOnUser | Set-ADDefaultDomainPasswordPolicy -LockoutDuration 00:15:00 -LockoutObservationWindow 00:20:00 -ComplexityEnabled $true -MinPasswordLength 12
#and finally, restarts the conputer to enact all configurations
Restart-Computer 

#fin
