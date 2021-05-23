# smarthelio Assignment 

Develop a web service, using resources on AWS, that accesses the database in real-time and provides excellent visualization of the time series analysis of Voltage, Current, and Power (Voltage * Current).

# Backend - Using Serverless REST APIs with PostgreSQL and offline support

## Built With

Technologies & plugins used to create this application
* [Python](https://www.python.org/)
* [Serverless](https://www.serverless.com/)
* [psycopg2](https://pypi.org/project/psycopg2/)

##### Serverless plugins

- [serverless-python-requirements](https://www.npmjs.com/package/serverless-python-requirements): A Serverless v1.x plugin to automatically bundle dependencies from requirements.txt and make them available in your PYTHONPATH.
- [serverless-offline](https://github.com/dherault/serverless-offline): This Serverless plugin emulates AWS λ and API Gateway on your local machine to speed up your development cycles.

## AWS Services

Currently, the application is built and tested on AWS using the following services.

- [AWS Lambda](https://aws.amazon.com/lambda/)

- AWS S3 [deployemt bucket](https://aws.amazon.com/s3/)

- AWS RDS [postgresql database server](https://aws.amazon.com/rds/)

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* [Python](https://www.python.org/): Setup python and pip
* Install the [serverless-cli](https://www.serverless.com/framework/docs/getting-started/)
  ```sh
  npm install -g serverless
  ```
* Create a postgresql server on [AWS RDS](https://aws.amazon.com/rds/)
* Create two [AWS S3](https://aws.amazon.com/s3/) buckets for deployment (For dev & QA)

## Installation

* Clone the repo
   ```sh
   git clone https://github.com/thisislucifer/smarthelio
   ```
* Install NPM packages
   ```sh
   npm install
   ```
* Update env.yml with environment variables
```
dev:
  ENV: "<environment name>"
  APP_NAME: "<app name>"
  RDS_ENDPOINT_STR: "<database rds string>"
  DEPLOYMENT_BUCKET: "<s3 bucket id for deployment>"
  ACCOUNT_ID: "<your AWS account ID>

qa:
  ENV: "<environment name>"
  APP_NAME: "<app name>"
  RDS_ENDPOINT_STR: "<database rds string>"
  DEPLOYMENT_BUCKET: "<s3 bucket id for deployment>"
  ACCOUNT_ID: "<your AWS account ID>

prod:
  ENV: "<environment name>"
  APP_NAME: "<app name>"
  RDS_ENDPOINT_STR: "<database rds string>"
  DEPLOYMENT_BUCKET: "<s3 bucket id for deployment>"
  ACCOUNT_ID: "<your AWS account ID>
```
## Usage
Test your service locally, without having to deploy it first.

```
serverless offline start
```
## Documentation
Please refer to the [Postman Documentation](https://www.getpostman.com/collections/1a71996fc1d5b553f19d)
## Deployment


##### 1. SetUP AWS Access Keys
To get started you can export the keys as environment variables so they would be accessible to Serverless and the AWS SDK in your shell:

```
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
# AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are now available for serverless to use

```
##### 2. Deploy to default region and stage

```
serverless deploy
# 'export' command is valid only for unix shells. In Windows - use 'set' instead of 'export'
```
##### 3. Specify region and stage (dev/ qa)

```
serverless deploy --stage <STAGE> --region <REGION>
```

# FrontEnd - Using simple HTML,CSS and Javascript

Technologies & plugins used to create this application
* [Chart.js](https://www.chartjs.org/)
* [Axios](https://www.npmjs.com/package/axios)

## Deployment and Hosting

Currently, the application is built and tested and deployed on AWS S3 service. 


- AWS S3 [Website Hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)

- Application Link [Click Here](http://smarthelio-app.s3-website.us-east-2.amazonaws.com/)


