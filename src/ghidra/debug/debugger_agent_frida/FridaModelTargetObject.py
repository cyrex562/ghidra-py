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
package agent.frida.model.iface2;

import java.util.List;
import java.util.Map;
import java.util.concurrent.CompletableFuture;

import agent.frida.manager.impl.FridaManagerImpl;
import agent.frida.model.AbstractFridaModel;
import ghidra.async.AsyncUtils;
import ghidra.dbg.agent.SpiTargetObject;
import ghidra.dbg.target.TargetObject;
import ghidra.dbg.util.CollectionUtils.Delta;

public interface FridaModelTargetObject extends SpiTargetObject {

	@Override
	public AbstractFridaModel getModel();

	public default CompletableFuture<Void> init(Map<String, Object> map) {
		return CompletableFuture.completedFuture(null);
	}

	public default FridaManagerImpl getManager() {
		return (FridaManagerImpl) getModel().getManager();
	}

	public default FridaManagerImpl getManagerWithCheck() {
		FridaManagerImpl impl = (FridaManagerImpl) getModel().getManager();
		if (impl == null) {
			return impl;
		}
		return impl;
	}

	public Delta<?, ?> changeAttributes(List<String> remove, Map<String, ?> add, String reason);

	public CompletableFuture<? extends Map<String, ?>> requestNativeAttributes();

	public default CompletableFuture<Void> requestAugmentedAttributes() {
		return AsyncUtils.nil();
	}

	public CompletableFuture<List<TargetObject>> requestNativeElements();

	public FridaModelTargetSession getParentSession();

	public FridaModelTargetProcess getParentProcess();

	public FridaModelTargetThread getParentThread();

	public TargetObject getProxy();

	public void setModified(Map<String, Object> map, boolean b);

	public void setModified(boolean modified);

	public void resetModified();

	public Object getModelObject();

	public void setModelObject(Object modelObject);

	public void addMapObject(Object object, TargetObject targetObject);

	public TargetObject getMapObject(Object object);

	public void deleteMapObject(Object object);
}
