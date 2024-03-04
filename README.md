The system's implementation phase has been completed, aligning with the wireframe design. The system architecture comprises various components, including the home page, sign-in/sign-up form, recognized result page, explore page, compare page, detail page, map page, and user profile page![image](https://github.com/novailable/Aves/assets/97833342/fc47d939-b73f-49d1-ac57-d8e0a5ab4ec8)

 <img width="422" alt="image" src="https://github.com/novailable/Aves/assets/97833342/ea53ba49-7459-4521-bd4c-b361b9f69512">

Figure 7 1: Home Page
The main/home page serves as the focal point of the system. It features an upload file area where users can upload photos to recognize bird species. 
  
Figure 7 2: Search Box Inside Home
Adjacent to the upload area is the preview section, which includes a search bar for users to search for birds by name. Beneath the search bar is the preview area for uploaded photos, along with the recognition button. 
  
Figure 7 3: Popular Birds Section
Each time a user utilizes functions such as bird recognition, viewing details, or comparison, the popularity of the bird increases. The above figure is the "Popular Birds" section that showcases the highest popular birds, sorted and displayed from left to right. Additionally, the footer of the page includes a reminder to preserve and cherish avian life. On the right side of the footer is another reminder prompting users to log in for a better user experience. Upon clicking the “Sign In” button down below or the one in navigation bar, this login form will pop up. The "Sign Up" form will be displayed when the user clicks on the corresponding option in the navigation menu. Users can login or register from any page within the system.



7.1.2	Sign In/ Sign Up

                          
Figure 7 4: Sign In & Sign Up Form
Each form will feature validation formats for fields such as email and password confirmation. If the user does not meet the specified requirements, the submit button will remain disabled until the conditions are met.
                       
Figure 7 5: Error Messages for Sign In & Sign Up
Upon submission of the login form, the system will verify the credentials. In the event of a failure, a pop-up message will appear stating "Incorrect email or password.". For the registration process, if the user submits the registration form, the system will check if the email already exists in the database. If the email is already registered, the error message "Email already registered!" will be displayed. Both messages will automatically close upon clicking the exit button "x" or after 5 seconds.

 
Figure 7 6: User Icon Update in Navigation Bar
 
Figure 7 7: Your Finding Section in Home
After successful login or registration, the navigation bar will display both the logo and a logout button. There will be "Your Findings" section at the bottom of the home page, displaying user's recently recognized birds. User can click the heart icon next to each finding to mark it as a favorite. Once it marked the heart icon will change to red, signifying its status. Clicking on the profile picture will redirect user to profile page, where detailed user information is displayed.

7.1.3	User Profile
 
Figure 7 8: Profile Page
The above figure is profile page which allows users to modify their "username," "email address," and "password," as well as set a new profile picture. Beneath these options, a "Finding" section exhibits the bird species recognized from photo upload, with the number in the left-top corner indicating the frequency of recognition. Below is the "Favorite Birds" section that displays birds selected as favorites, with an "x" button in the right-top corner to remove birds from the list.
7.1.4	Explore
The explore page can navigated from the navigation bar. In the explore page, there are four filters and one search box available to facilitate exploration through the birds.
                                                     
Figure 7 9 Different Search Filters
In each filter, users can either type or click the dropdown button to navigate through the provided options, accompanied by pictures to aid in beginner understanding and visual comprehension. 
 
Figure 7 10: Explore Page
It's important to note that each bird can only have one size and order, so the bird size and order filters can only assign one value. However, other filters allow for the selection of multiple values to search for the bird. Additionally, users can narrow down the search results by entering the bird's name in the search bar located at the top of the right column.
When users find a bird of interest, they can either click on the detail button or the bird itself. This action will lead the user to the respective bird detail page.

7.1.5	Detail
 
Figure 7 11: Detail Page
The detail page provides the scientific name annotation, physical characteristics of the bird, as well as its description, distribution across the world, and ecology.

7.1.6	Comparison
 
Figure 7 12: Compare Box in Explore Page
At the explore page, users can click "Compare" to add a bird to the comparison section. When two birds are added, the compare button will be activated, and user can proceed to the compare page by clicking it.
 
Figure 7 13: Compare Page
The above figure is the comparison page, where bird physical characteristics are grouped and listed at the top for better understanding of each bird.

7.1.7	Recognition
![image](https://github.com/novailable/Aves/assets/97833342/24f45bb4-9d13-4fbb-99c6-a6c0a524fdf2)
