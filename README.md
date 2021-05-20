## Behaviour Driven Tests for Gmail's "compose email" feature

|  Priority  |  Description  |  Steps  |  Expected result  |
|---|---|---|---|
|  P0  |  Verify that user can fill "To", "Subject", "Body" and send an email and the email is sent successfully  |  <ol><li>Open Gmail and login</li><li>Click on "Compose"</li><li>Enter valid values for ""To"", "Subject" and "Body"</li><li>Click on "Send"</li></ol>  | "Your message has been sent." message is displayed  |
|  P0  | Verify that appropriate error is displayed when "To" is invalid  |  <ol><li>Open Gmail and login</li><li>Click on "Compose"</li><li>Enter valid values for "Subject" and "Body" and invalid value for "To"</li><li>Click on "Send"</li></ol>  |  "....Please make sure that all addresses are properly formed" message is displayed  |

### How to run
1. Create a `.env` file containing: `EMAIL` and `PASSWORD`
2. Run `pip install -r requirements.txt` to install dependencies
3. Run `behave` to execute tests