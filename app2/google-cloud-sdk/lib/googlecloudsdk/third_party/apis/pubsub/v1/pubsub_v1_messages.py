"""Generated message classes for pubsub version v1.

Provides reliable, many-to-many, asynchronous messaging between applications.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'pubsub'


class AcknowledgeRequest(_messages.Message):
  """Request for the Acknowledge method.

  Fields:
    ackIds: The acknowledgment ID for the messages being acknowledged that was
      returned by the Pub/Sub system in the `Pull` response. Must not be
      empty.
  """

  ackIds = _messages.StringField(1, repeated=True)


class Binding(_messages.Message):
  """Associates `members` with a `role`.

  Fields:
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following values:  * `allUsers`: A
      special identifier that represents anyone who is    on the internet;
      with or without a Google account.  * `allAuthenticatedUsers`: A special
      identifier that represents anyone    who is authenticated with a Google
      account or a service account.  * `user:{emailid}`: An email address that
      represents a specific Google    account. For example, `alice@gmail.com`
      or `joe@example.com`.   * `serviceAccount:{emailid}`: An email address
      that represents a service    account. For example, `my-other-
      app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address
      that represents a Google group.    For example, `admins@example.com`.  *
      `domain:{domain}`: A Google Apps domain name that represents all the
      users of that domain. For example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`. Required
  """

  members = _messages.StringField(1, repeated=True)
  role = _messages.StringField(2)


class CreateSnapshotRequest(_messages.Message):
  """Request for the `CreateSnapshot` method.

  Fields:
    subscription: The subscription whose backlog the snapshot retains.
      Specifically, the created snapshot is guaranteed to retain:  (a) The
      existing backlog on the subscription. More precisely, this is
      defined as the messages in the subscription's backlog that are
      unacknowledged upon the successful completion of the
      `CreateSnapshot` request; as well as:  (b) Any messages published to the
      subscription's topic following the      successful completion of the
      CreateSnapshot request. Format is
      `projects/{project}/subscriptions/{sub}`.
  """

  subscription = _messages.StringField(1)


class Empty(_messages.Message):
  """A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class ListSnapshotsResponse(_messages.Message):
  """Response for the `ListSnapshots` method.

  Fields:
    nextPageToken: If not empty, indicates that there may be more snapshot
      that match the request; this value should be passed in a new
      `ListSnapshotsRequest`.
    snapshots: The resulting snapshots.
  """

  nextPageToken = _messages.StringField(1)
  snapshots = _messages.MessageField('Snapshot', 2, repeated=True)


class ListSubscriptionsResponse(_messages.Message):
  """Response for the `ListSubscriptions` method.

  Fields:
    nextPageToken: If not empty, indicates that there may be more
      subscriptions that match the request; this value should be passed in a
      new `ListSubscriptionsRequest` to get more subscriptions.
    subscriptions: The subscriptions that match the request.
  """

  nextPageToken = _messages.StringField(1)
  subscriptions = _messages.MessageField('Subscription', 2, repeated=True)


class ListTopicSubscriptionsResponse(_messages.Message):
  """Response for the `ListTopicSubscriptions` method.

  Fields:
    nextPageToken: If not empty, indicates that there may be more
      subscriptions that match the request; this value should be passed in a
      new `ListTopicSubscriptionsRequest` to get more subscriptions.
    subscriptions: The names of the subscriptions that match the request.
  """

  nextPageToken = _messages.StringField(1)
  subscriptions = _messages.StringField(2, repeated=True)


class ListTopicsResponse(_messages.Message):
  """Response for the `ListTopics` method.

  Fields:
    nextPageToken: If not empty, indicates that there may be more topics that
      match the request; this value should be passed in a new
      `ListTopicsRequest`.
    topics: The resulting topics.
  """

  nextPageToken = _messages.StringField(1)
  topics = _messages.MessageField('Topic', 2, repeated=True)


