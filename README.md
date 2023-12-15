# UiPath-Salesforce-API

Salesforce Validation Template

Overview

This automation is a starting point for a Salesforce Validation automation.  It begins by logging into a Salesforce account and downloads all the files associated with closed/won opportunities that closed after a certain date. Once downloaded, it goes through each file and extracts key data and compares the data to the data that was input in the fields.  If the data from the downloaded files and the fields match, then a validation was successful.

It performs the following key steps:

    1.	Logs into the Salesforce account using the provided credentials.
    2.	Queries for all closed/won opportunities after 8/1/2023 and loops through each one.
        1.	This could be modified to include an input user information to get start date/end date and opportunity status.
    3.	For each opportunity, it creates a folder using the opportunity name.
    4.	It queries for all files associated with that opportunity.
    5.	For each file, it downloads the file into the folder created earlier using the file name and extension.
    6.	After downloading all files for all opportunities, it loops through each folder.
    7.	For each folder, it determines the opportunity name, then loops through all files.
    8.	If a file is a MSG file, it extracts the email body and displays it.
    9.	Otherwise, it displays that it is not a mail message.


Key Components
•	Credentials: The bot logs into Salesforce using a hard-coded username, password, consumer key, consumer secret, and security token. These credentials should be stored more securely.
•	SalesforceApplicationScope: This wraps all the Salesforce operations and handles logging in.
•	SOQL Queries: SOQL queries are used to retrieve opportunities and associated files.
•	File Downloading: The Salesforce connector's DownloadFile method is used to download each file.
•	File Processing: Once files are downloaded, additional processing is done if it is a MSG file to extract the email body.
Notes
•	The file location for downloading is hard-coded and would need to be parameterized.
•	More validation and error handling could be added around the Salesforce operations.
•	The credentials should be stored securely rather than hard-coded.






Technical Documentation

Main Sequence
    Assign - Password
    •	Assigns a secure string variable secureVar to contain the hard-coded password
    Assign - Consumer Secret
    •	Assigns a secure string variable secureVar2 to contain the hard-coded consumer secret
    Assign - Security Token
    •	Assigns a secure string variable secureVar3 to contain the hard-coded security token

SalesforceApplicationScope

SalesforceApplicationScope
•	Logs into Salesforce using credentials stored in variables from main sequence
•	All Salesforce operations occur within this scope

Body Sequence
    Execute SOQL
    •	Executes SOQL query to get all closed/won opportunities after 8/1/2023
    •	Saves results to data table dtOpportunities
        •	Put SOQL code here

        For Each Row
        •	Loops through each row in dtOpportunities data table
        
        Body Sequence - For Each Row
            Assign
        •	Concatenates base folder path and opportunity name to create folder path for this opportunity


            Create Directory
            •	Creates folder using opportunity folder path
                Execute SOQL 2
                •	Executes SOQL query to get all ContentDocumentLinks for this opportunity
                •	Saves results to data table documentDataTable
                    •	Put SOQL code here
                        
                        For Each Row
                        •	Loops through each row in documentDataTable



                            Body Sequence - For Each Row - Inner For Each Row

                                Assign
                                •	Gets ContentDocumentId and saves to fileID variable

                                Assign
                                •	Gets ContentDocument.Title and saves to title variable

                                Assign
                                •	Gets ContentDocument.FileType and saves to fileType variable

                                Assign
•	Concatenates title and fileType to create file name
Download File
•	Downloads file using fileID, folder path, and file name
For Each
•	Loops through each folder in the base download path
Body Sequence - Outer For Each
Assign
•	Gets just the folder name from the path and saves to opportunityName
Assign
•	Searches dtOpportunities data table for row matching opportunityName
•	Saves row to opportunityRow variable
If
•	Checks if a matching opportunityRow was found
Body Sequence - Outer For Each - If
Assign
•	Gets all files in the current folder
For Each
•	Loops through each file
Body Sequence - Outer For Each - Inner For Each
If
•	Checks if file extension is .msg
Invoke Code
•	If .msg file, uses Outlook interop to extract email body text
Message Box
•	Displays email body text
Else Message Box
•	If not .msg, displays not a mail message
