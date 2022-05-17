# Copyright (C) 2022 Indoc Research
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from enum import Enum
from atlas_api import module_api
from flask_restx import Api, Resource, fields
from config import ConfigClass

class EDataType(Enum):
    nfs_file = 0
    nfs_file_processed = 1
    nfs_file_download = 2

class EPipeline(Enum):
    dicom_edit = 0
    data_transfer = 1

file_data_post_form = module_api.model(
    'FileDataPostForm',
    {
        'global_entity_id': fields.String(readOnly=True, description='global_entity_id'),
        'uploader': fields.String(readOnly=True, description='uploader'),
        'file_name': fields.String(readOnly=True, description='file name (not include path)'),
        'path': fields.String(readOnly=True, description='path'),
        'file_size': fields.Integer(readOnly=True, description='file size'),
        'description': fields.String(readOnly=True, description='description'),
        'namespace': fields.String(readOnly=True, description='namespace', enum=['greenroom', 'core']),
        'project_code': fields.String(readOnly=True, description='project code'),
        'labels': fields.List(readOnly=True, description='labels', cls_or_instance=fields.String), ## optional
        "dcm_id": fields.String(readOnly=True, description=''), ## optional
        'processed_pipeline': fields.String(readOnly=True, description='processed_pipeline'), ## optional, for processed file
        'operator': fields.String(readOnly=True, description='operator'), ## optional, for processed file
    }
)