Feature: E2E Shopping Flow Tests
    As a customer
    I want to complete end-to-end shopping scenarios
    So that I can verify the complete purchase flow

    Background:
        Given I login with valid credentials

    Scenario Outline: Add different products to cart
        When I scroll to product "<product>"
        And I add the product to cart
        Then the cart should show <expected_items> item
        And the subtotal should be "<expected_total>"

        Examples:
            | product         | expected_items | expected_total |
            | iPhone 11 Pro   | 1              | $ 699.00       |

    Scenario: Complete purchase flow with quantity changes
        When I scroll to product "iPhone 11 Pro"
        And I add the product to cart
        And I increase the product quantity 2 times
        Then the cart should show 3 items
        When I proceed to checkout
        And I fill shipping details with:
            | field      | value           |
            | firstName  | Test            |
            | lastName   | User            |
            | address    | 123 Main St     |
            | state      | California      |
            | postalCode | 90210           |
        And I submit the order
        Then I should see order confirmation
        And the order number should be displayed

    Scenario: Bug verification - Galaxy S20 Ultra cart issue
        When I scroll to product "Galaxy S20 Ultra"
        And I add the product to cart
        Then the cart should remain empty
        # This verifies the reported bug

    Scenario: Bug verification - Download receipt failure
        When I scroll to product "iPhone 11 Pro"
        And I add the product to cart
        And I proceed to checkout
        And I fill shipping details
        And I submit the order
        And I click download receipt
        Then the download should fail
        # This verifies the reported bug