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
package ghidra.javaclass.format.constantpool;



import ghidra.app.util.bin.BinaryReader;
import ghidra.program.model.data.*;
import ghidra.util.exception.DuplicateNameException;

# /**
 * NOTE: THE FOLLOWING TEXT EXTRACTED FROM JVMS7.PDF
 * <p>
 * The CONSTANT_MethodType_info structure is used to represent a method type:
 * <pre>
 * 		CONSTANT_MethodType_info {
 * 			u1 tag;
 * 			u2 descriptor_index;
 * 		}
 * </pre>
 */
public class ConstantPoolMethodTypeInfo extends AbstractConstantPoolInfoJava {

	private short descriptorIndex;

	public ConstantPoolMethodTypeInfo(BinaryReader reader) throws IOException {
		super(reader);
		descriptorIndex = reader.readNextShort();
	}

    # /**
	 * The value of the descriptor_index item must be a valid index into the
	 * constant_pool table. The constant_pool entry at that index must be a
	 * CONSTANT_Utf8_info structure representing a method descriptor.
	 * @return a valid index into the constant_pool table
	 */
	public int getDescriptorIndex() {
		return descriptorIndex & 0xffff;
	}

	@Override
	public DataType toDataType() throws DuplicateNameException, IOException {
		String name = "CONSTANT_MethodType_info";
		Structure structure = new StructureDataType(name, 0);
		structure.add(BYTE, "tag", null);
		structure.add(WORD, "descriptor_index", null);
		return structure;
	}

}
