# connect_demo

- Heres a simple demo for amazon connect of a spoof State Government call center.
- To create this experience only the following AWS Services were utilized 
  - Amazon Connect
  - Amazon Lex
  - Amazon Lambda
- The flow currently at this time doesn't route to queues nor any agents.
- A caller is prompted with their call reason at the end of the flow after navigating the lex (getUserInputs).
- There are two options in testing holiday observance (1) or in hours(2).
- To test (keep in mind maintaing free tier costs) you may call the following toll free number: (855) 577-8307.


- Time to build 
- All together 8 hours
- Time per service
  - Lambda - 4 hours
  - Lex 3 hours
  - Connect 1 hour