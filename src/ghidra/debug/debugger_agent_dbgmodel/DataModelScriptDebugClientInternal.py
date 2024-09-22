# /* ###
 * IP: GHIDRA
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package agent.dbgmodel.impl.dbgmodel.datamodel.script.debug;

import java.util.List;
import java.util.Map;

import com.sun.jna.Pointer;

import agent.dbgeng.impl.dbgeng.DbgEngUtil;
import agent.dbgeng.impl.dbgeng.DbgEngUtil.InterfaceSupplier;
import agent.dbgeng.impl.dbgeng.DbgEngUtil.Preferred;
import agent.dbgmodel.dbgmodel.datamodel.script.debug.DataModelScriptDebugClient;
import agent.dbgmodel.jna.dbgmodel.datamodel.script.debug.IDataModelScriptDebugClient;
import agent.dbgmodel.jna.dbgmodel.datamodel.script.debug.WrapIDataModelScriptDebugClient;
import ghidra.util.datastruct.WeakValueHashMap;

public interface DataModelScriptDebugClientInternal extends DataModelScriptDebugClient {
	Map<Pointer, DataModelScriptDebugClientInternal> CACHE = new WeakValueHashMap<>();

	static DataModelScriptDebugClientInternal instanceFor(
			WrapIDataModelScriptDebugClient data) {
		return DbgEngUtil.lazyWeakCache(CACHE, data, DataModelScriptDebugClientImpl::new);
	}

	List<Preferred<WrapIDataModelScriptDebugClient>> PREFERRED_DATA_SPACES_IIDS = List.of(
		new Preferred<>(IDataModelScriptDebugClient.IID_IDATA_MODEL_SCRIPT_DEBUG_CLIENT,
			WrapIDataModelScriptDebugClient.class));

	static DataModelScriptDebugClientInternal tryPreferredInterfaces(InterfaceSupplier supplier) {
		return DbgEngUtil.tryPreferredInterfaces(DataModelScriptDebugClientInternal.class,
			PREFERRED_DATA_SPACES_IIDS, supplier);
	}
}
