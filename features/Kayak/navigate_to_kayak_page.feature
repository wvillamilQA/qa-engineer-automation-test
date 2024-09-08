@regression_tests


Feature: Validate element created dropdown column


  Scenario: Navigate to the Kayak home page and validate principal elements
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The page "should" contain the next elements
      | name                   | type   |
      | name_tag               | input  |
      | name_dropdown_column   | input  |
      | search_tag             | input  |
      | cancel                 | button |
      | create_column_disabled | button |


  Scenario: Validate URL of Home page
    Given I navigate to the kayak main page
    Then I should be in the "home" page
    And The url page should be equal to the next "https://www.kayak.com.co/" url


  Scenario Outline: Navigate between countries and validate the URL
      Given I navigate to the kayak main page
      Then I should be in the "home" page
      When I navigate to the "<url>" URL
      Then The url page should be equal to the next "<url>" url

    Examples:
      | url                       |
      | https://www.kayak.com.my/ |
      | https://www.kayak.com.pr/ |
      | https://www.kayak.com.br/ |

  @test
  Scenario Outline: Validate navigation through main menu options
    Given I navigate to the kayak main page
    When I click on the "<menu_option>" menu option
    Then The url page should be equal to the next "<expected_url>" url

   Examples:
    | menu_option   | expected_url                        |
    | flights       | https://www.kayak.com.co/flights    |
    | stays         | https://www.kayak.com.co/stays      |
    | cars          | https://www.kayak.com.co/cars       |
    | city_breaks   | https://www.kayak.com.co/citybreaks |