class ModifyAckDeadlineRequest(_messages.Message):
  """Request for the ModifyAckDeadline method.

  Fields:
    ackDeadlineSeconds: The new ack deadline with respect to the time this
      request was sent to the Pub/Sub system. For example, if the value is 10,
      the new ack deadline will expire 10 seconds after the
      `ModifyAckDeadline` call was made. Specifying zero may immediately make
      the message available for another pull request. The minimum deadline you
      can specify is 0 seconds. The maximum deadline you can specify is 600
      seconds (10 minutes).
    ackIds: List of acknowledgment IDs.
  """

  ackDeadlineSeconds = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  ackIds = _messages.StringField(2, repeated=True)


class ModifyPushConfigRequest(_messages.Message):
  """Request for the ModifyPushConfig method.

  Fields:
    pushConfig: The push configuration for future deliveries.  An empty
      `pushConfig` indicates that the Pub/Sub system should stop pushing
      messages from the given subscription and allow messages to be pulled and
      acknowledged - effectively pausing the subscription if `Pull` is not
      called.
  """

  pushConfig = _messages.MessageField('PushConfig', 1)


class Policy(_messages.Message):
  """Defines an Identity and Access Management (IAM) policy. It is used to
  specify access control policies for Cloud Platform resources.   A `Policy`
  consists of a list of `bindings`. A `Binding` binds a list of `members` to a
  `role`, where the members can be user accounts, Google groups, Google
  domains, and service accounts. A `role` is a named list of permissions
  defined by IAM.  **Example**      {       "bindings": [         {
  "role": "roles/owner",           "members": [
  "user:mike@example.com",             "group:admins@example.com",
  "domain:google.com",             "serviceAccount:my-other-
  app@appspot.gserviceaccount.com",           ]         },         {
  "role": "roles/viewer",           "members": ["user:sean@example.com"]
  }       ]     }  For a description of IAM and its features, see the [IAM
  developer's guide](https://cloud.google.com/iam).

  Fields:
    bindings: Associates a list of `members` to a `role`. Multiple `bindings`
      must not be specified for the same `role`. `bindings` with no members
      will result in an error.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy.  If no `etag` is provided in the call to `setIamPolicy`, then
      the existing policy is overwritten blindly.
    version: Version of the `Policy`. The default version is 0.
  """

  bindings = _messages.MessageField('Binding', 1, repeated=True)
  etag = _messages.BytesField(2)
  version = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class PublishRequest(_messages.Message):
  """Request for the Publish method.

  Fields:
    messages: The messages to publish.
  """

  messages = _messages.MessageField('PubsubMessage', 1, repeated=True)


class PublishResponse(_messages.Message):
  """Response for the `Publish` method.

  Fields:
    messageIds: The server-assigned ID of each published message, in the same
      order as the messages in the request. IDs are guaranteed to be unique
      within the topic.
  """

  messageIds = _messages.StringField(1, repeated=True)


class PubsubMessage(_messages.Message):
  """A message data and its attributes. The message payload must not be empty;
  it must contain either a non-empty data field, or at least one attribute.

  Messages:
    AttributesValue: Optional attributes for this message.

  Fields:
    attributes: Optional attributes for this message.
    data: The message payload.
    messageId: ID of this message, assigned by the server when the message is
      published. Guaranteed to be unique within the topic. This value may be
      read by a subscriber that receives a `PubsubMessage` via a `Pull` call
      or a push delivery. It must not be populated by the publisher in a
      `Publish` call.
    publishTime: The time at which the message was published, populated by the
      server when it receives the `Publish` call. It must not be populated by
      the publisher in a `Publish` call.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class AttributesValue(_messages.Message):
    """Optional attributes for this message.

    Messages:
      AdditionalProperty: An additional property for a AttributesValue object.

    Fields:
      additionalProperties: Additional properties of type AttributesValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a AttributesValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  attributes = _messages.MessageField('AttributesValue', 1)
  data = _messages.BytesField(2)
  messageId = _messages.StringField(3)
  publishTime = _messages.StringField(4)


