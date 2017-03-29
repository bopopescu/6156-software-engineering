"""Generated client library for vision version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.vision.v1 import vision_v1_messages as messages


class VisionV1(base_api.BaseApiClient):
  """Generated client library for service vision version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://vision.googleapis.com/'

  _PACKAGE = u'vision'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'VisionV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new vision handle."""
    url = url or self.BASE_URL
    super(VisionV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.images = self.ImagesService(self)

  class ImagesService(base_api.BaseApiService):
    """Service class for the images resource."""

    _NAME = u'images'

    def __init__(self, client):
      super(VisionV1.ImagesService, self).__init__(client)
      self._upload_configs = {
          }

    def Annotate(self, request, global_params=None):
      """Run image detection and annotation for a batch of images.

      Args:
        request: (BatchAnnotateImagesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchAnnotateImagesResponse) The response message.
      """
      config = self.GetMethodConfig('Annotate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Annotate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'vision.images.annotate',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1/images:annotate',
        request_field='<request>',
        request_type_name=u'BatchAnnotateImagesRequest',
        response_type_name=u'BatchAnnotateImagesResponse',
        supports_download=False,
    )
