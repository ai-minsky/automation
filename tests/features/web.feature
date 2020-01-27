@web
Feature: Factorial Web Calculation
  As a developer,
  I want to calculate factorial,
  So I can verify that functionality of calculation factorial works correctly.


  Background:
    Given Factorial home page is displayed

  Scenario: Web application successfully calculate factorial in range 0 to 170
    When the user enter number "5"
    Then application shows factorial of "5" equals "120"

  Scenario: Application has correct title
    Then application title is "Factorial"

  Scenario: Application shows correct text body
    Then application shows textbody "The greatest factorial calculator!

  Scenario: Web application calculate infinity factorial for number more than 170
    When the user enter number "200"
    Then application shows factorial of "200" equals "Infinity"

  Scenario: Web application can calculate factorial only for numbers
    When the user enter number "Bla-bla-bla"
    Then application shows factorial of "Bla-bla-bla" equals "Please enter an integer"

  Scenario: Web application cannot calculate factorial for spaces
    When the user enter number "    "
    Then application shows factorial of "    " equals "Please enter an integer"

  Scenario: Web application doesn't support Java Script injection
    When the user enter number "<script> alert('Java Script injection'); </script>"
    Then application shows factorial of "    " equals "Please enter an integer"

  Scenario: Web application has correct footer
    Then application shows correct footer "© Qxf2 Services 2020

  Scenario: User can navigate to Terms and Conditions
    When the user navigate "Terms and Conditions"
    Then redirect to correct page "/privacy" "This is the terms and conditions document. We are not yet ready with it. Stay tuned!"

  Scenario: User can navigate to Privacy
    When the user navigate "Privacy"
    Then redirect to correct page "/terms" "This is the privacy document. We are not yet ready with it. Stay tuned!"

  Scenario: User can navigate to Qxf2 Services
    When the user navigate "Qxf2 Services"
    Then application title is "Qxf2 Services: Outsourced Software QA for startups"
