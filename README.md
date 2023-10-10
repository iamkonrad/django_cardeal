# django_cardeal (written in Django, using HTML and CSS)




## Some important points about this webapp:

1.DEFAULT ADMIN URL, default admin url IS NOT /admin, this project utilizes Honeypot; admin url path can be found inside the main app's (django_eshop) urls

2.USER AUTHORIZATION: For security reasons each person using this webapp needs to configure his/her own smtp settings, for now, only an EMAIL_BACKEND using django console handles that, but there are commented out lines in settings.py (the very bottom of the page) waiting to be filled with proper data in case there is a need to set profile update/password change/notifications/authorization handled by an smtp server (by default smtp server is set as Google);

3. USAGE of smtp server, in the relevant parts of the app there are commented out features allowing turning on smtp-related functions, they are commented out, but can be turned-on as per convenience and need


## Some of the key functionalities:
- User profile (registration/login/logout etc.)
- Multiple apps and views/dashboard etc.
- Fully-functional newsletter
- Pagination
- Styled admin panel (mainly with CSS)
- Safety features (admin honeypot)
- Securely stored secret key
- Session timeout
- Django messages (upon login, logout etc.)
- Few basic JS-related functions such as fetching the actual date from the db, different elements highlight
