# ==================================================================================================
# Copyright 2011 Twitter, Inc.
# --------------------------------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==================================================================================================

from python_target import PythonTarget

class PythonBinary(PythonTarget):
  def __init__(self, name, source, dependencies = None):
    """
      name: target name
      source: the python source file that becomes this binary's __main__
      dependencies: a list of other PythonLibrary or Pants targets this binary depends upon
    """
    PythonTarget.__init__(
      self,
      'src/python',
      name,
      [source],
      dependencies = dependencies)
