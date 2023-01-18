# CINParsingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**municipality** | **str** | Issuing municipality (or, if living abroad, issuing embassy/consulate). | [optional] 
**name** | **str** | Holder&#39;s name found on the identity card. | [optional] 
**surname** | **str** | Holder&#39;s surname found on the identity card. | [optional] 
**date_of_birth** | **str** | Holder&#39;s date of birth found on the identity card in the format *dd/mm/yyyy*. It is based on the *PLACE AND DATE OF BIRTH* field. | [optional] 
**place_of_birth** | **str** | Holder&#39;s place of birth found on the identity card. It is based on the *PLACE AND DATE OF BIRTH* field. | [optional] 
**sex** | **str** | Holder&#39;s gender as found on the document; *M* or *F* for *male* or *female*, respectively. | [optional] 
**height** | **int** | Holder&#39;s height found on the identity card. Measured in centimetres. | [optional]  if omitted the server will use the default value of 0
**nationality** | **str** | Holder&#39;s nationality found on the identity card. | [optional] 
**issuing** | **str** | Date of issue of the identity card in the format *dd/mm/yyyy*. | [optional] 
**expiry** | **str** | Expiration date of the identity card in the format *dd/mm/yyyy*. | [optional] 
**fiscal_code** | **str** | Holder&#39;s Italian fiscal code. | [optional] 
**birth_certificate** | **str** | Holder&#39;s details of the birth certificate found on the identity card. It refers to the field *ESTREMI ATTO DI NASCITA* | [optional] 
**residence** | **str** | Holder&#39;s place of residence found on the identity card. It is based on the *RESIDENCE* field. | [optional] 
**address** | **str** | Holder&#39;s residence address found on the identity card. It is based on the *RESIDENCE* field. | [optional] 
**document_number** | **str** | Card number, a sort of serial number identifying the document. | [optional] 
**card_access_number** | **str** | CAN - Card Access Number. | [optional] 
**legal_guardian** | **str** | Surname and name of parents or legal guardian (only for applicants aged 0–18). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


