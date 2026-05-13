terraform {
  required_version = ">= 1.0"
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "grc_findings_bucket" {
  bucket = "ai-aws-grc-findings-bucket"
}

resource "aws_dynamodb_table" "grc_findings_table" {
  name         = "grc-findings"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "finding_id"

  attribute {
    name = "finding_id"
    type = "S"
  }
}
