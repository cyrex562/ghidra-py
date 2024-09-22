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

import java.io.IOException;
import java.util.Set;

import ghidra.app.util.bin.format.golang.rtti.GoString;
import ghidra.app.util.bin.format.golang.structmapping.StructureMapping;
import ghidra.app.util.bin.format.golang.structmapping.StructureReader;
import ghidra.program.model.data.*;
import ghidra.util.Msg;

# /**
 * WARNING: tricky code / class layout here!
 * <p>
 * To coerce java inheritance and structmapping features to match the layout of go rtti type structs,
 * this class is constructed strangely.
 * <p>
 * {@link GoType} structure that defines a built-in primitive type.
 */
@StructureMapping(structureName = {"runtime._type", "internal/abi.Type"})
public class GoPlainType extends GoType implements StructureReader<GoType> {
	@Override
	public void readStructure() throws IOException {
		this.typ = context.getDataTypeMapper().readStructure(GoBaseType.class, context.getReader());
	}

	@Override
	public DataType recoverDataType() throws IOException {
		DataTypeManager dtm = programContext.getDTM();
		DataType dt = switch (typ.getKind()) {
			case Bool -> BooleanDataType.dataType;
			case Float32 -> AbstractFloatDataType.getFloatDataType(32 / 8, null);
			case Float64 -> AbstractFloatDataType.getFloatDataType(64 / 8, null);
			case Int -> AbstractIntegerDataType.getSignedDataType(programContext.getPtrSize(), dtm);
			case Int8 -> AbstractIntegerDataType.getSignedDataType(8 / 8, null);
			case Int16 -> AbstractIntegerDataType.getSignedDataType(16 / 8, null);
			case Int32 -> AbstractIntegerDataType.getSignedDataType(32 / 8, null);
			case Int64 -> AbstractIntegerDataType.getSignedDataType(64 / 8, null);
			case Uint -> AbstractIntegerDataType.getUnsignedDataType(programContext.getPtrSize(),
					dtm);
			case Uint8 -> AbstractIntegerDataType.getUnsignedDataType(8 / 8, null);
			case Uint16 -> AbstractIntegerDataType.getUnsignedDataType(16 / 8, null);
			case Uint32 -> AbstractIntegerDataType.getUnsignedDataType(32 / 8, null);
			case Uint64 -> AbstractIntegerDataType.getUnsignedDataType(64 / 8, null);
			case Uintptr -> AbstractIntegerDataType.getUnsignedDataType(programContext.getPtrSize(),
					dtm);
			case String -> programContext.getStructureDataType(GoString.class);
			case UnsafePointer -> dtm.getPointer(null);
			default -> null;
		};
		if (dt == null) {
			dt = super.recoverDataType();
		}

		String name = getUniqueTypename();
		if (!dt.getName().equalsIgnoreCase(name)) {
			dt = new TypedefDataType(programContext.getRecoveredTypesCp(getPackagePathString()),
				name, dt, dtm);
		}
		if (dt.getLength() != typ.getSize()) {
			Msg.warn(this,
				"Recovered golang data type size mismatch: %s, %d != %d".formatted(getDebugId(),
					typ.getSize(), dt.getLength()));
		}
		return dt;
	}

	@Override
	public boolean discoverGoTypes(Set<Long> discoveredTypes) throws IOException {
		return super.discoverGoTypes(discoveredTypes);
	}


}
