#!/usr/bin/env python
from aws.boto_connections import AWSBotoAdapter
from botocore.exceptions import ClientError


class Cloudformation(object):
    RESOURCE = "cloudformation"

    def __init__(self, profile, name):
        self.__profile = profile
        self.__connection = AWSBotoAdapter()
        self.__name = name
        self.__stackName = self.__name

    def get_stackName(self):
        return self.__stackName

    def get_connection_cloudformation(self):
        conn = self.__connection.get_client(Cloudformation.RESOURCE, self.__profile)
        return conn

    def exist_cloud_formation(self, cf):
        try:
            stack_summaries = bool(cf.describe_stacks(StackName=self.__stackName))
        except  ClientError as error:
            print (error.response['Error']['Message'])
            exit(1)
        return stack_summaries
