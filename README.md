# waldo
Application that finds articles and relevant tweets

Documentation available [here](http://docs.waldo2.apiary.io/#)

---
## Bottle Necks
 - Api Call limitations
    - Creating user authorization layer would allow more calls
 - Server performance
    - Would the server be able to handle all the request
 - Api endpoints
    - If either of the providers decide to eliminate ep's or change them. The application would have to quickly adapt

### Releases
---
Version 0.5.0 provided usable api. Returning data from both twitter and wikipedia.

Version 1 the ux experience has been added to the application

---

## Running the application
Running the application requires nodejs & python

To run the application install api requirements

`
pip install -Ur requirements.txt
`

Then start the application

`
python run api/run.py
`

To run the user interface first install node. After installing node run these commands

`
    npm install
`

After installing the dependencies start the application

`
    gulp
`
