

# Quick Bank
Quick Bank is a Python terminal banking application, which runs in the Code Institute mock terminal on Heroku.  It can be used by anyone that has worked with a bank account before. It is ideal for anyone wanting to data capture banking details quickly and efficiently.

Users can create accounts, make withdrawals, and deposits. The data is stored in a Google spreadsheet that is easy to access and read.  Balances are available before and after the transactions.  

The flow and input was designed with the user's comfort in mind. Minimal keystrokes and mouse use was a priority.  The terminal is easy to read, navigate and relays information in a simple way.  The user is prompted at every step, making for easy navigation.  Bulk data capture is easily accomodated with only the keyboard use.

[Click on this hyperlink for a live version of the project.](https://p3-bank2-bedbb06cdecb.herokuapp.com/).

![Responsive](assets/readme/am_I_responsive.png)



- - -

# Table of Contents
## [How To Transact](#how-to-transact-1)
## [User Experience-(UX)](#user-experience-ux-1)
### [User Stories](#user-stories-1)
#### [First-time Visitor Goals](#first-time-visitor-goals-1)
#### [Returning User Goals](#returning-user-goals-1)
#### [Frequent User Goals](#frequent-user-goals-1)
## [Features](#features-1)
### [Existing Features](#existing-features-1)
#### [Intro Screen](#intro-screen-1)
#### [Account Name Prompt](#account-name-prompt-1)
#### [Exit Prompt](#exit-prompt-1)
#### [Create New Account](#create-new-account-1)
#### [Numerical Menu](#numerical-menu-1)
#### [Transaction Amount Prompt](#transaction-amount-prompt-1)
#### [Withdrawal](#withdrawal-1)
#### [Deposit](#deposit-1)
#### [Exit on End of Transaction](#exit-on-end-of-transaction-1)
#### [Date and Time Automatically Captured](#date-and-time-automatically-captured-1)
### [Future Features](#future-features-1)
## [Data Model](#data-model-1)
## [Design](#design-1)
## [Technologies Used](#technologies-used-1)
### [Language](#language-1)
## [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs-1)
## [Testing](#testing-1)
### [Validator Testing](#validator-testing-1)
### [Manual Testing](#manual-testing-1)
### [Bugs](#bugs-1)
#### [Solved Bugs](#solved-bugs-1)
#### [Remaining Bugs](#remaining-bugs-1)
## [Deployment and Local Development](#deployment-and-local-development-1)
### [Deploying to Heroku](#deploying-to-heroku-1)
### [Forking with GitHub Repository](#forking-with-github-repository)
### [Local Clone](#local-clone-1)
## [Credits](#credits-1)
### [Code and Media](#code-and-media-1)
### [Content](#content-1)
## [Acknowledgements](#acknowledgements-1)

# Quick Bank
## How To Transact
The logic flowchart below gives a diagramatic layout of how to transact.  Initially you will be prompted to input an account name. If the account name is recognised as one of the current Google worksheets, you will be told what the balance is on the account. If the account name is not found, you will be prompted to create an account name or exit. 

If you did not exit, you will then be prompted to enter a transaction amount. After this you need to select a number from the menu for withdrawal, deposit or exit. A withdrawal amount that is bigger than your balance, will prompt a notification and you will be taken back to the account prompt menu.  

If your withdrawal amount is smaller than your balance, you will be notified that the transaction was successful with the new balance.  The deposit transaction will be processed and a new balance provided at the end of the transaction. The program closes with another prompt to exit. 

If you select no on the exit menu, you will be taken back to the account name prompt.  The exit option is conveniently placed at the beginning, middle and end. 

## User Experience (UX)
- Quick Bank provides a quick and easy way to keep track of your banking accounts. 
- Bulk data capture is possible if you input the account name with your left-hand. Your right-hand can then hover over the numpad for the rest of the selections. This makes for 
 <b>fewer weight-shifting moments and fewer keystrokes</b>.
- You are prompted with simple menu choices (no more than 3 at a time) and you can enter in the number - so ensuring fewer errors and keystrokes.
- The layout is clear and efficient so that you can navigate through the program landscape easily and quickly.  
- You are prompted to exit at three crucial points for convenience - to either correct information given or to exit. 
- The logic is forgiving and predictive hopefully supporting your decision making as it unfolds.
- The user is <b> set up for success</b>.  Very little room is given for user input error. The user is prompted to try again if invalid input is given - no fuss and efficiently. 

### User Stories
#### First-time Visitor Goals
- As a first-time visitor, I want to understand what is required from me at a glance.
- I want to be able to change my mind and start again quickly.
- I want to feel comfortable when there is not sufficient funds for a withdrawal. 
- I want to type with as few keystrokes as possible. 
- I would like my right-hand to hover over the numpad - I don't want to have it return to the keyboard or mouse and so having to shift my weight. I can do that if my accountnames can be typed with my left-hand. Three letters and three digits are recommended for this.
- I don't want to have to ask for an update if you found my account or a balance. It should be automatically given to me.

#### Returning User Goals
- I don't want to have to remember which case I used for my accountname. 
- I don't want to be limited with numbers only or letters only - for an accountname. I want to be able to input an account name that is easy to remember.
- If I typed in the account name incorrectly, I should be asked before an account is created and I should find my way back to the account name prompt without fuss.
- I want to be able to exit quickly if I cannot continue.

#### Frequent User Goals
- When I return I want to be able to transact quickly and see what the new balance is. 
- I want the menu to be predictable and easy to navigate.
- I want a forgiving data input standard that will direct me to the prompt to try again automatically.

## Features
- The flow was created for a simple and efficient user experience that shows consideration for the user. 
- Minimal keystrokes was taken into consideration with the design of the menus and flow.
- It was also a consideration to make left-hand account naming possible leaving the right-hand available to hover over the numpad and ready for mouse use.

### Existing Features
#### Intro Screen
- A big welcome message is displayed to make the user feel welcome and at ease.
![Intro Screen](assets/readme/create_new_account.png)

#### Account Name Prompt
- The accountname is converted to lowercase automatically avoiding annoying the user when the accountname is not found due to case sensitivity.
- Account names can be typed with a left-hand, leaving the right-hand open to hover over the numpad and mouse. 
- Bulk data capturing is easy as you are prompted if the account name was not found, before you inadvertantly create an account that already exists.
- The accountname can accomodate alphanumeric keys allowing you to use Identification numbers, or fullnames or unique names that are easy-to-reference.  
- If you inadvertantly type in anything but the alphanumeric characters, you will be prompted to try again (this includes hitting enter with no input, a space, and other characters like "%$#@!").
- The account name is displayed in bold, so that you can see what you actually typed. 

#### Exit Prompt
- The exit prompt is provided at regular intervals to ensure that the user is given the opportunity to correct input or exit.
- If you select that you do not want to exit, you will be taken back to the accountname prompt.

![Exit Prompt](assets/readme/account_name_second_try.png)

#### Create New Account
- The input is forgiving - you are prompted before creating a new account in case you made a typo.

![Create New Account Prompt](assets/readme/create_new_account.png)

#### Numerical Menu
- Where possible a numerical selection prompt has been used, avoiding extra unnecessary shifting of weight or changing of hands - it is assumed that you will have your one hand over the numpad anyway since you are doing financial work.
 
#### Transaction Amount Prompt
- The transaction decimal amount is automatically rounded to zero enabling the user to type in decimals.  If no decimals are entered, it is assumed it is zero.  If decimals are entered, it is taken into the calculations automatically.
- Where possible the menu requires a numeric selection, cutting down on keystrokes.  This is especially welcome when there is bulk data capturing required.

![Transaction Amount](assets/readme/transaction_amount.png)

#### Withdrawal 
- The system will check if the funds you are trying to withdraw is less than your balance (from the new account 0.00 or the found account).
- If the withdrawal exceeds the balance, you will get an error message (displayed above) and you will be taken to the transaction amount prompt where you can enter a smaller amount or the same amount.  
- From there you can also choose to deposit instead of withdraw (you may have simply selected the wrong transaction).  
- Once the withdrawal is successful a message is displayed showing the new balance.

#### Deposit
- The deposit is added to the balance and a message displayed showing the new balance.

#### Exit on End of Transaction
- The user is prompted to exit or not to exit. If the user exits, the program is closed, if not the user is taken to the account name menu. This then allows for multi- or bulk data capturing efficiency.

#### Date and Time Automatically Captured
- The transaction date and time is automatically captured in the data worksheet to save the user effort. 
- This timestamp also serves as a reference for multiple transactions on one day.
- It also gives the information more integrity for security reasons.

![Date and Time Automatically Captured](assets/readme/google_account.png)

### Future Features
 - A secure entry system with authenticated passwords.
 - A search list on current names per authenticated user entered. 
 - <b>Future-proof</b> the programme by planning for a maximum amount of accounts for the Google worksheet.
 - <b>Scalability</b> is important, gear the programme to automatically add another Google account if needed.
 - Add an compound interest earned calculation and transaction fee charged feature.
 - Add a statement emailed to user and a CSV dowlload file and a interface with accounting softawre feature.
 - A query and overdraft feature.
 - International facilities could also be introduced further down the line with live linking to currency exchange.

## Data Model
Google Sheets was used to store account information for the application. Each user account name generated a new worksheet with it's own date and time, transaction type, amount and balance column. The date and time was automatically entered for security, <b>data integrity</b> and efficiency reasons. The cred.json file was listed as one of the gitignore files.

## Design
- A flowchart was created in [Balsamiq Wireframes](https://balsamiq.com/wireframes).
- The site has been designed with an "easy to take in" style focussed on avoiding decision fatigue and information overload. The underlined navigation items tells you where you are.  
- Each stroke and click is efficient and intentional.

![Design Workflow](assets/readme/logic_wireframe.png)

## Technologies Used
### Language
Python 3 was used.

## Frameworks, Libraries and Programs
- [Git](https://git-scm.com/) was used for version control.
- [Github](https://github.com/) wa used to save and store files.
- [Lightshot](https://app.prntscr.com/en/index.html) was used for screendumps.
- [Heroku](https://id.heroku.com/) was used to deploy the project.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the code.

## Testing
### Validator Testing
The project passed the code through a PEP8 linter with no problems.

![PEP8 Linter](assets/readme/pep8_linter.png)

## Manual Testing
| Test | Expected Behavior | Test Result |
| --- |--- |--- |
| Account Name input empty | Error message displayed and user is asked to try again | Passed |
| Account Name input non-alphanumeric characters | Error message displayed and user is asked to try again | Passed |
| Account Name input uppercase and lowercase |  Automatically convert to lowercase | Passed |
| Account Name input Enter key only | Error message displayed and user is asked to try again | Passed |
| Account Name input Spacebar key only | Error message displayed and user is asked to try again | Passed |
| Transaction Amount empty | Error message displayed and user is asked to try again | Passed |
| Transaction Amount non-numeric characters | Error message displayed and user is asked to try again | Passed |
| Transaction Amount no decimals given | Amount is displayed with no decimals | Passed |
| Transaction Amount with decimals | Amount is displayed with the given decimals | Passed |
| Transaction Amount Enter key only | Error message displayed and user is asked to try again | Passed |
| Transaction Amount Spacebar key only | Error message displayed and user is asked to try again | Passed |
| Withdrawal more than Balance | Error message displayed and user is asked to try again | Passed |

## Bugs
### Solved Bugs
- There were many parameter issues regarding the account name intially.  These are all fixed. 
- The sequencing of creating a new account had to be adjusted to ensure that the correct balance was given if the account was found. This was fixed by using nested functions and atomic style coding.
- The initial gspead import gave several issues, which were solved by updating imported library versions.

### Remaining Bugs
There are no bugs remaining.

## Deployment and Local Development
### Deploying to Heroku
This project was deployed using the Code Institute's mock terminal for Heroku with the following steps:
1. Log in to Heroku or create a new account.
2. On the main page click 'New' and select 'Create new app'.
3. Choose your unique app name and select your region.
4. Click 'Create app'.
5. On the next page find 'settings' and locate 'Config Vars'.
6. Click 'Reveal Config Vars' and add 'PORT' key and value '8000', click 'Add'.
7. Scroll down, locate 'Buildpack' and click 'Add', select 'Python'.
8. Repeat step 7. only this time add 'Node.js', make sure 'Python' is first.
9. Scroll to the top and select 'Deploy' tab.
10. Select GitHub as deployment method and search for your repository and link them together.
11. Scroll down and select either 'Enable Automatic Deploys' or 'Manual Deploy'.
12. View deployed site.

### Forking with GitHub Repository
Forking the repository enables us to make a copy of the original repository to change and view without affecting the original repository.
1. Log in to the Github repository.
2. Select the 'Fork' button which is found at the top under the main menu.
3. You now have a copy of the original repository.

### Local Clone
1. Log into the GitHub repository.
2. Select the 'Clone or download' button.
3. Click on the 'code' button, select clone with HTTPS, SSH or GitHub CLI and copy the link.
4. Open Git Bash.
5. Change the current working directory to the desired one.
6. Type 'git clone' and then past the URL copied in step 3.
7. Press the 'Enter' key to create your local clone.  

## Credits
### Code and Media
- [Am I Responsive](https://ui.dev/amiresponsive) displays the site on a range of devices.
- [Code Institute Readme Template Tutorial](Code-Institute-Solutions/readme-template).
- [Code Institue Readme from Kera Cudmore](https://github.com/kera-cudmore).
- [FreeCodeCamp Tutorial](https://www.youtube.com) was used for examples and learning.
- [Emoji](https://www.emojipedia.org) was used for emojis.
- [Dave Gray Beginners Python Course](https://www.youtube.com/results?search_query=codeforfree+dave) helped me gain understanding.
- [Thomas Tomo Readme File](https://github.com/Thomas-Tomo/hangman/blob/main/README.md#how-to-play-1) provided by Mitko Bachvarov.

### Content
All content was written by Caylin Dewey

## Acknowledgements
- My mentor,<b> Mitko Bachvarov</b> provided helpful feedback and advice.
- <b>Code Institute </b> Slack community provided solutions and feedback.
- <b>Code Institute </b> tutors were quick to respond to my problems and to assist me - all with very little fuss!