class PubsubProjectsSnapshotsCreateRequest(_messages.Message):
  """A PubsubProjectsSnapshotsCreateRequest object.

  Fields:
    createSnapshotRequest: A CreateSnapshotRequest resource to be passed as
      the request body.
    name: Optional user-provided name for this snapshot. If the name is not
      provided in the request, the server will assign a random name for this
      snapshot on the same project as the subscription. Note that for REST API
      requests, you must specify a name. Format is
      `projects/{project}/snapshots/{snap}`.
  """

  createSnapshotRequest = _messages.MessageField('CreateSnapshotRequest', 1)
  name = _messages.StringField(2, required=True)


class PubsubProjectsSnapshotsDeleteRequest(_messages.Message):
  """A PubsubProjectsSnapshotsDeleteRequest object.

  Fields:
    snapshot: The name of the snapshot to delete. Format is
      `projects/{project}/snapshots/{snap}`.
  """

  snapshot = _messages.StringField(1, required=True)


class PubsubProjectsSnapshotsGetIamPolicyRequest(_messages.Message):
  """A PubsubProjectsSnapshotsGetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  resource = _messages.StringField(1, required=True)


class PubsubProjectsSnapshotsListRequest(_messages.Message):
  """A PubsubProjectsSnapshotsListRequest object.

  Fields:
    pageSize: Maximum number of snapshots to return.
    pageToken: The value returned by the last `ListSnapshotsResponse`;
      indicates that this is a continuation of a prior `ListSnapshots` call,
      and that the system should return the next page of data.
    project: The name of the cloud project that snapshots belong to. Format is
      `projects/{project}`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  project = _messages.StringField(3, required=True)


class PubsubProjectsSnapshotsSetIamPolicyRequest(_messages.Message):
  """A PubsubProjectsSnapshotsSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class PubsubProjectsSnapshotsTestIamPermissionsRequest(_messages.Message):
  """A PubsubProjectsSnapshotsTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class PubsubProjectsSubscriptionsAcknowledgeRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsAcknowledgeRequest object.

  Fields:
    acknowledgeRequest: A AcknowledgeRequest resource to be passed as the
      request body.
    subscription: The subscription whose message is being acknowledged. Format
      is `projects/{project}/subscriptions/{sub}`.
  """

  acknowledgeRequest = _messages.MessageField('AcknowledgeRequest', 1)
  subscription = _messages.StringField(2, required=True)


class PubsubProjectsSubscriptionsDeleteRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsDeleteRequest object.

  Fields:
    subscription: The subscription to delete. Format is
      `projects/{project}/subscriptions/{sub}`.
  """

  subscription = _messages.StringField(1, required=True)


class PubsubProjectsSubscriptionsGetIamPolicyRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsGetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  resource = _messages.StringField(1, required=True)


class PubsubProjectsSubscriptionsGetRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsGetRequest object.

  Fields:
    subscription: The name of the subscription to get. Format is
      `projects/{project}/subscriptions/{sub}`.
  """

  subscription = _messages.StringField(1, required=True)


class PubsubProjectsSubscriptionsListRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsListRequest object.

  Fields:
    pageSize: Maximum number of subscriptions to return.
    pageToken: The value returned by the last `ListSubscriptionsResponse`;
      indicates that this is a continuation of a prior `ListSubscriptions`
      call, and that the system should return the next page of data.
    project: The name of the cloud project that subscriptions belong to.
      Format is `projects/{project}`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  project = _messages.StringField(3, required=True)


class PubsubProjectsSubscriptionsModifyAckDeadlineRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsModifyAckDeadlineRequest object.

  Fields:
    modifyAckDeadlineRequest: A ModifyAckDeadlineRequest resource to be passed
      as the request body.
    subscription: The name of the subscription. Format is
      `projects/{project}/subscriptions/{sub}`.
  """

  modifyAckDeadlineRequest = _messages.MessageField('ModifyAckDeadlineRequest', 1)
  subscription = _messages.StringField(2, required=True)


