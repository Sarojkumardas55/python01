Feature: OrangeHrm Login Functionality

  Scenario: Performing login to orangehrm
    When lunch the url and login to orrangehrm application
    Then click admin menu
    Then Click on qualification tab
    Then select add education from list
    Then click on add button
    Then add education "abc"
    Then check and save
    Then wait for "2" second
    Then logout from application
    Then I close the browser orangehrm application