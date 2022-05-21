# Python - i18n

## Description of the files inside this folder:


0. This project module contains a single / route and an index.html template that simply outputs "Welcome to Holberton” as page title and “Hello world” as header.
1. This project module contains a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].
Use Config to set Babel’s default locale ("en") and timezone ("UTC"). Use that class as config for your Flask app.
2. This project module contains a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.
3. This project module contains a gettext function to parametrize your templates. Use the message IDs home_title and home_header. Create a babel.cfg. Initialize the translations and two dictionaries.
4. This project module contains a get_locale function that detects if the incoming request contains locale argument and ifs value is a supported locale, returns it. If not or if the parameter is not present, resort to the previous default behavior. Test using http://127.0.0.1:5000?locale=[fr|en].
5. This project module contains a get_user function that returns a user dictionary or None if the ID cannot be found or if login_as was not passed. Define a before_request function and use the app.before_request decorator to make it be executed before all other functions. before_request should use get_user to find a user if any, and set it as a global on flask.g.user..
6. This project module contains a get_locale function to use a user’s preferred local if it is supported.
7. This project module contains a get_timezone function and use the babel.timezoneselector decorator. Must validate that it is a valid time zone. To that, use pytz.timezone and catch the pytz.exceptions.UnknownTimeZoneError exception.


## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Python 3.8.10
- Style guidelines: [PEP 8](https://www.python.org/dev/peps/pep-0008/)

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>