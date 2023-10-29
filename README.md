# Template project for pyspark application
This repository contains the core and most of the required dependencies to start a pyspark application using docker to test against both local instance of pyspark or cluster in Databricks.

# Step1: Dependencies
1. Install Docker for Desktop([https://docs.docker.com/desktop/install/windows-install/] or[https://docs.docker.com/desktop/install/mac-install/])
2. Install VSCode ([https://code.visualstudio.com/download])
3. Create Databricks resource

# Step2: Repo
1. Clone this project and open them in VSCode
2. Update `HOST_URL`  and `TOKEN` in the `Dockerfile`. You can get this info from the Azure. 
3. Rebuild container


# Note:
1. At this moment it support only `Databricks Personal access token (PAT)` only.
2. This repo tested with **Azure Cloud linked Databricks**. I would expect the same should work with other cloud providers too.
3. As of this checkin date, this repo use **databricks.databricks** extentions to integrate and run pyspark code against Azure Databricks - and this extension is in **preview**.


Congrats - You're all set!

Your contributions are most welcome!