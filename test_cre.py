import os
import streamlit as st
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

subscription_id = os.environ["SUBSCRIPTION_ID"]
resource_group = os.environ["RESOURCE_GROUP"]
workspace_name = os.environ["WORKSPACE_NAME"]


print(DefaultAzureCredential())
# Create Azure ML client
ml_client = MLClient(
    credential=DefaultAzureCredential(),
    subscription_id=subscription_id,
    resource_group_name=resource_group,
    workspace_name=workspace_name,
)
print(ml_client)
print(ml_client.model)
model_name = "XGBoost_Model"
# Get latest version of model
my_model = ml_client.models.get(model_name, label="latest")
endpoint_name = "endpoint-xgb-model"
print(ml_client.online_endpoints)
print(list(ml_client.online_endpoints.list()))
# Get the endpoint credentials
endpoint = ml_client.online_endpoints.get(endpoint_name)
print(endpoint)
st.write("hoidho")
