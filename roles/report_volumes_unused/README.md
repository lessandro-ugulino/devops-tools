# Tool: Report all volumes unused

## Index

- [Summary](#summary)
- [Diagram](#diagram)
- [Requirements](#requirements)
- [Possible modifications](#possible-modifications)

## Summary

Report all volumes unused (not attached) and send an email via SNS.

## Diagram

![lambda-diagram](/imgs/unused_vol_lambda.png)

## Requirements

Set your email up on the file `lambda_report_volumes_unused.yml.j2` line `72`

## Possible modifications

This function is designed to send an email based on AEST time zone. You can change it on the file `lambda_report_volumes_unused.yml.j2` before deploying it, line `126` .
