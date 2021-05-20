Feature: Compose

  @signin
  Scenario: User can enter TO, SUBJECT, BODY and send email successfully
    Given user enters To:"bddassessment1@gmail.com", Subject:"Incubyte" and Body:"Automation QA test for Incubyte"
    When user clicks on send
    Then email is sent successfully

  @signin
  Scenario: Appropriate error is displayed when TO is invalid
    Given user enters To:"bdd", Subject:"BDD Framework" and Body:"This is automated message"
    When user clicks on send
    Then error "The address "bdd" in the "To" field was not recognized. Please make sure that all addresses are properly formed." is displayed



