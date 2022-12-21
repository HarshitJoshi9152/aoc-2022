param([Int32] $day=-1, [Int32] $answer=0)

# if ($submit -eq $True)
# {
#   Write-Debug "Not implemented" # this is not shown with stdout
#   # hmm whats the difference
#   Write-Host "NOT IMPLEMENTED"
#   Exit 0
# }

if (!($day -lt 26 -and $day -gt 0))
{
  Write-Error "DAY MUST BE IN RANGE 1 TO 25"
  Exit 1
}


if ($answer -ne 0)
{
  # for submiting the result

  $submit_page_uri = "https://adventofcode.com/2022/day/$day"
  
  # 
  $session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
  $cookie = New-Object System.Net.Cookie 
  $cookie.Name = "session"
  $cookie.Value = Get-Content ".\.session"
  $cookie.Domain = "adventofcode.com"
  $session.Cookies.Add($cookie);
  # 
  
  $submit_page = Invoke-Webrequest $submit_page_uri -WebSession $session
  $submit_page.Forms[0].Fields.answer = $answer


  $submit_request = Invoke-WebRequest -Uri ($submit_page_uri + "/answer") -WebSession $session -Method POST -Body $submit_page.Forms[0].Fields

  Write-Output $submit_request.StatusCode
  Write-Output $submit_request.content

  Exit 0
}

# Check if folder for this day already exists

if (Test-Path ".\day")
{
  Write-Host "Folder for day $day already exists"
  Exit 1
}

# $Headers = @{
# 	'Cookie' = 'session=53616c7465645f5ff28db16ffb792bc5c10e8ef6c396612e0318e32aec7bc279f2b08a9048106512afea0643555d6df9b98edec06ecc1642511a936010f95719'
# }


$input_uri = "https://adventofcode.com/2022/day/$day/input"

# https://gist.github.com/lawrencegripper/6bee7de123bea1936359

$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
# inspect and research the WebRequestSession OBJECT PROPERTIES it might be helpful in understanding the HTTP protocol

$cookie = New-Object System.Net.Cookie 


# split the cookie name and Value by "="

$cookie.Name = "session"
$cookie.Value = Get-Content ".\.session"
$cookie.Domain = "adventofcode.com"

$session.Cookies.Add($cookie);


$day_input = Invoke-Webrequest $input_uri -WebSession $session
# Write-Output $day_input.content

# Make the folder and the required file and open them in code

[String] $day_folder = ".\day$day"

mkdir $day_folder

ni "$day_folder\input"
ni "$day_folder\code.py"
# ni "$day_folder\problem"

# $day_input.content | Write-Output "$day_folder\input" DOESNT WORK
Set-Content -Path "$day_folder\input" -Value $day_input


code "$day_folder\input"
code "$day_folder\code.py"


cd $day_folder

# Make the folder for this day if it doesnot exist
# [System.IO.File]::exists("C:\Users\harsj\code\aoc2022\aoc.ps1") or Test-Path


# todo: add a force flag