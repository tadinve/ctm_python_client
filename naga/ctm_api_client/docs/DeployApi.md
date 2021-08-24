# ctm_api_client.DeployApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_calendar**](DeployApi.md#delete_calendar) | **DELETE** /deploy/calendar/{calendarName} | delete a calendar
[**delete_connection_profile**](DeployApi.md#delete_connection_profile) | **DELETE** /deploy/connectionprofile/{server}/{agent}/{type}/{name} | Delete Local Connection Profile
[**delete_folder**](DeployApi.md#delete_folder) | **DELETE** /deploy/folder/{controlM}/{folderName} | delete a folder
[**delete_local_connection_profile**](DeployApi.md#delete_local_connection_profile) | **DELETE** /deploy/connectionprofile/local/{server}/{agent}/{type}/{name} | Delete Local Connection Profile
[**delete_shared_connection_profile**](DeployApi.md#delete_shared_connection_profile) | **DELETE** /deploy/connectionprofile/centralized/{type}/{name} | Delete centralized Connection Profile
[**deploy_ai_jobtype**](DeployApi.md#deploy_ai_jobtype) | **POST** /deploy/ai/jobtype | Deploy of Application Integrator job type.
[**deploy_file**](DeployApi.md#deploy_file) | **POST** /deploy | Deploy definitions file
[**deploy_jobtype_file**](DeployApi.md#deploy_jobtype_file) | **POST** /deploy/jobtype | Deploy jobtype
[**get_connection_profiles_deployment_status**](DeployApi.md#get_connection_profiles_deployment_status) | **GET** /deploy/connectionprofile/centralized/deploymentstatus/{type}/{name} | Get deployed connection profiles deployment status
[**get_deployed_ai_jobtypes**](DeployApi.md#get_deployed_ai_jobtypes) | **GET** /deploy/ai/jobtypes | Get Application Integrator job types
[**get_deployed_calendars**](DeployApi.md#get_deployed_calendars) | **GET** /deploy/calendars | Get deployed calendars that match the search criteria.
[**get_deployed_connection_profiles**](DeployApi.md#get_deployed_connection_profiles) | **GET** /deploy/connectionprofiles | Get local deployed connection profiles
[**get_deployed_connection_profiles_status**](DeployApi.md#get_deployed_connection_profiles_status) | **GET** /deploy/connectionprofiles/centralized/status | Get deployed connection profiles status
[**get_deployed_folders_new**](DeployApi.md#get_deployed_folders_new) | **GET** /deploy/jobs | Get deployed jobs that match the search criteria.
[**get_local_connection_profiles**](DeployApi.md#get_local_connection_profiles) | **GET** /deploy/connectionprofiles/local | Get local deployed connection profiles
[**get_shared_connection_profiles**](DeployApi.md#get_shared_connection_profiles) | **GET** /deploy/connectionprofiles/centralized | Get centralized deployed connection profile
[**get_site_standard_field_restrictions**](DeployApi.md#get_site_standard_field_restrictions) | **GET** /deploy/sitestandard/{standardName}/fieldRestriction/{fieldName} | Get the allowed values for the specified field in the specified site standard.
[**set_site_standard_field_restrictions**](DeployApi.md#set_site_standard_field_restrictions) | **POST** /deploy/sitestandard/{standardName}/fieldRestriction/{fieldName} | Replace the allowed values for the specified field in the specified site standard.
[**test_connection_profile**](DeployApi.md#test_connection_profile) | **POST** /deploy/connectionprofile/test | Test connection profile on agent
[**transform_file**](DeployApi.md#transform_file) | **POST** /deploy/transform | Transform a definitions file


# **delete_calendar**
> SuccessData delete_calendar(calendar_name, server=server)

delete a calendar

Delete a calendar

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
calendar_name = 'calendar_name_example' # str | The name of the calendar to be deleted.
server = 'Global' # str | The name of the server in which the calendar deploy. (optional) (default to Global)

try:
    # delete a calendar
    api_response = api_instance.delete_calendar(calendar_name, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_name** | **str**| The name of the calendar to be deleted. | 
 **server** | **str**| The name of the server in which the calendar deploy. | [optional] [default to Global]

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection_profile**
> SuccessData delete_connection_profile(server, agent, type, name)

Delete Local Connection Profile

Delete Local Connection Profile.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
server = 'server_example' # str | The name of the Control-M in which the connection profile is deployed.
agent = 'agent_example' # str | The name of the agent the connection profile is deployed on.
type = 'type_example' # str | The type of connection profile to delete.
name = 'name_example' # str | Name of the Connection Profile

try:
    # Delete Local Connection Profile
    api_response = api_instance.delete_connection_profile(server, agent, type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_connection_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The name of the Control-M in which the connection profile is deployed. | 
 **agent** | **str**| The name of the agent the connection profile is deployed on. | 
 **type** | **str**| The type of connection profile to delete. | 
 **name** | **str**| Name of the Connection Profile | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> SuccessData delete_folder(control_m, folder_name)

delete a folder

Delete a folder

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
control_m = 'control_m_example' # str | The name of the Control-M in which the folder(s) are deployed.
folder_name = 'folder_name_example' # str | The name of the required folder(s).

try:
    # delete a folder
    api_response = api_instance.delete_folder(control_m, folder_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **control_m** | **str**| The name of the Control-M in which the folder(s) are deployed. | 
 **folder_name** | **str**| The name of the required folder(s). | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_local_connection_profile**
> SuccessData delete_local_connection_profile(server, agent, type, name)

Delete Local Connection Profile

Delete Local Connection Profile

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
server = 'server_example' # str | The name of the Control-M in which the connection profile is deployed.
agent = 'agent_example' # str | The name of the agent the connection profile is deployed on.
type = 'type_example' # str | The type of connection profile to delete.
name = 'name_example' # str | Name of the Connection Profile

try:
    # Delete Local Connection Profile
    api_response = api_instance.delete_local_connection_profile(server, agent, type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_local_connection_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The name of the Control-M in which the connection profile is deployed. | 
 **agent** | **str**| The name of the agent the connection profile is deployed on. | 
 **type** | **str**| The type of connection profile to delete. | 
 **name** | **str**| Name of the Connection Profile | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shared_connection_profile**
> SuccessData delete_shared_connection_profile(type, name)

Delete centralized Connection Profile

Delete centralized Connection Profile

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
type = 'type_example' # str | The type of connection profile to delete.
name = 'name_example' # str | Name of the Connection Profile

try:
    # Delete centralized Connection Profile
    api_response = api_instance.delete_shared_connection_profile(type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_shared_connection_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of connection profile to delete. | 
 **name** | **str**| Name of the Connection Profile | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_ai_jobtype**
> AiDeployResponse deploy_ai_jobtype(ctm, agent, job_type_id)

Deploy of Application Integrator job type.

Deploy an exsiting Application Integrator job type to agent in order to allow it to run

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
ctm = 'ctm_example' # str | 
agent = 'agent_example' # str | 
job_type_id = 'job_type_id_example' # str | 

try:
    # Deploy of Application Integrator job type.
    api_response = api_instance.deploy_ai_jobtype(ctm, agent, job_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->deploy_ai_jobtype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**|  | 
 **agent** | **str**|  | 
 **job_type_id** | **str**|  | 

### Return type

[**AiDeployResponse**](AiDeployResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_file**
> list[DeploymentFileResults] deploy_file(definitions_file, deploy_descriptor_file=deploy_descriptor_file, additional_configuration=additional_configuration)

Deploy definitions file

Deploy the provided definition file (JSON, XML or zip) to Control-M

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
definitions_file = '/path/to/file.txt' # file | A file that contains definitions to be deployed to the server. Can be either a JSON definition file, an XML definition file, or a zip file that contains multiple JSON or XML definition files.
deploy_descriptor_file = '/path/to/file.txt' # file | Deploy Descriptor JSON file. (optional)
additional_configuration = '/path/to/file.txt' # file | additionalConfiguration to enable skip testing for local connection profile (optional)

try:
    # Deploy definitions file
    api_response = api_instance.deploy_file(definitions_file, deploy_descriptor_file=deploy_descriptor_file, additional_configuration=additional_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->deploy_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions_file** | **file**| A file that contains definitions to be deployed to the server. Can be either a JSON definition file, an XML definition file, or a zip file that contains multiple JSON or XML definition files. | 
 **deploy_descriptor_file** | **file**| Deploy Descriptor JSON file. | [optional] 
 **additional_configuration** | **file**| additionalConfiguration to enable skip testing for local connection profile | [optional] 

### Return type

[**list[DeploymentFileResults]**](DeploymentFileResults.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_jobtype_file**
> DeployJobtypeResponse deploy_jobtype_file(definitions_file, payload_file=payload_file, agent=agent, server=server)

Deploy jobtype

Deploy the provided jobtype to AI server, EM server, and Agent.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
definitions_file = '/path/to/file.txt' # file | A .ctmai file that contains definitions of jobtype to be deployed to the server.
payload_file = '/path/to/file.txt' # file | A JSON file that contains specifications of an agent. (optional)
agent = 'agent_example' # str |  (optional)
server = 'server_example' # str |  (optional)

try:
    # Deploy jobtype
    api_response = api_instance.deploy_jobtype_file(definitions_file, payload_file=payload_file, agent=agent, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->deploy_jobtype_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions_file** | **file**| A .ctmai file that contains definitions of jobtype to be deployed to the server. | 
 **payload_file** | **file**| A JSON file that contains specifications of an agent. | [optional] 
 **agent** | **str**|  | [optional] 
 **server** | **str**|  | [optional] 

### Return type

[**DeployJobtypeResponse**](DeployJobtypeResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_profiles_deployment_status**
> ConnectionProfilesDeploymentStatusResult get_connection_profiles_deployment_status(type, name)

Get deployed connection profiles deployment status

Get currently deployed connection profiles deployment status according to the search query as JSON.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
type = 'type_example' # str | The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP.
name = 'name_example' # str | Name of the Connection Profile

try:
    # Get deployed connection profiles deployment status
    api_response = api_instance.get_connection_profiles_deployment_status(type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_connection_profiles_deployment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP. | 
 **name** | **str**| Name of the Connection Profile | 

### Return type

[**ConnectionProfilesDeploymentStatusResult**](ConnectionProfilesDeploymentStatusResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_ai_jobtypes**
> AiJobtypeList get_deployed_ai_jobtypes(job_type_name=job_type_name, job_type_id=job_type_id)

Get Application Integrator job types

Get deployed Application Integrator job types that match the requested search criteria.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
job_type_name = 'job_type_name_example' # str | Job type display name ( or partial name ) for query. It accepts * as wildcard. (optional)
job_type_id = 'job_type_id_example' # str | Job type id ( or partial name ) for query. It accepts * as wildcard. (optional)

try:
    # Get Application Integrator job types
    api_response = api_instance.get_deployed_ai_jobtypes(job_type_name=job_type_name, job_type_id=job_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_ai_jobtypes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_name** | **str**| Job type display name ( or partial name ) for query. It accepts * as wildcard. | [optional] 
 **job_type_id** | **str**| Job type id ( or partial name ) for query. It accepts * as wildcard. | [optional] 

### Return type

[**AiJobtypeList**](AiJobtypeList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_calendars**
> str get_deployed_calendars(name=name, server=server, type=type, alias=alias)

Get deployed calendars that match the search criteria.

Get definition of calendars as json code that match the requested search criteria.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
name = 'name_example' # str |  (optional)
server = 'server_example' # str |  (optional)
type = 'type_example' # str | Calendar type. (optional)
alias = 'alias_example' # str | Calendar alias name for z/OS servers. (optional)

try:
    # Get deployed calendars that match the search criteria.
    api_response = api_instance.get_deployed_calendars(name=name, server=server, type=type, alias=alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_calendars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **server** | **str**|  | [optional] 
 **type** | **str**| Calendar type. | [optional] 
 **alias** | **str**| Calendar alias name for z/OS servers. | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_connection_profiles**
> str get_deployed_connection_profiles(agent, type, ctm=ctm, server=server)

Get local deployed connection profiles

Get currently local deployed connection profiles according to the search query as JSON.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
agent = 'agent_example' # str | The name of the agent the connection profile is deployed on
type = 'type_example' # str | The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP.
ctm = 'ctm_example' # str | The name of the Control-M in which the connection profile is deployed on (optional)
server = 'server_example' # str | The name of the Control-M in which the connection profile is deployed on (optional)

try:
    # Get local deployed connection profiles
    api_response = api_instance.get_deployed_connection_profiles(agent, type, ctm=ctm, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_connection_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent** | **str**| The name of the agent the connection profile is deployed on | 
 **type** | **str**| The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP. | 
 **ctm** | **str**| The name of the Control-M in which the connection profile is deployed on | [optional] 
 **server** | **str**| The name of the Control-M in which the connection profile is deployed on | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_connection_profiles_status**
> ConnectionProfilesStatusResult get_deployed_connection_profiles_status(limit=limit, name=name, type=type)

Get deployed connection profiles status

Get currently deployed connection profiles status according to the search query as JSON.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
limit = 0 # int | number to limit the returned connection profiles. If missed - get all (optional) (default to 0)
name = '*' # str | conn profile name (support *, ?, and comma, default is * for all). (optional) (default to *)
type = '*' # str | conn profile type (default is * for accounts from all CMs). (optional) (default to *)

try:
    # Get deployed connection profiles status
    api_response = api_instance.get_deployed_connection_profiles_status(limit=limit, name=name, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_connection_profiles_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| number to limit the returned connection profiles. If missed - get all | [optional] [default to 0]
 **name** | **str**| conn profile name (support *, ?, and comma, default is * for all). | [optional] [default to *]
 **type** | **str**| conn profile type (default is * for accounts from all CMs). | [optional] [default to *]

### Return type

[**ConnectionProfilesStatusResult**](ConnectionProfilesStatusResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_folders_new**
> str get_deployed_folders_new(format=format, folder=folder, ctm=ctm, server=server)

Get deployed jobs that match the search criteria.

Get definition of jobs and folders (in the desired format - JSON or XML) that match the requested search criteria.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
format = 'json' # str | Output format (json or xml) (optional) (default to json)
folder = 'folder_example' # str |  (optional)
ctm = 'ctm_example' # str |  (optional)
server = 'server_example' # str |  (optional)

try:
    # Get deployed jobs that match the search criteria.
    api_response = api_instance.get_deployed_folders_new(format=format, folder=folder, ctm=ctm, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_folders_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Output format (json or xml) | [optional] [default to json]
 **folder** | **str**|  | [optional] 
 **ctm** | **str**|  | [optional] 
 **server** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_connection_profiles**
> str get_local_connection_profiles(agent, type, ctm=ctm, server=server)

Get local deployed connection profiles

Get currently local deployed connection profiles according to the search query as JSON.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
agent = 'agent_example' # str | The name of the agent the connection profile is deployed on
type = 'type_example' # str | The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP.
ctm = 'ctm_example' # str | The name of the Control-M in which the connection profile is deployed on (optional)
server = 'server_example' # str | The name of the Control-M in which the connection profile is deployed on (optional)

try:
    # Get local deployed connection profiles
    api_response = api_instance.get_local_connection_profiles(agent, type, ctm=ctm, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_local_connection_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent** | **str**| The name of the agent the connection profile is deployed on | 
 **type** | **str**| The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP. | 
 **ctm** | **str**| The name of the Control-M in which the connection profile is deployed on | [optional] 
 **server** | **str**| The name of the Control-M in which the connection profile is deployed on | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_connection_profiles**
> str get_shared_connection_profiles(type, name=name)

Get centralized deployed connection profile

Get currently centralized deployed connection profiles according to the search query as JSON.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
type = '*' # str | The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP. Use * to get all types (default to *)
name = '*' # str | The name of centralized connection profile. Supports for *, ?, and comma. By default is * (optional) (default to *)

try:
    # Get centralized deployed connection profile
    api_response = api_instance.get_shared_connection_profiles(type, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_shared_connection_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP. Use * to get all types | [default to *]
 **name** | **str**| The name of centralized connection profile. Supports for *, ?, and comma. By default is * | [optional] [default to *]

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_standard_field_restrictions**
> str get_site_standard_field_restrictions(standard_name, field_name)

Get the allowed values for the specified field in the specified site standard.

Get the allowed values for the specified field in the specified site standard.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
standard_name = 'standard_name_example' # str | 
field_name = 'field_name_example' # str | 

try:
    # Get the allowed values for the specified field in the specified site standard.
    api_response = api_instance.get_site_standard_field_restrictions(standard_name, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_site_standard_field_restrictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_name** | **str**|  | 
 **field_name** | **str**|  | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_standard_field_restrictions**
> SuccessData set_site_standard_field_restrictions(standard_name, field_name, values_file)

Replace the allowed values for the specified field in the specified site standard.

Replace the allowed values for the specified field in the specified site standard.

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
standard_name = 'standard_name_example' # str | 
field_name = 'field_name_example' # str | 
values_file = ctm_api_client.FieldValues() # FieldValues | The JSON file with the allowed values

try:
    # Replace the allowed values for the specified field in the specified site standard.
    api_response = api_instance.set_site_standard_field_restrictions(standard_name, field_name, values_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->set_site_standard_field_restrictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_name** | **str**|  | 
 **field_name** | **str**|  | 
 **values_file** | [**FieldValues**](FieldValues.md)| The JSON file with the allowed values | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection_profile**
> SuccessData test_connection_profile(definitions_file, ctm=ctm, agent=agent)

Test connection profile on agent

Test connection profile on agent

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
definitions_file = '/path/to/file.txt' # file | A file that contains definitions of the connection profile to be tested
ctm = 'ctm_example' # str |  (optional)
agent = 'agent_example' # str |  (optional)

try:
    # Test connection profile on agent
    api_response = api_instance.test_connection_profile(definitions_file, ctm=ctm, agent=agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->test_connection_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions_file** | **file**| A file that contains definitions of the connection profile to be tested | 
 **ctm** | **str**|  | [optional] 
 **agent** | **str**|  | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transform_file**
> str transform_file(definitions_file, deploy_descriptor_file)

Transform a definitions file

Transform the provided definitions file (JSON) according to the provided Deploy Descriptor file (JSON).

### Example
```python
from __future__ import print_function
import time
import ctm_api_client
from ctm_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = ctm_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ctm_api_client.DeployApi(ctm_api_client.ApiClient(configuration))
definitions_file = '/path/to/file.txt' # file | A file that contains definitions to be deployed to the server. Can be either a JSON definition file, an XML definition file, or a zip file that contains multiple JSON or XML definition files.
deploy_descriptor_file = '/path/to/file.txt' # file | Deploy Descriptor JSON file.

try:
    # Transform a definitions file
    api_response = api_instance.transform_file(definitions_file, deploy_descriptor_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->transform_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions_file** | **file**| A file that contains definitions to be deployed to the server. Can be either a JSON definition file, an XML definition file, or a zip file that contains multiple JSON or XML definition files. | 
 **deploy_descriptor_file** | **file**| Deploy Descriptor JSON file. | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

