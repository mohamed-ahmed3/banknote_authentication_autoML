# banknote_authentication_autoML
It is an automated ML project on the banknote_authentication dataset to predict the probability of the positive class.
We are using tpot to choose the best model on our data. Then, we calibrate the model using Isotonic regression function.
The choice of the function used to calibrate the model is done using the brier_score_loss function. (See the notebook).
We also deployed this ML model using Django. A post request will be sent with a datapoint to predict the probability of the 
positive class. The return message of the request will contain the output of the probability. 

## Guide to test the project:
1. Clone the project to your directory
2. Open the CMD or powershell in this directory
3. Open the WSL terminal
4. Write the following command: docker compose up
5. Open postman and add a new post request
6. The url for the post request is: http://localhost:8087/banknote_authentication_api/datasets/prediction
7. Write your request body as json
8. Send the request

### Important Note!
If after executing the docker compose up command, an error occured: entrypoint.sh: no such file or directory, please
follow the following steps:

1. Delete the entrypoint.sh file
2. Create a new file named: entrypoint.sh
3. Open this file in any text editor
4. Write the following in the file:
   
  #!/bin/sh
  
  python manage.py makemigrations
  
  python manage.py migrate
  
  python manage.py runserver 0.0.0.0:8087
  

5. Save the file and run the docker compose up command again
