# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for ListTableSpecs
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-automl


# [START automl_v1beta1_generated_AutoMl_ListTableSpecs_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import automl_v1beta1


async def sample_list_table_specs():
    # Create a client
    client = automl_v1beta1.AutoMlAsyncClient()

    # Initialize request argument(s)
    request = automl_v1beta1.ListTableSpecsRequest(
        parent="parent_value",
    )

    # Make the request
    page_result = client.list_table_specs(request=request)

    # Handle the response
    async for response in page_result:
        print(response)

# [END automl_v1beta1_generated_AutoMl_ListTableSpecs_async]