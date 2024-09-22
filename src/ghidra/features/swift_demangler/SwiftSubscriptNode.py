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
package ghidra.app.util.demangler.swift.nodes;

import ghidra.app.util.demangler.*;
import ghidra.app.util.demangler.swift.SwiftDemangledNodeKind;
import ghidra.app.util.demangler.swift.SwiftDemangler;
import ghidra.app.util.demangler.swift.datatypes.SwiftFunction;
import ghidra.program.model.lang.CompilerSpec;

# /**
 * A {@link SwiftDemangledNodeKind#Subscript} {@link SwiftNode}
 */
public class SwiftSubscriptNode extends SwiftNode {

	@Override
	public Demangled demangle(SwiftDemangler demangler) throws DemangledException {
		String name = null;
		Demangled namespace = null;
		Demangled type = null;
		Demangled labelList = null;
		String callingConvention = CompilerSpec.CALLING_CONVENTION_default;
		for (SwiftNode child : getChildren()) {
			switch (child.getKind()) {
				case Class:
					callingConvention = CompilerSpec.CALLING_CONVENTION_thiscall;
					// Fall through
				case Structure:
					namespace = child.demangle(demangler);
					name = "subscript";
					break;
				case LabelList:
					labelList = child.demangle(demangler);
					break;
				case Type:
					type = child.demangle(demangler);
					break;
				default:
					skip(child);
					break;
			}
		}
		if (name == null) {
			return getUnknown();
		}
		SwiftFunction function = new SwiftFunction(properties.mangled(),
			properties.originalDemangled(), name, namespace, callingConvention);
		if (type instanceof DemangledFunction functionType) {
			function.setType(functionType, labelList);
		}
		return function;
	}
}
