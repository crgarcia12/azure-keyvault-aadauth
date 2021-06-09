# azure-keyvault-aadauth
Log-in from python to Azure KeyVault to retrieve secrets 

New Auth libraries for Python are really good! 

First, the flow. How is the communication happening?
![AAD flow](https://docs.microsoft.com/en-us/azure/key-vault/media/authentication/authentication-flow.png)

[source](https://docs.microsoft.com/en-us/azure/key-vault/general/authentication#the-key-vault-request-operation-flow-with-authentication)

The code will have two parts:

First get the Credentials (token) :
```
default_credential = DefaultAzureCredential(logging_enable=True)
```
Second create a client that connect to KeyVault (KV)
```
client = SecretClient("https://<KV_Name>.vault.azure.net/", default_credential)
```

`DefaultAzureCredential` will automatically try to use the app's managed identity (MSI) when running on Azure, but it will also automatically load a local service principal from environment variables when running locally or in any other cloud.
The credential object can be used to authenticate to a lot of different Azure services