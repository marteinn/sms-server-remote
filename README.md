# SMS-Server-Remote
This is a experiment based on Twilio and [Serverless](http://serverless.com) that lets you trigger fabric tasks on your server through SMS.

## Getting started
- [Install serverless](: `npm install serverless -g`)
- Setup project on AWS (just follow the serverless instructions)
- Update dependencies: `make update_dependencies`
- Write your own fabfile and server handling, store it in `src/incoming/sms/config`
- Deploy the function and endpoint `incoming_sms`
- Create a Twilio TwiML app that handles SMS messaging, use your lambda endpoint as request url with HTTP GET

## Usage
- Send a SMS with your fabric command to your Twilio phone number (example: `prod restart_apache`)
- Sends back something like this:

    ```
    service apache restart
    restarting apache..
    restart complete!
    ```
- Please note that fabric taks that takes longer then 15 seconds are not sent back to Twilio (due to Twilio limitations)

## Endpoints: incoming_sms
The endpoint incoming_sms requires the following params:

- `Body` (SMS message body delivered from Twilio) 
- `From` (Phone number delivered from Twilio)
- `secret` (A simple auth token)

Example:

```
curl -X "GET" "https://XXXXX.execute-api.eu-west-1.amazonaws.com/stage/incoming_sms?Body=mp%20info&From=%2B46000000&secret=myscret"
```

Returns:

```
<Response>
  <Message>
    <Body><![CDATA[cat /etc/*-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=14.04
DISTRIB_CODENAME=trusty
DISTRIB_DESCRIPTION="Ubuntu 14.04.4 LTS"
NAME="Ubuntu"
VERSION="14.04.4 LTS, Trusty Tahr"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 14.04.4 LTS"
VERSION_ID="14.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"]]></Body>
  </Message>
</Response>
```

## Commands
- Deploy function: `npm run serverless function deploy -a`
- Deploy endpoint: `npm run serverless endpoint deploy -a`
- Deploy: `npm run serverless dash deploy`

## Dependencies
- https://github.com/Doerge/awslambda-pycrypto

### References
- http://docs.serverless.com/docs/templates-variables
- http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html

### Tutorials/Examples
- https://serverlesscode.com/post/python-on-serverless-intro/
- https://www.twilio.com/docs/quickstart/php/sms/hello-monkey
- https://github.com/mauerbac/lambda-gateway-twilio-demo/blob/master/lambda_function.py
- https://www.twilio.com/blog/2015/11/sending-selfies-without-servers-how-to-use-twilio-mms-amazon-lamba-and-amazons-gateway.html