class PubsubProjectsSubscriptionsModifyPushConfigRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsModifyPushConfigRequest object.

  Fields:
    modifyPushConfigRequest: A ModifyPushConfigRequest resource to be passed
      as the request body.
    subscription: The name of the subscription. Format is
      `projects/{project}/subscriptions/{sub}`.
  """

  modifyPushConfigRequest = _messages.MessageField('ModifyPushConfigRequest', 1)
  subscription = _messages.StringField(2, required=True)


class PubsubProjectsSubscriptionsPatchRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsPatchRequest object.

  Fields:
    name: The name of the subscription. It must have the format
      `"projects/{project}/subscriptions/{subscription}"`. `{subscription}`
      must start with a letter, and contain only letters (`[A-Za-z]`), numbers
      (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (`~`),
      plus (`+`) or percent signs (`%`). It must be between 3 and 255
      characters in length, and it must not start with `"goog"`.
    updateSubscriptionRequest: A UpdateSubscriptionRequest resource to be
      passed as the request body.
  """

  name = _messages.StringField(1, required=True)
  updateSubscriptionRequest = _messages.MessageField('UpdateSubscriptionRequest', 2)


class PubsubProjectsSubscriptionsPullRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsPullRequest object.

  Fields:
    pullRequest: A PullRequest resource to be passed as the request body.
    subscription: The subscription from which messages should be pulled.
      Format is `projects/{project}/subscriptions/{sub}`.
  """

  pullRequest = _messages.MessageField('PullRequest', 1)
  subscription = _messages.StringField(2, required=True)


class PubsubProjectsSubscriptionsSeekRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsSeekRequest object.

  Fields:
    seekRequest: A SeekRequest resource to be passed as the request body.
    subscription: The subscription to affect.
  """

  seekRequest = _messages.MessageField('SeekRequest', 1)
  subscription = _messages.StringField(2, required=True)


class PubsubProjectsSubscriptionsSetIamPolicyRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class PubsubProjectsSubscriptionsTestIamPermissionsRequest(_messages.Message):
  """A PubsubProjectsSubscriptionsTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class PubsubProjectsTopicsDeleteRequest(_messages.Message):
  """A PubsubProjectsTopicsDeleteRequest object.

  Fields:
    topic: Name of the topic to delete. Format is
      `projects/{project}/topics/{topic}`.
  """

  topic = _messages.StringField(1, required=True)


class PubsubProjectsTopicsGetIamPolicyRequest(_messages.Message):
  """A PubsubProjectsTopicsGetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  resource = _messages.StringField(1, required=True)


class PubsubProjectsTopicsGetRequest(_messages.Message):
  """A PubsubProjectsTopicsGetRequest object.

  Fields:
    topic: The name of the topic to get. Format is
      `projects/{project}/topics/{topic}`.
  """

  topic = _messages.StringField(1, required=True)


