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
package ghidra.file.formats.ext4;



import ghidra.app.util.bin.*;
import ghidra.program.model.data.*;
import ghidra.util.exception.DuplicateNameException;

public class Ext4XattrIbodyHeader implements StructConverter {
	static final int SIZEOF = 4;

	private int h_magic;
	
	public Ext4XattrIbodyHeader(ByteProvider provider) throws IOException {
		this( new BinaryReader( provider, true ) );
	}
	
	public Ext4XattrIbodyHeader(BinaryReader reader) throws IOException {
		h_magic = reader.readNextInt();
	}
	
	
	
	public int getH_magic() {
		return h_magic;
	}

	@Override
	public DataType toDataType() throws DuplicateNameException, IOException {
		Structure structure = new StructureDataType("ext4_xattr_ibody_header", 0);
		structure.add(DWORD, "h_magic", null);
		return structure;
	}

	public boolean isValid() {
		return h_magic == Ext4Constants.EXT4_XATTR_MAGIC;
	}

}
