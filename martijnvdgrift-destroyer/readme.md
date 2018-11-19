#Martijn's Battleship

Technology of chose:
- Google Cloud Platform
- App Engine
- Standard environment
- Python 3.7 Runtime

I chose Google App Engine (GAE) because it offers a very easy solution to deploy (almost) any kind of application in a production grade environment.
GAE applications are auto scaled by default, support CI/CD via the gcloud sdk and even provides an HTTPS endpoint, while also offering scale to zero.

This battleship has an REST API with the following endpoints:

GET / : Alive probe endpoint
GET, POST /shoot : Shoot to a target url
POST /hit : Hit endpoint for the opponent.   


 
 
 
 