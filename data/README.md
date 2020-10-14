# Data collection

## Post data

Post from Marvin (combining answers with questions, but without comments) (the integer within "upvotes" and "comments" field is actually Unix timestamps)

```json
{
  "tags": ["ios", "iphone", "amazon-web-services", "amazon-cognito"],
  "is_answered": true,
  "view_count": 1067,
  "accepted_answer_id": 37146730,
  "answer_count": 2,
  "score": 2,
  "last_activity_date": 1462906453,
  "creation_date": 1462843379,
  "question_id": 37127831,
  "content_license": "CC BY-SA 3.0",
  "link": "https://stackoverflow.com/questions/37127831/aws-expiredtokenexception-after-app-relaunch",
  "title": "AWS ExpiredTokenException after app relaunch",
  "body": "<p>I'm building an iOS (Swift) app using AWS as the backend with Developer Authenticated Identities. Everything works fine until I close the app, leave it for a while and then relaunch. In this scenario I often, but not always, receive ExpiredTokenException errors when trying to retrieve data from AWS.</p>\n\n<p>Here is my code:</p>\n\n<pre><code>class DeveloperAuthenticatedIdentityProvider: AWSAbstractCognitoIdentityProvider {\n    var _token: String!\n    var _logins: [ NSObject : AnyObject ]!\n\n    override var token: String {\n        get {\n            return _token\n        }\n    }\n\n    ultServiceRegion, credentialsProvider: credentialsProvider)\n    AWSServiceManager.defaultServiceManager().defaultServiceConfiguration = configuration\n\n    // set service configuration for S3 (my bucket is located in a different region to my Cognito and Lambda service)\n    let credentialsProviderForS3 = AWSCognitoCredentialsProvider(regionType: cognitoRegion, identityProvider: identityProvider, unauthRoleArn: unauthRole, authRoleArn: unauthRole)\n    let awsConfigurationForS3 = AWSServiceConfiguration(region: s3ServiceRegion, credentialsProvider: credentialsProviderForS3)\n    AWSS3TransferUtility.registerS3TransferUtilityWithConfiguration(awsConfigurationForS3, forKey: \"S3\")\n\n    return true\n}\n</code></pre>\n\n<p>This <a href=\"http://direct.amorf.net/index.cgi/00/https/forums.aws.amazon.com/thread.jspa=3fmessageID=3d711931\" rel=\"nofollow\">post</a> suggests that the Cognito token has expired and it is up to the developer to manually refresh. This seems overly complex as it would require setting a timer to refresh regularly, handling app closures and relaunches and handling AWS requests that occur while the refresh is taking place. Is there a simpler way? For example, is it possible to have the AWS SDK automatically call refresh whenever it attempts to query the server using an expired token?</p>\n\n<p>Any help would be appreciated. I'm using version 2.3.5 of the AWS SDK for iOS.</p>\n",
  "answers": {
    "37146730": {
      "is_accepted": true,
      "score": 1,
      "last_activity_date": 1462906453,
      "creation_date": 1462906453,
      "answer_id": 37146730,
      "question_id": 37127831,
      "content_license": "CC BY-SA 3.0",
      "body": "<p>The AWS Mobile SDK for iOS 2.4.x has a new protocol called <a href=\"https://github.com/aws/aws-sdk-ios/blob/master/AWSCore/Authentication/AWSIdentityProvider.h#L66\" rel=\"nofollow\"><code>AWSIdentityProviderManager</code></a>. It has the following method:</p>\n\n<pre><code>/**\n * Each entry in logins represents a single login with an identity provider.\n * The key is the domain of the login provider (e.g. 'graph.facebook.com') and the value is the\n * OAuth/OpenId Connect token that results from an authentication with that login provider.\n */\n- (AWSTask&lt;NSDictionary&lt;NSString *, NSString *&gt; *&gt; *)logins;\n</code></pre>\n\n<p>The responsibility of an object conforming to this protocol is to return a valid <code>logins</code> dictionary whenever it is requested. Because this method is asynchronous, you can make networking calls in it if the cached token is expired. The implementation is up to you, but in many cases, <code>AWSIdentityProviderManager</code> manages multiple <a href=\"https://github.com/aws/aws-sdk-ios/blob/master/AWSCore/Authentication/AWSIdentityProvider.h#L52\" rel=\"nofollow\"><code>AWSIdentityProvider</code></a>s, aggregates them and return the <code>logins</code> dictionary.</p>\n",
      "upvotes": [1463184000],
      "comments": [1463020870]
    },
    "37130926": {
      "is_accepted": false,
      "score": 0,
      "last_activity_date": 1462862192,
      "creation_date": 1462862192,
      "answer_id": 37130926,
      "question_id": 37127831,
      "content_license": "CC BY-SA 3.0",
      "body": "<p>Unfortunately developers refreshing the token is the only way.</p>\n\n<p>I agree that it would be simpler for app developers if AWS SDK handled this but the way CrdentialsProvider is designed is supposed to be generic for all providers. For example, if someone wants to use Facebook as provider then AWS SDK will not be able to handle the refresh on its own and developer will have t handle that in his app. Keeping the refresh flow out of the SDK gives us the capability to keep the CredentialsProvider generic.</p>\n",
      "upvotes": [],
      "comments": [1462888093, 1462881271]
    }
  },
  "upvotes": [1494288000, 1466985600],
  "comments": []
}
```

Posts tree with comments

