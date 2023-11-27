![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!



# Quick Bank
This app allows you to keep a record of all withdrawals and deposits made to various accounts.  It is an easy, simple, way to keep track of ledgers.

The site is responsive to viewing on mobiles, tablets, laptops, and desktops.  

![Responsive](assets/images/readme/am-i-responsive.png)

Please view the Decision Helper live project [here](https://caylindewey.github.io/project2-v1/).

- - -

# Table of Contents
## [User Experience](#user-experience-1)
### [User Stories UX](#user-stories-ux-1)
#### [First Time Visitor Goals](#first-time-visitor-goals-1) 
#### [Returning Visitor Goals](#returning-visitor-goals-1)
#### [Frequent Visitor Goals](#frequent-visitor-goals-1)

## [Features](#features-1)
### [Existing Features](#existing-features-1)
#### [Personalisation](#personalisation-1)
#### [Clear Buttons](#clear-buttons-1)
#### [Footer](#footer-1)
#### [Main Headings](#main-headings-1)
### [Features Left to Implement](#features-left-to-implement-1)
## [Design](#design-1)
### [Color Scheme](#color-scheme-1)
### [Typography](#typography-1)
### [Wireframes](#wireframes-1)
## [Technologies Used](#technologies-used-1)
## [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs-1)
## [Testing](#testing-1)
### [Issues and Bugs](#issues-and-bugs-1)
### [Validator Results](#validator-results-1)
### [Jshint Testing](#jshint-testing-1)
### [Manual Testing](#manual-testing-1)
### [WAVE Testing](#w)
### [Lighthouse Testing](#lighthouse-testing-1)
## [Deployment and Local Development](#deployment-and-local-development-1)
#### [How to Deploy](#how-to-deploy-1)
#### [How to Fork](#how-to-fork-1)
#### [How to Clone](#how-to-clone-1)
## [Credits](#credits-1)
### [Code and Media](#code--media-1)
### [Content](#content-1)
## [Acknowledgements](#acknowledgements-1)

# Decision Helper
## User Experience
- A <b>user-centered</b> approach was taken with the design of a lean, simple and elegant site.
- The user should be able to start the game, <i><b>filling in a name and then the question</i></b> within a short period of time.
- The site should be <b>future-proofed</b> to accomodate <b>scalability</b> but keep the navigation of the site consistent for the user - regardless of growth and expansion.  Future ideas are to include are pages with more elaborate decision making process. Theme-related advertising that can generate income can also be considered.


### User Stories UX
#### First Time Visitor Goals
- As a user, I want to be able to start this game quickly and generate a score for my decision easily. The decision should include a margin of randomness. The input of the user name and question is optional for this reason.

#### Returning Visitor Goals
- The same basic structure will allow for consistency and predictability for returning users.
- Users wuold be able to prepare better for decision making with each use but would have to return to this site for the random feedback.

#### Frequent Visitor Goals
- The user can easily access this site for decisions both big and small providing they want the random feedback in their decision.
- The user will be more mindfull of feelings with more use promoting emotional wellness.

## Features
- The site is responsive on all device sizes.

### Existing Features
#### Personalisation
- The user fills in the name and the question which adds a personalised element to the service.

![Personalised](assets/images/readme/personalised-site.png)
#### Clear Buttons
- The choices to make a decision is simple and clear. The user is encouraged to hit the buttons for every concern they have about the decision.

![Clear Buttons Desktop](assets/images/readme/clear-buttons-desktop.png)

On the mobile device the buttons are still easy to use. 

![Clear Buttons Mobile](assets/images/readme/clear-buttons-mobile.png)

#### Footer
- Disclaimer and copyright information prevents legal protection.

![Disclaimer](assets/images/readme/disclaimer.png)

#### Main Headings
The headings are clear and concise describing exactly what to do next. This avoids the need for rules and further explanations.

### Features Left to Implement
- In future links to professional services, decision tutorials, and personal growth courses, could be included on the site. 
- Adverts for these services could also generate income.

## Design
### Color Scheme
The following palette was selected from [My Color Space](https://mycolor.space/)

![Color Palette](assets/images/readme/color-palette.png)

### Typography
- The Lato family of fonts was chosen from [Google Fonts](https://fonts.google.com) with sans-serif in case it doesn't import.

### Wireframes
- [FigmaJam](https://www.figma.com/) was used to create wireframes that will scale up easily for teamwork. 
- The site has been designed with an "easy to take in" style focussed on avoiding decision fatigue and information overload. The underlined navigation items tells you where you are.  
- Each stroke and click is efficient and intentional.

![Design](assets/images/readme/wireframe.png) 

## Technologies Used
### Language
- HTML, CSS and Javascript was used

## Frameworks, Libraries and Programs
- [Git](https://git-scm.com/) was used for version control
- [Github](https://github.com/) wa used to save and store files
- [Lightshot](https://app.prntscr.com/en/index.html) was used for screendumps

## Testing
### Issues and Bugs
-  The web accessibility evaluation tool showed many tag and contrasting issues which had to be fixed https://wave.webaim.org/report#/https://caylindewey.github.io/project2-v1/. All errors are fixed.

- The reset function was initially triggered from the js function. It was moved to the HTML funtion after a jshint error was found. All errors are fixed.

### Validator Results 
- The W3C HTML Validator were used and Index.html passed the test  [W3C HTML Validtor](https://validator.w3.org/).

![Page validation result](/assets/images/readme/validator-html-result.png)

- The W3C CSS Validator was used and Style.css passed the test [W3C CSS Validtor](https://jigsaw.w3.org/css-validator/).

![CSS validation result](/assets/images/readme/validator-css-result.png)

### Jshint Testing
- No errors were found.

![Jshint result](/assets/images/readme/jshintResult.png)

### Manual Testing

| Test | Expected Functionality | Actual Behavior | Test Result |
| --- |---                   |---            |---|
| Random URL Load | Redirect User | Redirection executed with 404 page | Test Passed |
| Load on Browsers | Load successfully on Opera, Google Chrome, Microsoft Edge | Loaded successfully | Test Passed |
| Responsive to Varied Devices using Chrome Dev Tools | Tested desktop, tablet iPad Air and Samsung Galaxy A33 | Response Good | Test Passed |
| Buttons | All buttons responded as expected | Quick response and correct calculation | Test Passed |
| Fields Input Range | Text and numbers required | Did not respond | Test Failed |

![Error-404](assets/images/readme/error-404.png)

### Wave Testing (Web Accesibility Evaluation Tool)
- A few tag and contrasting errors were corrected [WAVE](https://wave.webaim.org/) which improved the lighthouse scores.

- Wave Testing Results were initially riddled with minor errors which have now been resolved.

![Wave Result](assets/images/readme/wave-results.png)

### Lighthouse Testing
#### Results
- Desktop Results were initially showing a low score on accesibility which have now been resolved.

![Lighthouse Desktop Result](assets/images/readme/lighthouse-desktop-test.png)

- Mobile Results were initially showing a low score on accesibility which have now been resolved.

![Lighthouse Desktop Result](assets/images/readme/lighthouse-mobile-test.png)

## Deployment and Local Development

### How to Deploy 
Github was used to deploy this site.  The steps are as follows:
1. Log into the [Github site](https://github.com/)
2. Pull up the repository for [Decision Helper](https://github.com/CaylinDewey/project2-v1)
3. Select the settings link, then the pages link.
4. In the source section choose 'main' from the dropdown menu.  
5. Select the 'root' from the drop menu and 'save'.
6. The URL that is displayed should have your live Github pages site. 

### How to Fork
1. Log into the [Github site](https://github.com/)
2. Pull up the repository for [Decision Helper](https://github.com/CaylinDewey/project2-v1)
3. Use to [fork button](assets/images/readme_github_fork.png) on the top right hand corner 

### How to Clone
1. Log into the [Github site](https://github.com/)
2. Click on the burger menu that will open up the repositories you are working on at the bottom.  Select the project you need.
3. Click on the clone button and select from HTTPS, SSH, or GitHub CLI.  Then copy the link shown.
4. Open your code editor terminal and change the current work directory to the location you want to use for the cloned directory.
5. Type in the terminal 'git clone' and paste your link here. 

## Credits
### Code and Media
- [Am I Responsive](https://ui.dev/amiresponsive) displays the site on a range of devices.
- [Code Institute Readme Template Tutorial](Code-Institute-Solutions/readme-template) 
- [Code Institute Readme from Thomas Tomo](https://github.com/Thomas-Tomo/Lunar-Escape) 
- [Code Institue Readme from Kera Cudmore](https://github.com/kera-cudmore)
- [freeCodeCamp Tutorial](https://www.youtube.com) was used for examples and learning.
- [Favicon](https://favicon.io/favicon-converter/) was used to create the favicon
- [Figjam](https://www.figma.com/) was used for the wireframe
- [Font Awesome](https://fontawesome.com/v4/icons/) was used for all icons 
- [Emoji](https://www.emojipedia.org) was used for hand emojis

### Content
- All content was written by Caylin Dewey

## Acknowledgements
- My mentor,<b> Mitko Bachvarov</b> provided helpful feedback and advice.
- <b>Code Institute </b> Slack community provided solutions and feedback.
- <b>Code Institute </b> tutors were quick to respond to my problems and to assist me - all with very little fuss!
