##  Docs
# https://docs.microsoft.com/en-us/azure/key-vault/general/authentication#authentication-to-key-vault-in-application-code
# https://azuresdkdocs.blob.core.windows.net/$web/python/azure-identity/1.6.0/azure.identity.html#azure.identity.EnvironmentCredential
# https://docs.microsoft.com/en-us/python/api/azure-keyvault-secrets/azure.keyvault.secrets.secretclient?view=azure-python#get-secret-name--version-none----kwargs-

# You need the following environment variables
# AZURE_TENANT_ID: ID of the service principal’s tenant. Also called its ‘directory’ ID.
# AZURE_CLIENT_ID: the service principal’s client ID
# AZURE_CLIENT_SECRET: one of the service principal’s client secrets

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

default_credential = DefaultAzureCredential(logging_enable=True)
client = SecretClient("https://azure-kv-aadauth-kv.vault.azure.net/", default_credential)
secretValue = client.get_secret("secret")
print(secretValue.value)