class PubsubProjectsTopicsListRequest(_messages.Message):
  """A PubsubProjectsTopicsListRequest object.

  Fields:
    pageSize: Maximum number of topics to return.
    pageToken: The value returned by the last `ListTopicsResponse`; indicates
      that this is a continuation of a prior `ListTopics` call, and that the
      system should return the next page of data.
    project: The name of the cloud project that topics belong to. Format is
      `projects/{project}`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  project = _messages.StringField(3, required=True)


class PubsubProjectsTopicsPublishRequest(_messages.Message):
  """A PubsubProjectsTopicsPublishRequest object.

  Fields:
    publishRequest: A PublishRequest resource to be passed as the request
      body.
    topic: The messages in the request will be published on this topic. Format
      is `projects/{project}/topics/{topic}`.
  """

  publishRequest = _messages.MessageField('PublishRequest', 1)
  topic = _messages.StringField(2, required=True)


class PubsubProjectsTopicsSetIamPolicyRequest(_messages.Message):
  """A PubsubProjectsTopicsSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class PubsubProjectsTopicsSubscriptionsListRequest(_messages.Message):
  """A PubsubProjectsTopicsSubscriptionsListRequest object.

  Fields:
    pageSize: Maximum number of subscription names to return.
    pageToken: The value returned by the last
      `ListTopicSubscriptionsResponse`; indicates that this is a continuation
      of a prior `ListTopicSubscriptions` call, and that the system should
      return the next page of data.
    topic: The name of the topic that subscriptions are attached to. Format is
      `projects/{project}/topics/{topic}`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  topic = _messages.StringField(3, required=True)


class PubsubProjectsTopicsTestIamPermissionsRequest(_messages.Message):
  """A PubsubProjectsTopicsTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class PullRequest(_messages.Message):
  """Request for the `Pull` method.

  Fields:
    maxMessages: The maximum number of messages returned for this request. The
      Pub/Sub system may return fewer than the number specified.
    returnImmediately: If this field set to true, the system will respond
      immediately even if it there are no messages available to return in the
      `Pull` response. Otherwise, the system may wait (for a bounded amount of
      time) until at least one message is available, rather than returning no
      messages. The client may cancel the request if it does not wish to wait
      any longer for the response.
  """

  maxMessages = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  returnImmediately = _messages.BooleanField(2)


class PullResponse(_messages.Message):
  """Response for the `Pull` method.

  Fields:
    receivedMessages: Received Pub/Sub messages. The Pub/Sub system will
      return zero messages if there are no more available in the backlog. The
      Pub/Sub system may return fewer than the `maxMessages` requested even if
      there are more messages available in the backlog.
  """

  receivedMessages = _messages.MessageField('ReceivedMessage', 1, repeated=True)


class PushConfig(_messages.Message):
  """Configuration for a push delivery endpoint.

  Messages:
    AttributesValue: Endpoint configuration attributes.  Every endpoint has a
      set of API supported attributes that can be used to control different
      aspects of the message delivery.  The currently supported attribute is
      `x-goog-version`, which you can use to change the format of the pushed
      message. This attribute indicates the version of the data expected by
      the endpoint. This controls the shape of the pushed message (i.e., its
      fields and metadata). The endpoint version is based on the version of
      the Pub/Sub API.  If not present during the `CreateSubscription` call,
      it will default to the version of the API used to make such call. If not
      present during a `ModifyPushConfig` call, its value will not be changed.
      `GetSubscription` calls will always return a valid version, even if the
      subscription was created without this attribute.  The possible values
      for this attribute are:  * `v1beta1`: uses the push format defined in
      the v1beta1 Pub/Sub API. * `v1` or `v1beta2`: uses the push format
      defined in the v1 Pub/Sub API.

  Fields:
    attributes: Endpoint configuration attributes.  Every endpoint has a set
      of API supported attributes that can be used to control different
      aspects of the message delivery.  The currently supported attribute is
      `x-goog-version`, which you can use to change the format of the pushed
      message. This attribute indicates the version of the data expected by
      the endpoint. This controls the shape of the pushed message (i.e., its
      fields and metadata). The endpoint version is based on the version of
      the Pub/Sub API.  If not present during the `CreateSubscription` call,
      it will default to the version of the API used to make such call. If not
      present during a `ModifyPushConfig` call, its value will not be changed.
      `GetSubscription` calls will always return a valid version, even if the
      subscription was created without this attribute.  The possible values
      for this attribute are:  * `v1beta1`: uses the push format defined in
      the v1beta1 Pub/Sub API. * `v1` or `v1beta2`: uses the push format
      defined in the v1 Pub/Sub API.
    pushEndpoint: A URL locating the endpoint to which messages should be
      pushed. For example, a Webhook endpoint might use
      "https://example.com/push".
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class AttributesValue(_messages.Message):
    """Endpoint configuration attributes.  Every endpoint has a set of API
    supported attributes that can be used to control different aspects of the
    message delivery.  The currently supported attribute is `x-goog-version`,
    which you can use to change the format of the pushed message. This
    attribute indicates the version of the data expected by the endpoint. This
    controls the shape of the pushed message (i.e., its fields and metadata).
    The endpoint version is based on the version of the Pub/Sub API.  If not
    present during the `CreateSubscription` call, it will default to the
    version of the API used to make such call. If not present during a
    `ModifyPushConfig` call, its value will not be changed. `GetSubscription`
    calls will always return a valid version, even if the subscription was
    created without this attribute.  The possible values for this attribute
    are:  * `v1beta1`: uses the push format defined in the v1beta1 Pub/Sub
    API. * `v1` or `v1beta2`: uses the push format defined in the v1 Pub/Sub
    API.

    Messages:
      AdditionalProperty: An additional property for a AttributesValue object.

    Fields:
      additionalProperties: Additional properties of type AttributesValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a AttributesValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  attributes = _messages.MessageField('AttributesValue', 1)
  pushEndpoint = _messages.StringField(2)


