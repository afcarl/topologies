#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: EPL-2.0
#

'''

Creates the Ansible inventory file (inv.yml) based on the
parameter server and worker node IPs in settings_dist.py

'''

from settings_dist import PS_HOSTS, WORKER_HOSTS

with open('inv.yml','w') as txt_file:

	txt_file.write('# These are the nodes that will be used in the distributed TensorFlow training\n')
	txt_file.write('# This file is auto-generated by the list in settings_dist.py\n')
	txt_file.write('# DO NOT EDIT\n\n')
	txt_file.write('[nodes]\n')

	for x in PS_HOSTS:
		txt_file.write('{}\n'.format(x))

	for x in WORKER_HOSTS:
		txt_file.write('{}\n'.format(x))