```json
{
  "tags": ["ios", "iphone", "amazon-web-services", "amazon-cognito"],
  "view_count": 1067,
  "answer_count": 2,
  "score": 2,
  "last_activity_date": 1462906453,
  "creation_date": 1462843379,
  "question_id": 37127831,
  "link": "https://stackoverflow.com/questions/37127831/aws-expiredtokenexception-after-app-relaunch",
  "title": "AWS ExpiredTokenException after app relaunch",
  "body": "<p>I'm building an iOS (Swift) app using AWS as the backend with Developer Authenticated Identities. Everything works fine until I close the app, leave it for a while and then relaunch. In this scenario I often, but not always, receive ExpiredTokenException errors when trying to retrieve data from AWS.</p>\n\n<p>Here is my code:</p>\n\n<pre><code>class DeveloperAuthenticatedIdentityProvider: AWSAbstractCognitoIdentityProvider {\n    var _token: String!\n    var _logins: [ NSObject : AnyObject ]!\n\n    override var token: String {\n        get {\n            return _token\n        }\n    }\n\n    ultServiceRegion, credentialsProvider: credentialsProvider)\n    AWSServiceManager.defaultServiceManager().defaultServiceConfiguration = configuration\n\n    // set service configuration for S3 (my bucket is located in a different region to my Cognito and Lambda service)\n    let credentialsProviderForS3 = AWSCognitoCredentialsProvider(regionType: cognitoRegion, identityProvider: identityProvider, unauthRoleArn: unauthRole, authRoleArn: unauthRole)\n    let awsConfigurationForS3 = AWSServiceConfiguration(region: s3ServiceRegion, credentialsProvider: credentialsProviderForS3)\n    AWSS3TransferUtility.registerS3TransferUtilityWithConfiguration(awsConfigurationForS3, forKey: \"S3\")\n\n    return true\n}\n</code></pre>\n\n<p>This <a href=\"http://direct.amorf.net/index.cgi/00/https/forums.aws.amazon.com/thread.jspa=3fmessageID=3d711931\" rel=\"nofollow\">post</a> suggests that the Cognito token has expired and it is up to the developer to manually refresh. This seems overly complex as it would require setting a timer to refresh regularly, handling app closures and relaunches and handling AWS requests that occur while the refresh is taking place. Is there a simpler way? For example, is it possible to have the AWS SDK automatically call refresh whenever it attempts to query the server using an expired token?</p>\n\n<p>Any help would be appreciated. I'm using version 2.3.5 of the AWS SDK for iOS.</p>\n",
  "answers": {
    "37146730": {
      "is_accepted": true,
      "score": 1,
      "last_activity_date": 1462906453,
      "creation_date": 1462906453,
      "answer_id": 37146730,
      "question_id": 37127831,
      "body": "<p>The AWS Mobile SDK for iOS 2.4.x has a new protocol called <a href=\"https://github.com/aws/aws-sdk-ios/blob/master/AWSCore/Authentication/AWSIdentityProvider.h#L66\" rel=\"nofollow\"><code>AWSIdentityProviderManager</code></a>. It has the following method:</p>\n\n<pre><code>/**\n * Each entry in logins represents a single login with an identity provider.\n * The key is the domain of the login provider (e.g. 'graph.facebook.com') and the value is the\n * OAuth/OpenId Connect token that results from an authentication with that login provider.\n */\n- (AWSTask&lt;NSDictionary&lt;NSString *, NSString *&gt; *&gt; *)logins;\n</code></pre>\n\n<p>The responsibility of an object conforming to this protocol is to return a valid <code>logins</code> dictionary whenever it is requested. Because this method is asynchronous, you can make networking calls in it if the cached token is expired. The implementation is up to you, but in many cases, <code>AWSIdentityProviderManager</code> manages multiple <a href=\"https://github.com/aws/aws-sdk-ios/blob/master/AWSCore/Authentication/AWSIdentityProvider.h#L52\" rel=\"nofollow\"><code>AWSIdentityProvider</code></a>s, aggregates them and return the <code>logins</code> dictionary.</p>\n",
      "upvotes": [1463184000],
      "comments": [
        {
          "owner": {
            "reputation": 3413,
            "user_id": 3932569,
            "display_name": "Garf365",
            "link": "https://stackoverflow.com/users/3932569/garf365"
          },
          "score": 0,
          "post_type": "question",
          "creation_date": 1464862898,
          "post_id": 37588941,
          "comment_id": 62663293,
          "body_markdown": "Just by curiosity, what do you attempt to do ?",
          "body": "Just by curiosity, what do you attempt to do ?"
        }
      ]
    },
    "37130926": {
      "is_accepted": false,
      "score": 0,
      "last_activity_date": 1462862192,
      "creation_date": 1462862192,
      "answer_id": 37130926,
      "question_id": 37127831,
      "body": "<p>Unfortunately developers refreshing the token is the only way.</p>\n\n<p>I agree that it would be simpler for app developers if AWS SDK handled this but the way CrdentialsProvider is designed is supposed to be generic for all providers. For example, if someone wants to use Facebook as provider then AWS SDK will not be able to handle the refresh on its own and developer will have t handle that in his app. Keeping the refresh flow out of the SDK gives us the capability to keep the CredentialsProvider generic.</p>\n",
      "upvotes": [],
      "comments": [1462888093, 1462881271]
    }
  },
  "upvotes": [1494288000, 1466985600],
  "comments": []
}
```