class ReceivedMessage(_messages.Message):
  """A message and its corresponding acknowledgment ID.

  Fields:
    ackId: This ID can be used to acknowledge the received message.
    message: The message.
  """

  ackId = _messages.StringField(1)
  message = _messages.MessageField('PubsubMessage', 2)


class SeekRequest(_messages.Message):
  """Request for the `Seek` method.

  Fields:
    snapshot: The snapshot to seek to. The snapshot's topic must be the same
      as that of the provided subscription. Format is
      `projects/{project}/snapshots/{snap}`.
    time: The time to seek to. Messages retained in the subscription that were
      published before this time are marked as acknowledged, and messages
      retained in the subscription that were published after this time are
      marked as unacknowledged. Note that this operation affects only those
      messages retained in the subscription (configured by the combination of
      `message_retention_duration` and `retain_acked_messages`). For example,
      if `time` corresponds to a point before the message retention window (or
      to a point before the system's notion of the subscription creation
      time), only retained messages will be marked as unacknowledged, and
      already-expunged messages will not be restored.
  """

  snapshot = _messages.StringField(1)
  time = _messages.StringField(2)


class SeekResponse(_messages.Message):
  """A SeekResponse object."""


class SetIamPolicyRequest(_messages.Message):
  """Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Cloud Platform services (such as Projects)
      might reject them.
  """

  policy = _messages.MessageField('Policy', 1)


