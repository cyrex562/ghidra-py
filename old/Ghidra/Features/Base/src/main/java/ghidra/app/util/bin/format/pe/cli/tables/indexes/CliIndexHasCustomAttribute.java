/* ###
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
package ghidra.app.util.bin.format.pe.cli.tables.indexes;



import ghidra.app.util.bin.BinaryReader;
import ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata;
import ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable;
import ghidra.program.model.data.DataType;
import ghidra.util.exception.InvalidInputException;

public class CliIndexHasCustomAttribute {
	private static final int bitsUsed = 5;
	private static final CliTypeTable tables[] = { CliTypeTable.MethodDef, CliTypeTable.Field, CliTypeTable.TypeRef, CliTypeTable.TypeDef, CliTypeTable.Param, 
		CliTypeTable.InterfaceImpl, CliTypeTable.MemberRef, CliTypeTable.Module, null, CliTypeTable.Property, CliTypeTable.Event, CliTypeTable.StandAloneSig,
		CliTypeTable.ModuleRef, CliTypeTable.TypeSpec, CliTypeTable.Assembly, CliTypeTable.AssemblyRef, CliTypeTable.File, CliTypeTable.ExportedType, 
		CliTypeTable.ManifestResource }; // TODO: null should be TableName.Permission, but this is not well-described in the standard
	
	public static DataType toDataType(CliStreamMetadata stream) {
		return CliCodedIndexUtils.toDataType(stream, bitsUsed, tables);
	}
	
	public static int getRowIndex(int codedIndex) {
		return CliCodedIndexUtils.getRowIndex(codedIndex, bitsUsed);
	}
	
	public static CliTypeTable getTableName(int codedIndex) throws InvalidInputException {
		return CliCodedIndexUtils.getTableName(codedIndex, bitsUsed, tables);
	}
	
	public static int readCodedIndex(BinaryReader reader, CliStreamMetadata stream) throws IOException {
		return CliCodedIndexUtils.readCodedIndex(reader, stream, bitsUsed, tables);
	}

}
