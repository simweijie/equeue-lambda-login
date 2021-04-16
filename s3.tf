terraform {
  backend "s3" {
    bucket = "nus-iss-equeue-terraform"
    key    = "lambda/login/tfstate"
    region = "us-east-1"
  }
}
