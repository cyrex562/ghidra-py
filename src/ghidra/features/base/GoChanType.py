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
package ghidra.app.util.bin.format.golang.rtti.types;


import java.util.Set;

import ghidra.app.util.bin.format.golang.structmapping.*;
import ghidra.program.model.data.*;
import ghidra.util.Msg;

# /**
 * A {@link GoType} structure that defines a go channel
 */
@StructureMapping(structureName = {"runtime.chantype", "internal/abi.ChanType"})
public class GoChanType extends GoType {

	@FieldMapping
	@MarkupReference("getElement")
	private long elem;

	@FieldMapping
	private long dir;

	public GoChanType() {
		// empty
	}

	/**
	 * Returns a reference to the {@link GoType} that defines the elements this channel uses
	 * @return reference to the {@link GoType} that defines the elements this channel uses
	 * @throws IOException if error reading type
	 */
	@Markup
	public GoType getElement() throws IOException {
		return programContext.getGoType(elem);
	}

	@Override
	public DataType recoverDataType() throws IOException {
		GoType chanGoType = programContext.getChanGoType();
		if (chanGoType == null) {
			// if we couldn't find the underlying/hidden runtime.hchan struct type, just return
			// a void*
			return programContext.getDTM().getPointer(null);
		}

		DataType chanDT = programContext.getRecoveredType(chanGoType);
		Pointer ptrChanDt = programContext.getDTM().getPointer(chanDT);
		if (typ.getSize() != ptrChanDt.getLength()) {
			Msg.warn(this, "Size mismatch between chan type and recovered type");
		}
		TypedefDataType typedef =
			new TypedefDataType(programContext.getRecoveredTypesCp(getPackagePathString()),
				getUniqueTypename(), ptrChanDt, programContext.getDTM());
		return typedef;

	}

	@Override
	public boolean discoverGoTypes(Set<Long> discoveredTypes) throws IOException {
		if (!super.discoverGoTypes(discoveredTypes)) {
			return false;
		}
		GoType element = getElement();
		if (element != null) {
			element.discoverGoTypes(discoveredTypes);
		}
		return true;
	}

}
