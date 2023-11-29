Feature: OrangeHrm Login Functionality

  Scenario: Performing login to orangehrm
    When lunch the url of orrangehrm application
    Then enter the "Admin" and "admin123" to orangehrm application
    Then click on the login button on orangehrm application
   # Then verify the "title" orangehrm application
    Then I close the browser orangehrm application