class Snapshot(_messages.Message):
  """A snapshot resource.

  Fields:
    expirationTime: The snapshot is guaranteed to exist up until this time. A
      newly-created snapshot expires no later than 7 days from the time of its
      creation. Its exact lifetime is determined at creation by the existing
      backlog in the source subscription. Specifically, the lifetime of the
      snapshot is `7 days - (age of oldest unacked message in the
      subscription)`. For example, consider a subscription whose oldest
      unacked message is 3 days old. If a snapshot is created from this
      subscription, the snapshot -- which will always capture this 3-day-old
      backlog as long as the snapshot exists -- will expire in 4 days.
    name: The name of the snapshot.
    topic: The name of the topic from which this snapshot is retaining
      messages.
  """

  expirationTime = _messages.StringField(1)
  name = _messages.StringField(2)
  topic = _messages.StringField(3)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class Subscription(_messages.Message):
  """A subscription resource.

  Fields:
    ackDeadlineSeconds: This value is the maximum time after a subscriber
      receives a message before the subscriber should acknowledge the message.
      After message delivery but before the ack deadline expires and before
      the message is acknowledged, it is an outstanding message and will not
      be delivered again during that time (on a best-effort basis).  For pull
      subscriptions, this value is used as the initial value for the ack
      deadline. To override this value for a given message, call
      `ModifyAckDeadline` with the corresponding `ack_id` if using pull. The
      minimum custom deadline you can specify is 10 seconds. The maximum
      custom deadline you can specify is 600 seconds (10 minutes). If this
      parameter is 0, a default value of 10 seconds is used.  For push
      delivery, this value is also used to set the request timeout for the
      call to the push endpoint.  If the subscriber never acknowledges the
      message, the Pub/Sub system will eventually redeliver the message.
    messageRetentionDuration: How long to retain unacknowledged messages in
      the subscription's backlog, from the moment a message is published. If
      `retain_acked_messages` is true, then this also configures the retention
      of acknowledged messages, and thus configures how far back in time a
      `Seek` can be done. Defaults to 7 days. Cannot be more than 7 days or
      less than 10 minutes.
    name: The name of the subscription. It must have the format
      `"projects/{project}/subscriptions/{subscription}"`. `{subscription}`
      must start with a letter, and contain only letters (`[A-Za-z]`), numbers
      (`[0-9]`), dashes (`-`), underscores (`_`), periods (`.`), tildes (`~`),
      plus (`+`) or percent signs (`%`). It must be between 3 and 255
      characters in length, and it must not start with `"goog"`.
    pushConfig: If push delivery is used with this subscription, this field is
      used to configure it. An empty `pushConfig` signifies that the
      subscriber will pull and ack messages using API methods.
    retainAckedMessages: Indicates whether to retain acknowledged messages. If
      true, then messages are not expunged from the subscription's backlog,
      even if they are acknowledged, until they fall out of the
      `message_retention_duration` window.
    topic: The name of the topic from which this subscription is receiving
      messages. Format is `projects/{project}/topics/{topic}`. The value of
      this field will be `_deleted-topic_` if the topic has been deleted.
  """

  ackDeadlineSeconds = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  messageRetentionDuration = _messages.StringField(2)
  name = _messages.StringField(3)
  pushConfig = _messages.MessageField('PushConfig', 4)
  retainAckedMessages = _messages.BooleanField(5)
  topic = _messages.StringField(6)


class TestIamPermissionsRequest(_messages.Message):
  """Request message for `TestIamPermissions` method.

  Fields:
    permissions: The set of permissions to check for the `resource`.
      Permissions with wildcards (such as '*' or 'storage.*') are not allowed.
      For more information see [IAM
      Overview](https://cloud.google.com/iam/docs/overview#permissions).
  """

  permissions = _messages.StringField(1, repeated=True)


class TestIamPermissionsResponse(_messages.Message):
  """Response message for `TestIamPermissions` method.

  Fields:
    permissions: A subset of `TestPermissionsRequest.permissions` that the
      caller is allowed.
  """

  permissions = _messages.StringField(1, repeated=True)


class Topic(_messages.Message):
  """A topic resource.

  Fields:
    name: The name of the topic. It must have the format
      `"projects/{project}/topics/{topic}"`. `{topic}` must start with a
      letter, and contain only letters (`[A-Za-z]`), numbers (`[0-9]`), dashes
      (`-`), underscores (`_`), periods (`.`), tildes (`~`), plus (`+`) or
      percent signs (`%`). It must be between 3 and 255 characters in length,
      and it must not start with `"goog"`.
  """

  name = _messages.StringField(1)


class UpdateSubscriptionRequest(_messages.Message):
  """Request for the UpdateSubscription method.

  Fields:
    subscription: The updated subscription object.
    updateMask: Indicates which fields in the provided subscription to update.
      Must be specified and non-empty.
  """

  subscription = _messages.MessageField('Subscription', 1)
  updateMask = _messages.StringField(2)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'pubsub')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'pubsub')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'pubsub')
