# Tool: Start and Stop EC2 with a specific tag

## Index

- [Summary](#summary)
- [Diagram](#diagram)
- [Requirements](#requirements)
- [Possible modifications](#possible-modifications)

## Summary

Start all EC2 instances with specific tag (Key:daily_scheduled Value:True) everyday in morning and stop it everyday in evening using lambda function with Python 3.9

## Diagram

![lambda-diagram](/imgs/start_stop_lambda.png)

## Requirements

Tag all EC2 with the tag `Key:daily_scheduled Value:True` that will be started and stopped using these lambdas function.

## Possible modifications

These functions are designed to start and stop the instances based on AEST time zone. You can change it on the file `lambda_ec2_scheduled.yml.j2` before deploying it, lines `82` and `138`.
