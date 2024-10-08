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
package ghidra.dbg.jdi.model;

import java.util.List;
import java.util.Map;
import java.util.concurrent.CompletableFuture;

import ghidra.dbg.DebuggerObjectModel.RefreshBehavior;
import ghidra.dbg.target.TargetMemoryRegion;
import ghidra.dbg.target.TargetSection;
import ghidra.dbg.target.schema.*;
import ghidra.dbg.target.schema.TargetObjectSchema.ResyncMode;
import ghidra.program.model.address.AddressRange;

@TargetObjectSchemaInfo(
	name = "ConstantPool",
	elements = {
		@TargetElementType(type = Void.class)
	},
	elementResync = ResyncMode.ONCE,
	attributes = {
		@TargetAttributeType(type = Void.class)
	},
	canonicalContainer = true)
public class JdiModelTargetConstantPool extends JdiModelTargetObjectImpl implements //
		//TargetMemory
		TargetMemoryRegion, TargetSection {

	private AddressRange range;
	private byte[] pool;

	public JdiModelTargetConstantPool(JdiModelTargetSectionContainer parent, byte[] pool,
			boolean isElement) {
		super(parent, "Constant Pool", pool, isElement);
		this.pool = pool;

		this.range = impl.getAddressRange(getClassType(), pool.length);

		changeAttributes(List.of(), List.of(), Map.of( //
			DISPLAY_ATTRIBUTE_NAME, getDisplay(), //
			MODULE_ATTRIBUTE_NAME, parent.getClassType(), //
			READABLE_ATTRIBUTE_NAME, true, //
			MEMORY_ATTRIBUTE_NAME, parent, //
			TargetMemoryRegion.RANGE_ATTRIBUTE_NAME, range //
		), "Initialized");
	}

	@Override
	public CompletableFuture<Void> requestAttributes(RefreshBehavior refresh) {

		this.range = impl.getAddressRange(getClassType(), pool.length);
		if (range != null) {
			changeAttributes(List.of(), List.of(), Map.of(), "Initialized");
		}

		return CompletableFuture.completedFuture(null);
	}

	@Override
	public CompletableFuture<Void> init() {
		return CompletableFuture.completedFuture(null);
	}

	@Override
	public String getDisplay() {
		JdiModelTargetReferenceType classType = getClassType();
		return classType.getName() + ": ConstPool" + range;
	}

	private JdiModelTargetReferenceType getClassType() {
		JdiModelTargetReferenceType classType =
			((JdiModelTargetSectionContainer) parent).getClassType();
		return classType;
	}

	@Override
	public AddressRange getRange() {
		return range;
	}

	public byte[] getPool() {
		return pool;
	}

}
