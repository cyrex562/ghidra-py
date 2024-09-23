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
package ghidra.file.formats.android.oat.tlt;


import java.util.ArrayList;
import java.util.List;

import ghidra.app.util.bin.BinaryReader;
import ghidra.program.model.data.*;
import ghidra.util.exception.DuplicateNameException;

# /**
 * <a href="https://android.googlesource.com/platform/art/+/nougat-release/runtime/type_lookup_table.h">nougat-release/runtime/type_lookup_table.h</a>
 */
public class TypeLookupTable_Nougat extends TypeLookupTable {

	private int dex_file_;
	private int mask_;
	private int entries_;
	private int owns_entries_;

	private List<TypeLookupTableEntry> entryList = new ArrayList<TypeLookupTableEntry>();

	public TypeLookupTable_Nougat(BinaryReader reader) throws IOException {
		dex_file_ = reader.readNextInt();
		mask_ = reader.readNextInt();
		entries_ = reader.readNextInt();
		owns_entries_ = reader.readNextInt();
	}

	public int getDexFile() {
		return dex_file_;
	}

	public int getMask() {
		return mask_;
	}

	public int getEntries() {
		return entries_;
	}

    # /**
	 * owns_entries_ specifies if the lookup table owns the entries_ array.
	 */
	public boolean isOwnsEntries() {
		return owns_entries_ == 0;
	}

	public List<TypeLookupTableEntry> getEntryList() {
		return entryList;
	}

	@Override
	public DataType toDataType() throws DuplicateNameException, IOException {
		Structure structure = new StructureDataType(
			TypeLookupTable_Nougat.class.getSimpleName() + "_" + entryList.size(), 0);
		structure.add(DWORD, "dex_file_", null);
		structure.add(DWORD, "mask_", null);
		structure.add(DWORD, "entries_", null);
		structure.add(DWORD, "owns_entries_", null);
		structure.setCategoryPath(new CategoryPath("/oat"));
		return structure;
	}

}
