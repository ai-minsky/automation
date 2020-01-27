###Setup 
``install chrome browser``
run the following command
```
pipenv install --dev
pipenv shell
```
###Run all tests:
```
py.test -vv --gherkin-terminal-reporter -n 6 --html report.html
```
###Generated html report contains API and UI tests:
```report.html```

###Bugs:
1. [Security] Web application uses simple HTTP, doesn't have a SSL certificate. It is easy to have man in the middle attack 
2. [REST API] Rest API should generate factorial only in range from 0 to 170. However API generates factorials between 0 to 900.
2. [REST API] Rest API generates 500 server error if number is more than 900.
3. [UI] Title has wrong spelling  title Factoriall. Should be Factorial.
4. [UI] Duplication 2020 in the copyright section. <script>document.write(new Date().getFullYear())</script> called twice.
5. [UI] Privacy and Terms and Conditions links has vice versa URLs

###P.S. 4 automated tests have failed as expected, there are bugs in the portal. 
#####This framework support Chrome browser now, support for other browsers can be add later 

## Copyright
This app was written by Andrei Izbavitelev