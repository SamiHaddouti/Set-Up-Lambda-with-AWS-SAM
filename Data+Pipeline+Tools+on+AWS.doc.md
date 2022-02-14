# Data Pipeline Tools on AWS

## Guide for Migrating to AWS Lambda with AWS SAM framework:

We use the AWS SAM framework for the migration and set up of our tools
in AWS Lambda, as it offers:

  - development in IDE

  - local testing

  - packaging of dependencies with docker images

  - easy deployment/configuration of Lambda functions

### Requirements:

  - Python

  - AWS

  - SAM

  - Docker

<https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html>

#### 1\. Set up Lambda Function in SAM with package type Image

**sam init**

![Text Description automatically generated](media/image1.png)

Process for initializing SAM App

  - Quick start templates/app-template doesn’t have to be hello-world,
    but it is a good fundament

  - base-image should be chosen according to preferred runtime

  - name is up to you

#### **2. Adapt template.yaml**

Set timeout to 120 or more

![Text Description automatically generated](media/image2.png)

Also comment out everything involving the API from the hello world
app-template, as we don’t need that resource and it just produces AWS
cost

If wanted you can also change the Role/Policy to for example
S3ReadAccess, but that can also be adjusted in AWS after deployment.

#### **3. Import libraries**

Now let’s move on to adding the required dependencies

![A picture containing text Description automatically
generated](media/image3.png)

Add the packages (optional: specify version) in the requirements.txt

Import them then to the app.py or other python files, where you need
them

 

#### **4. Code**

To add helper functions or other python files, they also need to be
added to the dockerfile, so that they are copied into the image.

**Folder Structure:**

![Graphical user interface, application Description automatically
generated](media/image4.png)

**  Dockerfile:**

*COPY app.py **helper\_functions.py** requirements.txt ./*

Every file to be copied into the image

#### **5. Build Image**

*sam build*

builds Docker Image

 

#### **6. Test Locally**

 

*sam local invoke*

Runs Image and tests locally

 

#### **7. Deploy to AWS**

 

*sam deploy –guided*

Guided is optional, but recommended

Just follow the steps and select the right region for deployment
(eu-central-1)

 ![Text Description automatically generated](media/image5.png)

**Other great guides:**

<https://medium.com/platform-engineer/automating-lambda-container-image-deployments-with-aws-sam-cli-71afbf09e172>

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html

#### Errors:

"errorMessage": "Unable to import module 'app': No module named 'app'",
"errorType": "Runtime.ImportModuleError", "stackTrace"

  - often folder structure or import problems (check dockerfile, if
    every file is being copied and imports/requirements.txt)

  - potential other errors are python dependencies, that are differen in
    macOS/local environment and Linux environment (AWS Lambda)

  - also always check region, especially when deploying

 

### For the Future: 

S3 Event Trigger

<https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html>

**Next Steps after POC**

Step Functions for Orchestration of Lambda Functions:

<https://www.youtube.com/watch?v=KcoLDAhLpbg>
