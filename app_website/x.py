from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient

# Authenticate
credential = DefaultAzureCredential()
subscription_id = "<your-subscription-id>"
client = CostManagementClient(credential)

# Scope: subscription
scope = f"/subscriptions/{subscription_id}"

# VMs you want to track
vm_names = ["vm-name-1", "vm-name-2"]  # replace with your actual VM names

# Build the query
query = {
    "type": "ActualCost",
    "timeframe": "MonthToDate",
    "dataset": {
        "granularity": "Daily",
        "aggregation": {
            "totalCost": {
                "name": "PreTaxCost",
                "function": "Sum"
            }
        },
        "filter": {
            "and": [
                {
                    "dimensions": {
                        "name": "ResourceType",
                        "operator": "In",
                        "values": [
                            "Microsoft.Compute/virtualMachines"
                        ]
                    }
                },
                {
                    "dimensions": {
                        "name": "ResourceName",
                        "operator": "In",
                        "values": vm_names
                    }
                }
            ]
        }
    }
}

# Execute the query
result = client.query.usage(scope, query)

# Output the result
for row in result.rows:
    print(row)