# Aves

The system's implementation phase has been completed, aligning with the wireframe design. The system architecture comprises various components, including the home page, sign-in/sign-up form, recognized result page, explore page, compare page, detail page, map page, and user profile page.

## Home

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/a3037175-5fcf-4ef2-9e8f-a4c3b7be3a2f">

The main/home page serves as the focal point of the system. It features an upload file area where users can upload photos to recognize bird species.

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/e1efff7c-f0f5-467f-834e-8655ae3b4114">

Adjacent to the upload area is the preview section, which includes a search bar for users to search for birds by name. Beneath the search bar is the preview area for uploaded photos, along with the recognition button.

<img width="400" alt="image" src="https://github.com/novailable/Aves/assets/97833342/f017acfa-d633-4341-bb3b-2032da53e08f">

Each time a user utilizes functions such as bird recognition, viewing details, or comparison, the popularity of the bird increases. The above figure is the "Popular Birds" section that showcases the highest popular birds, sorted and displayed from left to right. Additionally, the footer of the page includes a reminder to preserve and cherish avian life. On the right side of the footer is another reminder prompting users to log in for a better user experience. Upon clicking the “Sign In” button down below or the one in navigation bar, this login form will pop up. The "Sign Up" form will be displayed when the user clicks on the corresponding option in the navigation menu. Users can login or register from any page within the system.

## Sign In/ Sign Up

<img width="320" alt="image" src="https://github.com/novailable/Aves/assets/97833342/df2795b1-84de-4727-9b73-e444733e7944">
<img width="300" alt="image" src="https://github.com/novailable/Aves/assets/97833342/06714d0b-a947-4b48-87ca-4dac925e154f">

Each form will feature validation formats for fields such as email and password confirmation. If the user does not meet the specified requirements, the submit button will remain disabled until the conditions are met.

<img width="200" alt="image" src="https://github.com/novailable/Aves/assets/97833342/c67d317b-9a07-43e5-8a78-c001f8c32f21">
<img width="200" alt="image" src="https://github.com/novailable/Aves/assets/97833342/75623557-51c3-4f3d-ae92-1e32ab10adb4">

Upon submission of the login form, the system will verify the credentials. In the event of a failure, a pop-up message will appear stating "Incorrect email or password.". For the registration process, if the user submits the registration form, the system will check if the email already exists in the database. If the email is already registered, the error message "Email already registered!" will be displayed. Both messages will automatically close upon clicking the exit button "x" or after 5 seconds.

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/dda5ef8a-00ef-4eba-902a-3597b5ce3c4c">

After successful login or registration, the navigation bar will display both the logo and a logout button. There will be "Your Findings" section at the bottom of the home page, displaying user's recently recognized birds. User can click the heart icon next to each finding to mark it as a favorite. Once it marked the heart icon will change to red, signifying its status. Clicking on the profile picture will redirect user to profile page, where detailed user information is displayed.

## User Profile

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/d03d7679-8e00-4241-83bc-efb1a58e8306">

The above figure is profile page which allows users to modify their "username," "email address," and "password," as well as set a new profile picture. Beneath these options, a "Finding" section exhibits the bird species recognized from photo upload, with the number in the left-top corner indicating the frequency of recognition. Below is the "Favorite Birds" section that displays birds selected as favorites, with an "x" button in the right-top corner to remove birds from the list.

## Explore

The explore page can navigated from the navigation bar. In the explore page, there are four filters and one search box available to facilitate exploration through the birds.

<img width="300" alt="image" src="https://github.com/novailable/Aves/assets/97833342/627c276a-4606-4b2c-8a3b-15705d457e05">
<img width="300" alt="image" src="https://github.com/novailable/Aves/assets/97833342/41a6ecfd-338f-44f2-83e9-bf7d39da83ae">
<img width="300" alt="image" src="https://github.com/novailable/Aves/assets/97833342/4c849ffd-f384-4ed7-ada2-3d0b6e57ae31">
<img width="300" alt="image" src="https://github.com/novailable/Aves/assets/97833342/d918bdfb-d4e6-4bb7-9025-ab7d7686dd3e">

In each filter, users can either type or click the dropdown button to navigate through the provided options, accompanied by pictures to aid in beginner understanding and visual comprehension.

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/c51edb47-72b4-4f76-9f6e-1d9d6f1a3911">

It's important to note that each bird can only have one size and order, so the bird size and order filters can only assign one value. However, other filters allow for the selection of multiple values to search for the bird. Additionally, users can narrow down the search results by entering the bird's name in the search bar located at the top of the right column.
When users find a bird of interest, they can either click on the detail button or the bird itself. This action will lead the user to the respective bird detail page.

## Detail

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/00f2b52f-2876-4e0b-8612-1e08647ffdc0">

The detail page provides the scientific name annotation, physical characteristics of the bird, as well as its description, distribution across the world, and ecology.

## Comparison

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/d1972804-f12b-49ab-9929-f12b09d97bea">

At the explore page, users can click "Compare" to add a bird to the comparison section. When two birds are added, the compare button will be activated, and user can proceed to the compare page by clicking it.

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/be0a855e-4df7-41d4-9bf1-cddd0750752b">

The above figure is the comparison page, where bird physical characteristics are grouped and listed at the top for better understanding of each bird.

