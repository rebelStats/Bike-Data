# Analysis of New York City Public Bike Rental Data



## Summary
Data describes rides taken on public bike rentals all over New York City. Data was uploaded to kaggle and can be found [here](https://www.kaggle.com/datasets/daesunryu/public-dataset-from-bikesharecompany). The original dataset contains many features about the rides, but does not contain any information about the riders. We might be able to infer information about the riders using the original feautures such as starting and ending locations, but that is beyong the scope of this project. After processing the data and creating the necessary features as well as doing preliminary exploratory analysis, we attempted to create statistical models to see if we can predict the distance of a ride from our available features. The best overall model was created with a Random Forrest that was tuned using randomized grid search. The model was deployed to [Streamlit](https://rebelstats-bike-data-streamlitbike-app-of2ukx.streamlitapp.com/) where users can input features and the model will return a predicted distance.

## Preprocessing and Feature Engineering
The original data set contained several variables that needed to be processed for it to be interpretable. This included the date and time as well as measuring the distance between the start and end points. We also created several other variables such as the time of day the ride took place, if the ride took place with a friend, and if the ride took place during the weekend or weekday. The data also contained many observations that might have been created by an error or the riders did not use the bikes as intended. These observations had to be filtered out before we could proceed. 

## Modeling
In notebook 03 we try to fit a regression model to the data, but we had trouble with meeting the assumptions of a regression model that would make it valid. Instead of trying other regression models, we thought it would be a better fit to implement more modern modeles. In the baseline regression model, we saw that we had unequal variance in the residuals where the residuals were much close to 0 for shorter ride lengths than for longer ride lengths. This was a good indicatior that model that can split these apart such as a tree based model or a neural network would perform well. We decided to implement Random Forrest, XGBoost, and a simple Neural Network using Pytorch to create a predictive model. 

## Results and Deployment
The results from these models confirmed our assumptions. The Random Forrest algorithm performed the best, presumably because it could seperate the short rides from the longer rides. While the boosting algorithm had similar issues to our baseline regression model. We choose to use the random forrest model to implement in an online app which was published to Streamlit. 

## Notebooks
Notebooks 01 and 02 contain the code for preprocessing and feature engineering. In these notebooks, we explore the data and look for trends as well as get it ready for modeling. We also introduce new features in the data such as if a ride was done with a friend and the ride length. In notebooks 03,04,and 05 we implement a variety of models to try to predict the ride length.
