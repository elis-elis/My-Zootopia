# My Zootopia project

Description:

Zootopia is an engaging Python-based project that enables users to discover information about various animals by fetching data from the API Ninjas Animals API. Users can input the name of an animal, and the program retrieves details (like their diet, location and type) about that animal, which are then formatted and presented in a user-friendly HTML file named animals.html.

* this project is part of the 'Masterscool' curriculum.

Workflow:

User Input: The program starts by asking the user to enter the name of an animal.

Fetching Data: Based on the entered animal name, the program requests data from the API Ninjas Animals API.

Handling Non-Existent Animals: If the API does not return data for the specified animal name, the program creates an HTML message indicating that the animal does not exist.

Loading Template: The program loads an HTML template with placeholders for the animal data.

Replacing Placeholders: The program inserts the fetched animal data into the template, replacing the placeholders with actual information.

Writing HTML File: The final HTML content is written to an output file named animals.html.

Result: The animals.html file is created or updated, containing some information about the specified animal or an appropriate message if the animal does not exist.

