# HolidayBot

HolidayBot is a chatbot that helps you book your holiday, be it a hotel or a car rental. 

![](https://github.com/jnganzh/chatbot-holiday/blob/main/demo.png)

## Amazon Lex

Amazon Lex is Amazon's service for building conversational bots or "chatbots" and provides automatic speech recognition (ASR) for converting speech to text, and natural language understanding (NLU) to recognize the intent of the text. It also integrates seamlessly with other AWS services, including AWS CloudWatch, Cognito, and Lambda. This allows developers to built a more customized and effective chatbot that best fits their needs.

Our project uses Amazon Lex to build a chatbot that can help book hotels and cars for a trip. Test it out [here](https://dr5p7ego6gbjc.cloudfront.net/index.html)!

For a detailed, basic introduction to using Amazon Lex, see [Getting Started with Amazon Lex](https://docs.aws.amazon.com/lex/latest/dg/getting-started.html)

## Bot Structure

Amazon Lex allows you to input user **intents**. **Intents** are the actions that you want the user to respond to. In our case, we are simulating a travel website that is helping a user book a hotel or rent a car, so our intents walk the user through the location where the user is traveling to and how long they will need the room/rental for. An **utterance** invokes the intent, and in our case, an example utterance could be "Book a hotel." To help guide the user, **slots** are used to guide the user to what options are available. In our bot, the slots are either renting a car or booking a room.

## Deploying the Chatbot

There are a couple of options to deploy the chatbot. You can launch it on a few messeging apps such as Facebook, Slack and Twillo. However, we launched it on an independent page with AWS CloudFormation.



## Load Testing

To load test the website, [locust.io](https://locust.io) was used to simulate 1000 simultaneous users at a time accessing the chatbot, with up to 10,000 users total. Documentation of how to install and run locust can be found [here](https://docs.locust.io/en/stable/), but essentially after installing the package, one can use the CLI to launch the .py file then access the localhost through the web browser using the port http://127.0.0.1:8089 , leading to to a GUI that allows you to input the amount of users you want to simulate.

![](https://github.com/jnganzh/chatbot-holiday/blob/main/locust.png)

Load testing allows you to identify if your web design is optimal and if it can server a large number of users.

### Results of Load Testing


![](https://github.com/jnganzh/chatbot-holiday/blob/main/locustio_loadtest.PNG)
