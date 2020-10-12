1. Title: CS443 boto3test
2. Purpose: Research and testing was done to create buckets/files and send them to S3. Afterwards, we connect to a live EC2 server and manually download the given files.
3. Written by: Cameron Davis
4. Sources:
RealPython Boto3 to S3 Tutorial https://realpython.com/python-boto3-aws-s3/#:~:text=Boto3%20is%20the%20name%20of,resources%20from%20your%20Python%20scripts.:
	~ Code here was adopted and tested using my account
5. Instructions:
    1) Create a folder called ".aws" in the root folder of your user (Ex. Cameron Davis/.aws). Then create two generric Files named "config" and "credentials"
		1.1) config file should look like this:
		*- [default]          -*
		*- region =			  -*
		*- output = 		  -*
		1.2) credentials file should look like this:
		*- [default]               -*
		*- aws_access_key_id =     -*
		*- aws_secret_access_key = -*
		1.3) Fill out the information for both files before running boto3test.py. Region can be found here https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions . Output can be left blank. AWS Keys are located in your user Security Credentials - there you will find Access Keys. After editing make sure to save both files.
    2) Run boto3test.py and go to your S3 buckets - there should be two new buckets, and in the first there should be a new test file. This confirms that the program has worked. Also be sure to make the file uploaded public before attempting the next step; simply select in then click "Make public." The Object URL at the bottom is what we'll be using for the EC2 instance.
	3) Afterwards begin a EC2 instance - connect using either a SSH Client or and EC2 Instance Connect. Full details on how to connect using PuTTy can be referenced here: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html
	4) Once in your client do "wget [Object URL]" and wait for the download. Use "ls" to confirm the file has been downloaded properly.
	5) Once you are satisfied, TERMINATE your EC2 instance. Empty the first bucket in S3, then delete both buckets. 
6. Thoughts and Commentary:
    ~ Thankfully the tutorial shared in Resources was very useful in getting the Boto3 connected to S3, and then from there you need knowledge of connecting to EC2 and the "wget" command to download the file. Though this is a small piece of the final project the transfer of files from local storage to S3 and S3 to EC2 is fundamental and cannot be overlooked. This code will likely be built upon and integrated in the user agent. 
7. Contact: camrhys@uab.edu