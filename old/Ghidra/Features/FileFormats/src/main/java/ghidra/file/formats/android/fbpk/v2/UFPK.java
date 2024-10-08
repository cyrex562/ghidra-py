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
package ghidra.file.formats.android.fbpk.v2;



import ghidra.app.util.bin.BinaryReader;
import ghidra.app.util.bin.StructConverter;
import ghidra.file.formats.android.fbpk.FBPK_Constants;
import ghidra.program.model.data.DataType;
import ghidra.program.model.data.Structure;
import ghidra.program.model.data.StructureDataType;
import ghidra.util.exception.DuplicateNameException;

public class UFPK implements StructConverter {
	private String magic;
	private int unknown1;
	private String string1;

	public UFPK(BinaryReader reader) throws IOException {
		magic = reader.readNextAsciiString(FBPK_Constants.UFPK.length());
		unknown1 = reader.readNextInt();
		string1 = reader.readNextAsciiString(FBPK_Constants.V2_UFPK_STRING1_MAX_LENGTH);
	}

	public String getMagic() {
		return magic;
	}

	public int getUnknown1() {
		return unknown1;
	}

	public String getString1() {
		return string1;
	}

	@Override
	public DataType toDataType() throws DuplicateNameException, IOException {
		Structure struct = new StructureDataType(UFPK.class.getSimpleName(), 0);
		struct.add(STRING, magic.length(), "magic", null);
		struct.add(DWORD, "unknown1", null);
		struct.add(STRING, FBPK_Constants.V2_UFPK_STRING1_MAX_LENGTH, "string2", null);
		return struct;
	}

}
