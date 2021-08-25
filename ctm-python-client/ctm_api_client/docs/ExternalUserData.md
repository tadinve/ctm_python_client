# ExternalUserData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | external user name REQUIRED:addExternalUser | HIDDEN | [optional] 
**email** | **str** | user email REQUIRED:addExternalUser | HIDDEN | [optional] 
**company** | **str** | user&#39;s company REQUIRED:addExternalUser | HIDDEN | [optional] 
**password** | **str** | user password HIDDEN:updateExternalUser | [optional] 
**description** | **str** | user description HIDDEN | [optional] 
**phone_number** | **str** | external user phone number HIDDEN | [optional] 
**ssh_key** | **str** | SSH key string HIDDEN | [optional] 
**as2_key** | [**As2KeyData**](As2KeyData.md) | AS2 key string HIDDEN | [optional] 
**is_locked** | **bool** | indicates whether the user account is locked HIDDEN | [optional] 
**lock_reason** | **str** | provides the reason for locking the user account HIDDEN | [optional] 
**change_password_at_next_login** | **bool** | indicates whether a password change is required at next login HIDDEN | [optional] 
**password_never_expires** | **bool** | indicates whether the user&#39;s password is set to never expire HIDDEN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


