
# Quick Bank
Quick Bank is a Python terminal banking application, which runs in the Code Institute mock terminal on Heroku.  

Users can create accounts, make withdrawals, and deposits. The data is stored in a Google spreadsheet that is easy to access and read.  Balances are available before and after the transactions.  

The flow and input was designed with the user's comfort in mind. Minimal keystrokes and mouse use was a priority.  The terminal is easy to read, navigate and relays information in a simple way.  The user is prompted for information, making a user manual unnecessary.

[Click on this hyperlink for a live version of the project.](https://p3-bank2-bedbb06cdecb.herokuapp.com/).

![Responsive](assets/readme/am_I_responsive.png)



- - -

# Table of Contents
## [How To Transact](#how-to-transact-1)
## [Logic Flowchart](#logic-flowchart-1)
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
### [Features Left To Implement](#features-left-to-implement-1)
## [Data Model](#data-model-1)
## [Testing](#testing-1)
## [Design](#design-1)
## [Technologies Used](#technologies-used-1)
### [Language](#language-1)
## [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs-1)
### [Bugs](#bugs-1)
#### [Solved Bugs](#solved-bugs-1)
#### [Remaining Bugs](#remaining-bugs-1)
### [Validator Testing](#validator-testing-1)
## [Manual Testing](#manual-testing-1)
## [Deployment](#deployment-1)
## [Credits](#credits-1)
### [Code and Media](#code-and-media-1)
### [Content](#content-1)
## [Acknowledgements](#acknowledgements-1)

# Quick Bank
## How To Transact
You will be prompted to input an account number. If the account number is recognised as one of the current Google worksheets, you will be told what the balance is on the account. If the account number is not found, you will be prompted to create an account number or exit. 

If you did not exit, you will then be prompted to enter a transaction amount. After this you need to select a number from the menu for withdrawal or deposit. If you ask for a withdrawal amount bigger than your balance, you will received a notification of this and taken back to the account prompt menu.  If your withdrawal amount is smaller than your balance, you will be notified that the transaction was successful with the new balance.

The deposit transaction will be processed and a new balance provided at the end. The program closes with another prompt to exit. If you select not to exit you will be taken back to the account name prompt.

## Logic Flowchart
![Logic Flowchart](assets/readme/Logic%20Wireframe.png)

## User Experience (UX)
- Quick Bank provides a quick and easy way to keep track of your banking accounts. 
- Bulk data capture is possible if you input the account name with your left-hand. Your right-hand can then hover over the numpad for the rest of the selections. This makes for <b>as little weight-shifting and keystrokes as possible</b>.
- You are prompted with simple menu choices that allow you to transact quickly. 
- The layout is clear and efficient so that you can navigate through the program landscape easily and quickly.  
- You are prompted to exit at a few points in case you need to come back later or you changed your mind. 
- The logic is forgiving and predictive hopefully supporting your decision making as it unfolds.
- Very little room is given for user input error. The user is prompted to try again if invalid input is given - no fuss and efficiently. 

### User Stories
#### First-time Visitor Goals
- As a first-time visitor, I want to understand what is required from me at a glance.
- I want to be able to change my mind and start again quickly.
- I want to feel comfortable when there is not sufficient funds for a withdrawal. 
- I want to type with as few keystrokes as possible. 
- I would like my right-hand to hover over the numpad and the mouse - I don't want to have it return to the keyboard and so having to shift my weight.
- I don't want to have to ask an update, for example, like if you found my account or a balance. It should be automatically given.

#### Returning User Goals
- I don't want to have to remember which case I used for my accountname. 
- I don't want to be limited with numbers for an accountname. I want to be able to input an account name that is easy to remember.
- If I typed in the account name incorrectly, I should be asked before an account is created and I should find my way back to the account name prompt without fuss.
- I like to select the numbers, it fast and easy.

#### Frequent User Goals
- When I return I want to be able to transact quickly and see what the new balance is. 
- I want the menu to be predictable and easy to navigate.
- I want a forgiving data input standard that won't be rigid about the data I give by sending me directly back to the prompt menu.

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
- If you select that you do not want to exit, you will be taken to the account name prompt.

![Exit Prompt](assets/readme/account_name_second_try.png)

#### Create New Account
- The input is forgiving - you are prompted before creating a new account in case you made a typo.

![Create New Account Prompt](assets/readme/create_new_account.png)

#### Numerical Menu
- Where possible a numerical selection prompt has been used, avoiding extra unnecessary shifting of weight or changing of hands - it is assumed that you will have your one hand over the numpad anyway since you are doing financial work.
 
#### Transaction Amount Prompt
- The transaction decimal amount is automatically rounded to zero enabling the user to type in decimals if there are any and if there are not, it is assumed it is zero.
- Where possible the menu requires a numeric selection, cutting down on mouse use so avoiding shifting of the weight.  This is especially welcome when there is bulk data capturing required.

![Transaction Amount](assets/readme/transaction_amount.png)

#### Withdrawal 
- The system will check if the funds you are trying to withdraw is less than your balance (from the new account 0.00 or the found account).
- If the withdrawal exceeds the balance, you will get an error message (displayed above) and you will be taken to the transaction amount prompt where you can enter a smaller amount or the same amount.  From there you can also choose to deposit instead of withdraw - in case you selected the wrong transaction.
- Once the withdrawal is successful a message is displayed showing the new balance.

#### Deposit
- The deposit is added to the balance and a message displayed showing the new balance.

#### Exit on End of Transaction
- The user is prompted to exit or not to exit. If the user exits, the program is closed, if not the user is taken to the account name menu. This then allows for multi- or bulk data capturing efficiency.

#### Date and Time Automatically Captured
- The transaction date and time is automatically captured in the data worksheet to save the user effort. 
- This also gives the information more integrity for security reasons.

![Date and Time Automatically Captured](assets/readme/google_account.png)

### Features Left to Implement
 - <b>Future-proof</b> the programme by planning for a maximum amount of accounts and a new Google file being opened for <b>scalability</b> of the operation.
 - More color could be used for the messages to the user to enhance the experience positively.
 - A little explanation could be given about the account name being converted to lower case automatically to avoid user recording incorrect details in personal records.
 - Enhance features by providing for an interest earned calculation.  This would require a policy with scheduled interest rates that can then be compounded to reflect the correct interest earned for the user since the last transaction.
 - A feature charging the user a transaction fee for every transaction.
 - A feature sending a statement to the user.
 - A CSV file which can be downloaded by the user.
 - A query feature could be implemented giving users the opportunity to include other transactions.
 - Closing the account could also be another feature included (prompting the user for a contact opportunity which could be used to dissuade the user to change services).
 - Overdraft facilities would need the balances to be printed in green and red or with brackets to show credit.
 - International facilities could also be introduced further down the line with live linking to currency exchange.

## Data Model
Google Sheets was used to store account information for the application. Each user accountname generated a new worksheet with it's own date, transaction type, amount and balance column. The date and time was automatically entered for security, data integrity and efficiency reasons. The cred.json file was listed as one of the gitignore files.

## Testing
The project has been manually tested in the following way:
- The code was passed through a PEP8 linter and no error status is confirmed.
- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same inputs twice.
- Tested in my local terminal and Code Institute Heroku terminal.

## Design
- A flowchart was created in [Balsamiq Wireframes](https://balsamiq.com/wireframes).
- The site has been designed with an "easy to take in" style focussed on avoiding decision fatigue and information overload. The underlined navigation items tells you where you are.  
- Each stroke and click is efficient and intentional.

## Technologies Used
### Language
- Python 3 was used

## Frameworks, Libraries and Programs
- [Git](https://git-scm.com/) was used for version control.
- [Github](https://github.com/) wa used to save and store files.
- [Lightshot](https://app.prntscr.com/en/index.html) was used for screendumps.
- [Heroku](https://id.heroku.com/) was used to deploy the project.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the code.

### Bugs
#### Solved Bugs
- There were many parameter issues regarding the account name but this was solved with the help of Code Institute student support and my mentor. 
- There were also issues with the balance of the old accounts and the balance on the new accounts. Atomic, modular code helped me to separate the two and deal with them individually to ensure accuracy.
- Initially the wrong functions were being called and it was difficult to see where the code needed to be adjusted.  By sequencing the code from top to bottom as the user would, I was able to easily find problems and fix code. I also called the next function in the current one to avoid confusion and to adhere to the correct flow. It simplified the process.
- The initial gspead import gave several issues which were solved by updating imports.
- The creds.json file prompted a critical error which was solved using Google. 

#### Remaining Bugs
- There are no bugs remaining.

### Validator Testing
- Passed the code through a PEP8 linter and confirmed that there are no problems.

![PEP8 Linter](assets/readme/PEP8%20Linter.png)

## Manual Testing
| Test | Expected Functionality | Actual Behavior | Test Result |
| --- |---                   |---            |---|
| Account Name Space Enter | Prompt for valid input | Prompt for valid input | Test Passed |
| Account Name Blanc Enter | Prompt for valid input | Prompt for valid input | Test Passed |
| Account Name other characters (not alphnumeric) Enter | Prompt for valid input | Prompt for valid input | Test Passed |
| Account Name upper case only | Convert to lowercase | Convert to lower case | Test Passed |
| Create New Account Space Enter | Prompt for valid input | Prompt for valid input | Test Passed |
| Create New Account Name Blanc Enter | Prompt for valid input | Prompt for valid input | Test Passed |
| Create New Account Name other characters (not alphnumeric) Enter | Prompt for valid input | Prompt for valid input | Test Passed |
| Transaction Amount no decimals given | Round with no decimals | Round with no decimals | Test Passed |
| Transaction Amount with decimals | Include decimals | Include Decimals | Test Passed |
| Transaction Amount other characters | Prompt for valid input | Prompt for valid input | Test Passed |
| Transaction Amount Enter | Prompt for valid input | Prompt for valid input | Test Passed |
| Transaction Amount Spacebar | Prompt for valid input | Prompt for valid input | Test Passed |
| Withdrawal more than Balance | Balance with caution message and redirect User | User redirected to transaction amount | Test Passed |

## Deployment
This project was deployed using the Code Institute's mock terminal for Heroku with the following steps:
- Log in to Heroku or create a new account
- On the main page click "New" and select "Create new app"
- Choose your unique app name and select your region
- Click "Create app"
- On the next page find "settings" and locate "Config Vars"
- Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add"
- Scroll down, locate "Buildpack" and click "Add", select "Python"
- Repeat step 7. only this time add "Node.js", make sure "Python" is first
- Scroll to the top and select "Deploy" tab
- Select GitHub as deployment method and search for your repository and link them together
- Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
- View deployed site

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
- All content was written by Caylin Dewey

## Acknowledgements
- My mentor,<b> Mitko Bachvarov</b> provided helpful feedback and advice.
- <b>Code Institute </b> Slack community provided solutions and feedback.
- <b>Code Institute </b> tutors were quick to respond to my problems and to assist me - all with very little fuss!
