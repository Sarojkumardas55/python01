Feature: OrangeHrm Functionality

  Scenario: Performing login to application
    Given initialize the driver instance
    When lunch the url of application
    Then enter the "Admin" and "admin123" to application
    Then click on the login button
 #   Then verify the "title"
    Then I close the browser
