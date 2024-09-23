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
package ghidra.app.util.bin.format.macho.commands.codesignature;



import ghidra.app.util.bin.BinaryReader;
import ghidra.app.util.bin.StructConverter;
import ghidra.app.util.bin.format.macho.MachConstants;
import ghidra.program.model.data.*;
import ghidra.util.exception.DuplicateNameException;

/**
 * Represents a CS_BlobIndex structure
 * 
 * @see <a href="https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/kern/cs_blobs.h">osfmk/kern/cs_blobs.h</a> 
 */
public class CodeSignatureBlobIndex implements StructConverter {

	private int type;
	private long offset;

	/**
	 * Creates a new {@link CodeSignatureBlobIndex}
	 * 
	 * @param reader A {@link BinaryReader} positioned at the start of the structure
	 * @throws IOException if there was an IO-related problem creating the structure
	 */
	public CodeSignatureBlobIndex(BinaryReader reader) throws IOException {
		type = reader.readNextInt();
		offset = reader.readNextUnsignedInt();
	}

	/**
	 * {@return the type}
	 */
	public int getType() {
		return type;
	}

	/**
	 * {@return the offset}
	 */
	public long getOffset() {
		return offset;
	}

	@Override
	public DataType toDataType() throws DuplicateNameException, IOException {
		StructureDataType struct = new StructureDataType("CS_BlobIndex", 0);
		struct.add(DWORD, "type", "type of entry");
		struct.add(DWORD, "offset", "offset of entry");
		struct.setCategoryPath(new CategoryPath(MachConstants.DATA_TYPE_CATEGORY));
		return struct;
	}

}
