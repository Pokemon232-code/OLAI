#!/usr/bin/env python3
"""
AWS Integration Module
Integrates with Amazon Web Services (S3, EC2, Lambda, RDS, etc.)
"""

import boto3
import os
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class AWSIntegration:
    """Amazon Web Services integration"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.region = self.config.get("region", "us-east-1")
        self.access_key = self.config.get("access_key") or os.getenv("AWS_ACCESS_KEY_ID")
        self.secret_key = self.config.get("secret_key") or os.getenv("AWS_SECRET_ACCESS_KEY")
        
        # Initialize AWS clients
        self.s3_client = None
        self.ec2_client = None
        self.lambda_client = None
        self.rds_client = None
        self.cloudfront_client = None
        self.ses_client = None
        self.sns_client = None
        
        self._initialize_clients()
    
    def _initialize_clients(self):
        """Initialize AWS service clients"""
        try:
            session = boto3.Session(
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
                region_name=self.region
            )
            
            self.s3_client = session.client('s3')
            self.ec2_client = session.client('ec2')
            self.lambda_client = session.client('lambda')
            self.rds_client = session.client('rds')
            self.cloudfront_client = session.client('cloudfront')
            self.ses_client = session.client('ses')
            self.sns_client = session.client('sns')
            
            logger.info("AWS clients initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize AWS clients: {e}")
    
    def create_s3_bucket(self, bucket_name: str, region: str = None) -> Dict[str, Any]:
        """Create an S3 bucket"""
        try:
            if not region:
                region = self.region
            
            if region == 'us-east-1':
                # us-east-1 doesn't need LocationConstraint
                self.s3_client.create_bucket(Bucket=bucket_name)
            else:
                self.s3_client.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': region}
                )
            
            return {
                "status": "success",
                "bucket_name": bucket_name,
                "region": region,
                "message": "S3 bucket created successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"S3 bucket creation failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def upload_to_s3(self, bucket_name: str, key: str, file_path: str, content_type: str = None) -> Dict[str, Any]:
        """Upload a file to S3"""
        try:
            extra_args = {}
            if content_type:
                extra_args['ContentType'] = content_type
            
            self.s3_client.upload_file(file_path, bucket_name, key, ExtraArgs=extra_args)
            
            # Generate presigned URL
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket_name, 'Key': key},
                ExpiresIn=3600
            )
            
            return {
                "status": "success",
                "bucket_name": bucket_name,
                "key": key,
                "presigned_url": url,
                "message": "File uploaded successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"S3 upload failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_ec2_instance(self, image_id: str, instance_type: str = "t2.micro", 
                          key_name: str = None, security_group_ids: List[str] = None) -> Dict[str, Any]:
        """Create an EC2 instance"""
        try:
            instance_config = {
                "ImageId": image_id,
                "MinCount": 1,
                "MaxCount": 1,
                "InstanceType": instance_type
            }
            
            if key_name:
                instance_config["KeyName"] = key_name
            
            if security_group_ids:
                instance_config["SecurityGroupIds"] = security_group_ids
            
            response = self.ec2_client.run_instances(**instance_config)
            
            instance = response['Instances'][0]
            
            return {
                "status": "success",
                "instance_id": instance['InstanceId'],
                "instance_type": instance['InstanceType'],
                "state": instance['State']['Name'],
                "public_ip": instance.get('PublicIpAddress'),
                "message": "EC2 instance created successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"EC2 instance creation failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def deploy_lambda_function(self, function_name: str, zip_file_path: str, 
                             handler: str = "lambda_function.lambda_handler", 
                             runtime: str = "python3.9", role_arn: str = None) -> Dict[str, Any]:
        """Deploy a Lambda function"""
        try:
            with open(zip_file_path, 'rb') as zip_file:
                zip_content = zip_file.read()
            
            function_config = {
                "FunctionName": function_name,
                "Runtime": runtime,
                "Role": role_arn,
                "Handler": handler,
                "Code": {"ZipFile": zip_content}
            }
            
            try:
                # Try to create new function
                response = self.lambda_client.create_function(**function_config)
            except self.lambda_client.exceptions.ResourceConflictException:
                # Function already exists, update it
                response = self.lambda_client.update_function_code(
                    FunctionName=function_name,
                    ZipFile=zip_content
                )
            
            return {
                "status": "success",
                "function_name": response['FunctionName'],
                "function_arn": response['FunctionArn'],
                "runtime": response['Runtime'],
                "handler": response['Handler'],
                "message": "Lambda function deployed successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Lambda function deployment failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_rds_instance(self, db_instance_identifier: str, db_name: str, 
                          master_username: str, master_password: str,
                          db_instance_class: str = "db.t3.micro",
                          engine: str = "mysql", allocated_storage: int = 20) -> Dict[str, Any]:
        """Create an RDS database instance"""
        try:
            response = self.rds_client.create_db_instance(
                DBInstanceIdentifier=db_instance_identifier,
                DBName=db_name,
                MasterUsername=master_username,
                MasterUserPassword=master_password,
                DBInstanceClass=db_instance_class,
                Engine=engine,
                AllocatedStorage=allocated_storage,
                BackupRetentionPeriod=7,
                MultiAZ=False,
                PubliclyAccessible=False
            )
            
            db_instance = response['DBInstance']
            
            return {
                "status": "success",
                "db_instance_identifier": db_instance['DBInstanceIdentifier'],
                "db_name": db_instance['DBName'],
                "engine": db_instance['Engine'],
                "db_instance_class": db_instance['DBInstanceClass'],
                "endpoint": db_instance.get('Endpoint', {}).get('Address'),
                "port": db_instance.get('Endpoint', {}).get('Port'),
                "message": "RDS instance created successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"RDS instance creation failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def send_email(self, to_addresses: List[str], subject: str, body: str, 
                  from_address: str = None) -> Dict[str, Any]:
        """Send email using SES"""
        try:
            if not from_address:
                from_address = self.config.get("from_address")
            
            response = self.ses_client.send_email(
                Source=from_address,
                Destination={'ToAddresses': to_addresses},
                Message={
                    'Subject': {'Data': subject},
                    'Body': {'Text': {'Data': body}}
                }
            )
            
            return {
                "status": "success",
                "message_id": response['MessageId'],
                "to_addresses": to_addresses,
                "subject": subject,
                "message": "Email sent successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"SES email sending failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def publish_sns_message(self, topic_arn: str, message: str, subject: str = None) -> Dict[str, Any]:
        """Publish a message to SNS topic"""
        try:
            message_params = {"Message": message}
            if subject:
                message_params["Subject"] = subject
            
            response = self.sns_client.publish(TopicArn=topic_arn, **message_params)
            
            return {
                "status": "success",
                "message_id": response['MessageId'],
                "topic_arn": topic_arn,
                "message": "SNS message published successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"SNS message publishing failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_cloudfront_distribution(self, origin_domain: str, comment: str = None) -> Dict[str, Any]:
        """Create a CloudFront distribution"""
        try:
            distribution_config = {
                "CallerReference": f"olai-distribution-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                "Origins": {
                    "Quantity": 1,
                    "Items": [
                        {
                            "Id": "origin1",
                            "DomainName": origin_domain,
                            "CustomOriginConfig": {
                                "HTTPPort": 80,
                                "HTTPSPort": 443,
                                "OriginProtocolPolicy": "https-only"
                            }
                        }
                    ]
                },
                "DefaultCacheBehavior": {
                    "TargetOriginId": "origin1",
                    "ViewerProtocolPolicy": "redirect-to-https",
                    "TrustedSigners": {
                        "Enabled": False,
                        "Quantity": 0
                    },
                    "ForwardedValues": {
                        "QueryString": False,
                        "Cookies": {"Forward": "none"}
                    }
                },
                "Enabled": True,
                "Comment": comment or "OLAI CloudFront Distribution"
            }
            
            response = self.cloudfront_client.create_distribution(
                DistributionConfig=distribution_config
            )
            
            distribution = response['Distribution']
            
            return {
                "status": "success",
                "distribution_id": distribution['Id'],
                "domain_name": distribution['DomainName'],
                "status": distribution['Status'],
                "message": "CloudFront distribution created successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"CloudFront distribution creation failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_service_status(self) -> Dict[str, Any]:
        """Get the status of all AWS services"""
        try:
            status = {
                "s3": "available" if self.s3_client else "unavailable",
                "ec2": "available" if self.ec2_client else "unavailable",
                "lambda": "available" if self.lambda_client else "unavailable",
                "rds": "available" if self.rds_client else "unavailable",
                "cloudfront": "available" if self.cloudfront_client else "unavailable",
                "ses": "available" if self.ses_client else "unavailable",
                "sns": "available" if self.sns_client else "unavailable"
            }
            
            return {
                "status": "success",
                "aws_services": status,
                "region": self.region,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"AWS service status check failed: {e}")
            return {"status": "error", "error": str(e)}

# Factory function
def create_aws_integration(config: Dict[str, Any] = None) -> AWSIntegration:
    """Create an AWS integration instance"""
    return AWSIntegration(config)

# Example usage
if __name__ == "__main__":
    # Example configuration
    config = {
        "region": "us-east-1",
        "access_key": "your_aws_access_key",
        "secret_key": "your_aws_secret_key",
        "from_address": "noreply@yourdomain.com"
    }
    
    aws = create_aws_integration(config)
    
    # Test service status
    status = aws.get_service_status()
    print(f"AWS service status: {status}")
    
    # Test creating S3 bucket
    bucket_result = aws.create_s3_bucket("olai-test-bucket")
    print(f"S3 bucket result: {bucket_result}")
