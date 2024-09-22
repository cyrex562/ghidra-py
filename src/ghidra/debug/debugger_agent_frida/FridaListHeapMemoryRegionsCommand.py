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
package agent.frida.manager.cmd;

import java.util.ArrayList;
import java.util.List;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import agent.frida.manager.FridaMemoryRegionInfo;
import agent.frida.manager.FridaProcess;
import agent.frida.manager.impl.FridaManagerImpl;

public class FridaListHeapMemoryRegionsCommand extends AbstractFridaCommand<Void> {

	private FridaProcess process;
	private List<FridaMemoryRegionInfo> regions = new ArrayList<>();

	public FridaListHeapMemoryRegionsCommand(FridaManagerImpl manager, FridaProcess process) {
		super(manager);
		this.process = process;
	}

	/*
	@Override
	public List<FridaMemoryRegionInfo> complete(FridaPendingCommand<?> pending) {
		return memoryRegions;
	}
	*/

	@Override
	public void invoke() {
		manager.loadScript(this, "list_malloc_ranges",     
				"result = Process.enumerateMallocRanges('---');");
		for (FridaMemoryRegionInfo region : regions) {
			manager.addMemoryRegionIfAbsent(process, region);
		}
	}

	@Override
	public void parseSpecifics(JsonElement element) {
		FridaMemoryRegionInfo region = new FridaMemoryRegionInfo(process);
		JsonObject memDetails = element.getAsJsonObject();
		region.setRangeAddress(memDetails.get("base").getAsString());
		region.setRangeSize(memDetails.get("size").getAsLong());
		regions.add(region);
	}
	
}
