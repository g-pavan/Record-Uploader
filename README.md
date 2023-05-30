# Record Uploader

## About 

Welcome to my Django project, designed to help individuals like Sunita Sharma, who are 65+ years old, lead healthier and better lives. This application offers a range of features specifically tailored to their needs, making it easy for them to manage their health effectively.

One of the key features is the ability to upload hospitalized images. By simply selecting and sharing medical images, such as X-rays or scans, users can quickly provide healthcare professionals with the necessary visuals for diagnosis and assessment. This seamless image upload process aims to make it easier for individuals like Sunita Sharma to receive the medical attention they need promptly.

To enhance communication between users and healthcare professionals, I have integrated a commenting system. Through this system, Sunita Sharma can easily provide additional details, share symptoms, ask questions, or express any concerns related to her uploaded images. By facilitating clear and direct communication, my goal is to ensure that healthcare providers have all the necessary information to provide optimal care.

Managing uploaded images is made simple through my web portal. Sunita Sharma can effortlessly navigate through her collection, view images individually, and access any associated comments or notes. This feature enables her to conveniently review her medical records and keep track of her health journey.

To respect user control and privacy, I have included a feature that allows Sunita Sharma to delete her records when needed. This empowers her to manage her data in a way that aligns with her preferences, ensuring her privacy and giving her a sense of ownership over her health information.

My goal with this Django project is to provide an intuitive and secure platform for elderly individuals like Sunita Sharma. By leveraging technology, I aim to empower them to actively participate in their healthcare journey, leading healthier and more independent lives while receiving the necessary support from healthcare professionals.

**1. User Authentication:** The first step is to provide a login system for Sunita Sharma and other elderly users. This allows them to create their accounts and securely log in to the web portal.

**2. Dashboard:** Once logged in, Sunita Sharma will have access to a personalized dashboard where she can view her uploaded images, comments, and other relevant information.

**3. Record Upload:** Sunita Sharma can upload her hospitalized images through the web portal. This feature allows her to share medical images, such as X-rays or scans, with healthcare professionals for assessment and diagnosis.

**4. Commenting System:** To enable effective communication with healthcare professionals, Sunita Sharma can provide comments or additional information about her uploaded images. This feature allows her to explain her symptoms, ask questions, or share any concerns she may have.

**5. Record Management:** The web portal provides functionality for Sunita Sharma to view and manage her uploaded images. She can easily navigate through her image collection, view them individually, and access associated comments or notes.

**6. Record Deletion:** Sunita Sharma has the ability to delete her records if she no longer needs them or wants to maintain privacy. This feature allows her to manage her data according to her preferences.

## Steps to run the project

**Run the below commands after downloding the project**

*Step - 1: Create a python virtual environment*

  ```py -m venv .env```
  
*Step - 2: Activate virtual environment*

  ```./.env/scripts/activate```
  
*Step - 3: If needed make migrations* 

  ```python manage.py makemigrations accounts```

*Step - 4: [Mandatory in first run] Migrate the apps*

  ```python manage.py migrate```

*Step - 5: Run Django server then open the application*

  ```python manage.py runserver```


  *Note: To see the project refer Working Sample folder*


