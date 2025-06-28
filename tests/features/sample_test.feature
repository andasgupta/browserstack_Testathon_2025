Feature: Kolkata BugBash Application Tests
    As a user
    I want to test the Kolkata BugBash application
    So that I can verify login and e-commerce functionality

    Scenario Outline: Login with different credentials
        Given I open the browser
        When I navigate to "https://kolkata.bugbash.live/"
        And I click on the sign in button
        And I wait for the login page to load
        And I select username "<username>"
        And I select password "<password>"
        And I click the login button
        Then I should see "<expected_result>"

        Examples:
            | username  | password        | expected_result   |
            | demouser  | testingisfun99  | login_success     |
            | demouser  | wrongpassword   | Invalid Password  |
            | wronguser | testingisfun99  | Invalid Username  |

    Scenario: End-to-end shopping with Galaxy S20 Ultra (Bug Test)
        Given I login with valid credentials
        When I scroll to product "Galaxy S20 Ultra"
        And I add the product to cart
        Then the cart should remain empty

    Scenario: End-to-end shopping with iPhone 11 Pro
        Given I login with valid credentials
        When I scroll to product "iPhone 11 Pro"
        And I add the product to cart
        Then the cart should show 1 item
        And the subtotal should be "$ 699.00"
        When I increase the product quantity 4 times
        Then the cart should show 5 items
        And the subtotal should be "$ 3495.00"
        When I proceed to checkout
        And I fill shipping details
        And I submit the order
        Then I should see order confirmation
        And the order number should be displayed
        When I click download receipt
        Then the download should fail
        When I click continue shopping
        Then I should return to homepage

    Scenario: Cart management operations
        Given I login with valid credentials
        When I scroll to product "iPhone 11 Pro"
        And I add the product to cart
        Then the cart should show 1 item
        When I delete the cart item
        Then I should see empty cart message