# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BatchJobDefinition(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'batch_data_type': 'str',
        'batch_interval': 'float',
        'batch_method': 'str',
        'batch_payload_type': 'str',
        'batch_retries': 'int',
        'batch_size': 'int',
        'batch_transport_protocol': 'str',
        'batch_workers': 'int',
        'input_data': 'str',
        'object_store_secret_name': 'str',
        'output_data': 'str',
        'pvc_size': 'str'
    }

    attribute_map = {
        'batch_data_type': 'batchDataType',
        'batch_interval': 'batchInterval',
        'batch_method': 'batchMethod',
        'batch_payload_type': 'batchPayloadType',
        'batch_retries': 'batchRetries',
        'batch_size': 'batchSize',
        'batch_transport_protocol': 'batchTransportProtocol',
        'batch_workers': 'batchWorkers',
        'input_data': 'inputData',
        'object_store_secret_name': 'objectStoreSecretName',
        'output_data': 'outputData',
        'pvc_size': 'pvcSize'
    }

    def __init__(self, batch_data_type=None, batch_interval=None, batch_method=None, batch_payload_type=None, batch_retries=None, batch_size=None, batch_transport_protocol=None, batch_workers=None, input_data=None, object_store_secret_name=None, output_data=None, pvc_size=None):  # noqa: E501
        """BatchJobDefinition - a model defined in Swagger"""  # noqa: E501

        self._batch_data_type = None
        self._batch_interval = None
        self._batch_method = None
        self._batch_payload_type = None
        self._batch_retries = None
        self._batch_size = None
        self._batch_transport_protocol = None
        self._batch_workers = None
        self._input_data = None
        self._object_store_secret_name = None
        self._output_data = None
        self._pvc_size = None
        self.discriminator = None

        if batch_data_type is not None:
            self.batch_data_type = batch_data_type
        if batch_interval is not None:
            self.batch_interval = batch_interval
        if batch_method is not None:
            self.batch_method = batch_method
        if batch_payload_type is not None:
            self.batch_payload_type = batch_payload_type
        if batch_retries is not None:
            self.batch_retries = batch_retries
        if batch_size is not None:
            self.batch_size = batch_size
        if batch_transport_protocol is not None:
            self.batch_transport_protocol = batch_transport_protocol
        if batch_workers is not None:
            self.batch_workers = batch_workers
        if input_data is not None:
            self.input_data = input_data
        if object_store_secret_name is not None:
            self.object_store_secret_name = object_store_secret_name
        if output_data is not None:
            self.output_data = output_data
        if pvc_size is not None:
            self.pvc_size = pvc_size

    @property
    def batch_data_type(self):
        """Gets the batch_data_type of this BatchJobDefinition.  # noqa: E501

        Batch Data Type (data, json or str)  # noqa: E501

        :return: The batch_data_type of this BatchJobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._batch_data_type

    @batch_data_type.setter
    def batch_data_type(self, batch_data_type):
        """Sets the batch_data_type of this BatchJobDefinition.

        Batch Data Type (data, json or str)  # noqa: E501

        :param batch_data_type: The batch_data_type of this BatchJobDefinition.  # noqa: E501
        :type: str
        """

        self._batch_data_type = batch_data_type

    @property
    def batch_interval(self):
        """Gets the batch_interval of this BatchJobDefinition.  # noqa: E501

        Interval between batches  # noqa: E501

        :return: The batch_interval of this BatchJobDefinition.  # noqa: E501
        :rtype: float
        """
        return self._batch_interval

    @batch_interval.setter
    def batch_interval(self, batch_interval):
        """Sets the batch_interval of this BatchJobDefinition.

        Interval between batches  # noqa: E501

        :param batch_interval: The batch_interval of this BatchJobDefinition.  # noqa: E501
        :type: float
        """

        self._batch_interval = batch_interval

    @property
    def batch_method(self):
        """Gets the batch_method of this BatchJobDefinition.  # noqa: E501

        Batch Method (predict)  # noqa: E501

        :return: The batch_method of this BatchJobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._batch_method

    @batch_method.setter
    def batch_method(self, batch_method):
        """Sets the batch_method of this BatchJobDefinition.

        Batch Method (predict)  # noqa: E501

        :param batch_method: The batch_method of this BatchJobDefinition.  # noqa: E501
        :type: str
        """

        self._batch_method = batch_method

    @property
    def batch_payload_type(self):
        """Gets the batch_payload_type of this BatchJobDefinition.  # noqa: E501

        Batch Payload Type (ndarray, tensor, tftensor, v2raw, v2binary - only if DataType=data)  # noqa: E501

        :return: The batch_payload_type of this BatchJobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._batch_payload_type

    @batch_payload_type.setter
    def batch_payload_type(self, batch_payload_type):
        """Sets the batch_payload_type of this BatchJobDefinition.

        Batch Payload Type (ndarray, tensor, tftensor, v2raw, v2binary - only if DataType=data)  # noqa: E501

        :param batch_payload_type: The batch_payload_type of this BatchJobDefinition.  # noqa: E501
        :type: str
        """

        self._batch_payload_type = batch_payload_type

    @property
    def batch_retries(self):
        """Gets the batch_retries of this BatchJobDefinition.  # noqa: E501

        Number of retries for each instance  # noqa: E501

        :return: The batch_retries of this BatchJobDefinition.  # noqa: E501
        :rtype: int
        """
        return self._batch_retries

    @batch_retries.setter
    def batch_retries(self, batch_retries):
        """Sets the batch_retries of this BatchJobDefinition.

        Number of retries for each instance  # noqa: E501

        :param batch_retries: The batch_retries of this BatchJobDefinition.  # noqa: E501
        :type: int
        """

        self._batch_retries = batch_retries

    @property
    def batch_size(self):
        """Gets the batch_size of this BatchJobDefinition.  # noqa: E501

        Size of the batch (number of predictions per request)  # noqa: E501

        :return: The batch_size of this BatchJobDefinition.  # noqa: E501
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this BatchJobDefinition.

        Size of the batch (number of predictions per request)  # noqa: E501

        :param batch_size: The batch_size of this BatchJobDefinition.  # noqa: E501
        :type: int
        """

        self._batch_size = batch_size

    @property
    def batch_transport_protocol(self):
        """Gets the batch_transport_protocol of this BatchJobDefinition.  # noqa: E501

        Batch Transport Protocol (rest or grpc)  # noqa: E501

        :return: The batch_transport_protocol of this BatchJobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._batch_transport_protocol

    @batch_transport_protocol.setter
    def batch_transport_protocol(self, batch_transport_protocol):
        """Sets the batch_transport_protocol of this BatchJobDefinition.

        Batch Transport Protocol (rest or grpc)  # noqa: E501

        :param batch_transport_protocol: The batch_transport_protocol of this BatchJobDefinition.  # noqa: E501
        :type: str
        """

        self._batch_transport_protocol = batch_transport_protocol

    @property
    def batch_workers(self):
        """Gets the batch_workers of this BatchJobDefinition.  # noqa: E501

        Number of batch workers  # noqa: E501

        :return: The batch_workers of this BatchJobDefinition.  # noqa: E501
        :rtype: int
        """
        return self._batch_workers

    @batch_workers.setter
    def batch_workers(self, batch_workers):
        """Sets the batch_workers of this BatchJobDefinition.

        Number of batch workers  # noqa: E501

        :param batch_workers: The batch_workers of this BatchJobDefinition.  # noqa: E501
        :type: int
        """

        self._batch_workers = batch_workers

    @property
    def input_data(self):
        """Gets the input_data of this BatchJobDefinition.  # noqa: E501

        S3 URI of input data file  # noqa: E501

        :return: The input_data of this BatchJobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._input_data

    @input_data.setter
    def input_data(self, input_data):
        """Sets the input_data of this BatchJobDefinition.

        S3 URI of input data file  # noqa: E501

        :param input_data: The input_data of this BatchJobDefinition.  # noqa: E501
        :type: str
        """

        self._input_data = input_data

    @property
    def object_store_secret_name(self):
        """Gets the object_store_secret_name of this BatchJobDefinition.  # noqa: E501

        name of Kubernetes Secret with S3 credentials  # noqa: E501

        :return: The object_store_secret_name of this BatchJobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._object_store_secret_name

    @object_store_secret_name.setter
    def object_store_secret_name(self, object_store_secret_name):
        """Sets the object_store_secret_name of this BatchJobDefinition.

        name of Kubernetes Secret with S3 credentials  # noqa: E501

        :param object_store_secret_name: The object_store_secret_name of this BatchJobDefinition.  # noqa: E501
        :type: str
        """

        self._object_store_secret_name = object_store_secret_name

    @property
    def output_data(self):
        """Gets the output_data of this BatchJobDefinition.  # noqa: E501

        S3 URI of output data file  # noqa: E501

        :return: The output_data of this BatchJobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._output_data

    @output_data.setter
    def output_data(self, output_data):
        """Sets the output_data of this BatchJobDefinition.

        S3 URI of output data file  # noqa: E501

        :param output_data: The output_data of this BatchJobDefinition.  # noqa: E501
        :type: str
        """

        self._output_data = output_data

    @property
    def pvc_size(self):
        """Gets the pvc_size of this BatchJobDefinition.  # noqa: E501

        Size of PVC required for the batch job  # noqa: E501

        :return: The pvc_size of this BatchJobDefinition.  # noqa: E501
        :rtype: str
        """
        return self._pvc_size

    @pvc_size.setter
    def pvc_size(self, pvc_size):
        """Sets the pvc_size of this BatchJobDefinition.

        Size of PVC required for the batch job  # noqa: E501

        :param pvc_size: The pvc_size of this BatchJobDefinition.  # noqa: E501
        :type: str
        """

        self._pvc_size = pvc_size

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BatchJobDefinition, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchJobDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
