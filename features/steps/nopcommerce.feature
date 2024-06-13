Feature: Nopcommerce logo

  Scenario: Logo presence on nopcommerce homepage
    Given Launch chrome browser
    When open nop commerce homepage
    Then verify that the logo is present on the page
    And close browser
