# Wasatch Academy Health and Wellness Auto Emailer

### The Problem

In order to ensure that our health insurance rates only 
increase by a percentage point or two, Wasatch Academy
needs 70% participation in Health and Wellness initiatives
through our health insurance provider Select Health. To provide context,
the items that need to be completed are:
1. Health Screening by workplace or other health provider
2. Digital Coaching through an App
3. Health Assessment Survey through an App
4. Two activity campaigns through an App

In the past, one of our employees would manually check the
status of reports sent to us through our health insurance
provider, Select Health. They would then send emails to all
delinquent employees reminding them of the initiatives 
they still needed to complete. This would take up hours
of their time every month or two. 

My goal of this project is to automate the process of 
sending out status updates for our health and wellness initiatives. Another
goal along the way is for me to build my skills in data reading and building
out workflows in code. I also want to explore creating modules to keep my 
main file smaller. 

### Running the Program

To run the program, ensure that all the correct packages are installed that
are listed in the requirements.txt file. The program also requires a password
for mailgun service, Excel document to be given, as well as a Google sheet 
that houses the employee email data as well as some other points of data.

Once everything is set, run the file auto_emailer_final.py. It will prompt for
a mailgun password as well as the name of the Excel file for the program to 
use.

This program could be adapted for other email sending scripts, but is 
specific to Wasatch Academy and its Health and Wellness Team. Individuals
should not try to clone and rerun this program as you may encounter significant
issues. Feel free to use, clone, and adapt to your own needs. 

### Overview and Results

Below is a screenshot of the Employee data for the health and wellness program. 
Names have been taken out to protect privacy.

[Initial Data](/Readme_Images/Select_Health_Data.png)

The Excel document is read in and converted to a Pandas Data Frame where the
data is then manipulated to make it easier to generate custom emails. After
manipulating the data to programmatically use, I merged this data frame with one
pulled from Google Sheets. This Google Sheets "Database" is where we are storing
employee email addresses as well as some other information. A screenshot of the
Google Sheets Database is shared below. 

[Google Sheets Database](/Readme_Images/Google_Sheets_Database.png)

The script will then loop through each row of the data, generate a custom email,
and send that email to the correct recipient. Below are screenshots of a few of the emails that
were generated.

[Email 1](Email_1.png) \
[Email 2](Email_2.png) \
[Email 3](Email_3.png) \
[Email 4](Email_4.png)

Emails were generated successfully and saved multiple days of work for one of our 
employees. 

Please reach out to Travis Magaluk if you have any questions regarding this work. 
