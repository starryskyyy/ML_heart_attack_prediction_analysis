# Machine Learning: Heart Attack Prediction Analysis
## Hands-on heart attack prediction project
## What is Heart Attack?

The medical name of heart attack: "Myocardial infarction"

A heart attack occurs when blood flow to a section of the heart becomes blocked and the heart muscle can’t get oxygen. If the blood flow isn’t restored quickly, that section of the heart begins to die. Depending on how long the blood supply is cut off, the damage can be mild, severe or cause lifelong problems. In some cases a heart attack can be fatal.
(https://www.heartandstroke.ca/heart-disease/conditions/heart-attack)

![heart img](https://snipboard.io/Z285rt.jpg)

## Symptoms

![symptoms](https://snipboard.io/Vxj2XQ.jpg)

## Required Python Libraries

- numpy (linear algebra)
- pandas (data processing, CSV file I/O (e.g. pd.read_csv)
- warnings (warnings.filterwarnings("ignore")
- matplotlib.pyplot
- seaborn

## Recognizing Variables In Dataset

### Variable definitions in the Dataset

- Age: Age of the patient
- Sex: Sex of the patient
- exang: exercise induced angina (1 = yes; 0 = no)
- ca: number of major vessels (0-3)
- cp: Chest Pain type chest pain type
- Value 1: typical angina
- Value 2: atypical angina
- Value 3: non-anginal pain
- Value 4: asymptomatic
- trtbps: resting blood pressure (in mm Hg)
- chol: cholestoral in mg/dl fetched via BMI sensor
- fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
- _restecg: resting electrocardiographic results
- Value 0: normal
- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
- thalach: maximum heart rate achieved
- target: 0= less chance of heart attack 1= more chance of heart attack

### Additional variable descriptions to help us

- age - age in years

- sex - sex (1 = male; 0 = female)

- cp - chest pain type (1 = typical angina; 2 = atypical angina; 3 = non-anginal pain; 0 = asymptomatic)

- trestbps - resting blood pressure (in mm Hg on admission to the hospital)

- chol - serum cholestoral in mg/dl

- fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)

- restecg - resting electrocardiographic results (1 = normal; 2 = having ST-T wave abnormality; 0 = hypertrophy)

- thalach - maximum heart rate achieved

- exang - exercise induced angina (1 = yes; 0 = no)

- oldpeak - ST depression induced by exercise relative to rest

- slope - the slope of the peak exercise ST segment (2 = upsloping; 1 = flat; 0 = downsloping)

- ca - number of major vessels (0-3) colored by flourosopy

- thal - 2 = normal; 1 = fixed defect; 3 = reversable defect

- num - the predicted attribute - diagnosis of heart disease (angiographic disease status) (Value 0 = < diameter narrowing; Value 1 = > 50% diameter narrowing)

### Note: You can find these varaiables definitions in the discussion section of the "Heart attack analysis and prediction" dataset.

## Authors

- [@starryskyyy](https://github.com/starryskyyy) :sparkling_heart:


