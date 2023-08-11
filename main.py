from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

key_vault_name = "<your-unique-keyvault-name>"
key_vault_uri = f"https://{key_vault_name}.vault.azure.net"
secret_name = "mySecret"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=key_vault_uri, credential=credential)
retrieved_secret = client.get_secret(secret_name)

print(f"The value of secret '{secret_name}' in '{key_vault_name}' is: '{retrieved_secret.value}'")