## Recognition

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/b3aaccad-f8b2-40f9-a041-27837b9e93c9">

In the home page, user can either drop, copy & paste or simply opening file dialog box to upload the photo. The uploaded photo will be shown as preview on the right side. Clicking the “Recognize” button initiates recognition process and the top three most probable results will then be displayed to provide user with potential matches.

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/086c4ab6-59c8-4adf-9805-729efc26d842">

On this results page following recognition, the left side displays the potential results, while the right side showcases the details of the first or highest-ranked result. Users can click on each result to view its details. Additionally, the "Compare" button allows users to initiate a comparison process, as previously described.

## Map

The Map page can be accessed from the navigation menu. When a user first enters the page, the system will request permission to access the user's location. Upon granting access, the following page will be displayed.

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/19e8935b-6d6f-47cb-ba6d-5744c0158b6c">

Within the map, users can explore bird watching areas within a 10km radius. The number of available birds watching areas can be found at the bottom of the map. The user's current location will be displayed in Latitude and Longitude. Moreover, clicking on the map will create a custom white marker with black circle in the middle. Clicking on this maker will zoom in to the marker’s location. After zooming in, users can click again to view a description of the route to get there, the route is preferred by less walking, for example, bus 106 is for the example custom marker. If user clicks the bird watching marker, the route will also be generated. Routes route can be deleted by re-clicking on markers, only custom markers can be removed by dragging and dropping them or by using button on the left of the map. Note that only custom marker can be deleted. This functionality is enabled using the Google Maps API.

# Machine Learning
## Dataset Preparing

For the machine learning model, I chose a dataset from Kaggle featuring 525 bird species. It includes 84,635 training images, 2,625 test images (5 per species), and 2,625 validation images, all in 224 x 224 x 3 color jpg format. The dataset is well-organized into subdirectories for each species and includes a birds.csv file with essential metadata. Each species has a minimum of 130 training images, but there's an imbalance between male and female images, with approximately 80% male and 20% female.
Since the dataset only provides images and bird names, I had to create a custom database tailored to my system for the detailed information of each bird species. However, due to time constraints, I could only create detailed profiles for 100 bird species.
To accommodate this, I trimmed the original Kaggle dataset to include only 100 bird species, resulting in 15,747 images for training, with 500 images each for validation and testing. This adjustment allowed for a more manageable dataset while still providing sufficient data for training and evaluation of the machine learning model.

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/38181fbc-5d5f-4aa1-9c4f-45d319eb6c85">

In the preprocessing step I load the data from the bird.csv file and give required variable for the model.

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/b5d51bb7-91e2-4333-b2da-ad459b8b9b74">

After that 100 bird data from my collection is read, and create a dataset that only matching the same name of birds from the original dataset. Then the file path location for the images are changes to suitable local path.

## Model Training

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/6a2f3b23-e908-4f65-ac48-8d67b6808f58">

The data is divided into train, test, and valid data frame depending on the value of the column ‘data set’. After that I data augmentation for each data set using augmentation techniques such as rotation, zoom, and horizontal flipping to the training images. These transformations introduce variability and diversity, helping the model learn robust features and reducing overfitting. Meanwhile, the validation data remains untouched to accurately assess the model's performance on original images.

<img width="400" alt="image" src="https://github.com/novailable/Aves/assets/97833342/e280b98c-cc5e-4541-8c02-13c880567cfc">

After that by utilizing the `flow_from_dataframe` method, data generators for training, validation, and testing datasets is created. Each generator is configured with DataFrame inputs, specifying the file paths and labels for images. Target image size, color mode, class mode, batch size, and shuffling settings are also specified. For training and validation, the data is shuffled and seeded for reproducibility, while the testing data remains unshuffled.

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/4fde26ba-0a93-47a4-b014-50bb981b1ba5">

With `get_model` function I defines a convolutional neural network (CNN) architecture using the Keras Sequential API. The model comprises several layers for feature extraction and classification. The base model consists of three convolutional layers, each followed by batch normalization and max-pooling operations to extract hierarchical features and downsample the spatial dimensions. Subsequently, the flattened output is passed through dense layers with batch normalization and dropout regularization to reduce overfitting. The final dense layer with softmax activation produces probabilities for each of the 100 bird species classes. This architecture is summarized using the `summary` method, providing insights into the model's structure and parameter count.

<img width="500" alt="image" src="https://github.com/novailable/Aves/assets/97833342/44049572-ba08-4409-84a8-e966dbfc77a4">

The model is compiled using the Adam optimizer with a learning rate of 0.0015. The loss function is set to categorical crossentropy, suitable for multiclass classification tasks, and accuracy is chosen as the metric for evaluation. Subsequently, the model is trained using the `fit` method, with the training data generator `train_df` passed as input. The number of epochs is set to 15, and the validation data generator `validation_df` is provided for model evaluation during training. Additionally, callbacks such as early stopping and model checkpointing are utilized to monitor training progress and save the best model weights.

<img width="300" alt="image" src="https://github.com/novailable/Aves/assets/97833342/280e639d-ea48-4b85-9b81-9a95932d83ea">

Finally, the model is saved as ‘bird_classification_model.h5’ in local file path. The saved model is loaded and used inside the ‘app.py’.

