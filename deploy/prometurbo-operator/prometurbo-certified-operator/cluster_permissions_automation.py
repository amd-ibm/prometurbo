#!/usr/bin/env python
import ruamel.yaml

## Utility function to update the cluster permission roles into target csv file
def insert_fields(cluster_permission_role_yaml, certified_operator_cluster_service_version_yaml):
    cluster_role_data = ruamel.yaml.round_trip_load(open(cluster_permission_role_yaml, 'r'))
    rules = cluster_role_data.get('rules', [])
    csv_data = ruamel.yaml.round_trip_load(open(certified_operator_cluster_service_version_yaml, 'r'))
    csv_data['spec']['install']['spec']['clusterPermissions'] = [{'rules': rules, 'serviceAccountName': 'prometurbo-operator'}]
    with open(certified_operator_cluster_service_version_yaml, 'w') as f:
        ruamel.yaml.round_trip_dump(csv_data, f)
    print("cluster permissions role inserted successfully.")


CLUSTER_PERMISSION_ROLE_YAML_FILE_PATH = 'deploy/prometurbo-operator-cluster-role.yaml'
CERTIFIED_OPERATOR_CLUSTER_SERVICE_VERSION_YAML_FILE_PATH = 'prometurbo-certified-operator-bundle/manifest/prometurbo-certified.clusterserviceversion.yaml'

insert_fields(CLUSTER_PERMISSION_ROLE_YAML_FILE_PATH, CERTIFIED_OPERATOR_CLUSTER_SERVICE_VERSION_YAML_FILE_PATH)