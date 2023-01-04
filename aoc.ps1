param(
  [Int32] $day=-1,
  [Int32] $answer=0 
) # is there any None / NULL type in PS coz i cant leave it unassigned, OKAY MAYBE I CAN !


if (!($day -lt 26 -and $day -gt 0))
{
  Write-Error "DAY MUST BE IN RANGE 1 TO 25"
  Exit 1
}


# Check if folder for this day already exists

if (($answer -eq 0) -and (Test-Path ".\day$day"))
{
  Write-Output "Folder for day $day already exists"
  Exit 1
}

# Setting up cookies/session
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
# inspect and research the WebRequestSession OBJECT PROPERTIES it might be helpful in understanding the HTTP protocol
$cookie = New-Object System.Net.Cookie 
$cookie.Name = "session"
$cookie.Value = Get-Content ".\.session"
$cookie.Domain = "adventofcode.com"
$session.Cookies.Add($cookie);
# https://gist.github.com/lawrencegripper/6bee7de123bea1936359


# Submittig the answer
if ($answer -ne 0) # using $null instead of 0 doesnt work i wonder why
{
  # for submiting the result

  $submit_page_uri = "https://adventofcode.com/2022/day/$day"
  
  $submit_page = Invoke-Webrequest $submit_page_uri -WebSession $session
  $submit_page.Forms[0].Fields.answer = $answer


  $submit_request = Invoke-WebRequest -Uri ($submit_page_uri + "/answer") -WebSession $session -Method POST -Body $submit_page.Forms[0].Fields

  Write-Output $submit_request.StatusCode
  # to show response from the server
  $submit_request.ParsedHtml.getElementsByTagName("p") | %{$_.innertext} | Write-Output

  Exit 0
}

# did this work ? idr
# $Headers = @{
# 	'Cookie' = 'session=53616c7465645f5ff28db16ffb792bc5c10e8ef6c396612e0318e32aec7bc279f2b08a9048106512afea0643555d6df9b98edec06ecc1642511a936010f95719'
# }


$input_uri = "https://adventofcode.com/2022/day/$day/input"



# split the cookie name and Value by "="

$day_input = Invoke-Webrequest $input_uri -WebSession $session
# Write-Output $day_input.content

# Make the folder and the required file and open them in code

[String] $day_folder = ".\day$day"
[String] $input_file = "$day_folder\input"
[String] $solution_file = "$day_folder\code.$extension"
[String] $template_path = ".\template.py"

$null = mkdir $day_folder # assignment to $null to hide the output in terminal

$null = new-item $input_file
# The next line Messed up the encoding of the file or the contents somehow 
# But i dont know if it was because of `>` or because i used '$day_input.contents' instead of $day_input
# $day_input.content > $input_file # writing the input , todo: maybe i do want to shave off the extra newlines at the end ...

set-content -Path "$day_folder\input" -Value $day_input
# Get-Content "./template.py" > "$day_folder\code" # could be unsafe ! i dont want to overwrite the contents !

# note: actually its safe to just use the above line coz this part woulnt even run if the folder exists already, but i wanted to try to implement it anyways lol

# todo check the langauge chosen then use corresponding template if available

if (test-path $solution_file)
{
  Write-Output "$solution_file already exists, This operating would Overwrite the contents of $solution_file, proceed with CAUTION"
  Get-Content $template_path | set-content -Path $solution_file -Confirm
}
else {
  $null = new-item $solution_file
  Copy-Item -Path $template_path -Destination $solution_file
}


# open in vscode
code $input_file
code $solution_file


set-location $day_folder

# Make the folder for this day if it doesnot exist
# [System.IO.File]::exists("C:\Users\harsj\code\aoc2022\aoc.ps1") or Test-Path


# todo: add a force flag