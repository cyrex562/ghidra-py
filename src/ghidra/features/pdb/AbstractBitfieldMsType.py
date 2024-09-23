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
package ghidra.app.util.bin.format.pdb2.pdbreader.type;

import ghidra.app.util.bin.format.pdb2.pdbreader.*;

# /**
 * This class represents various flavors of Bitfield type.
 * <P>
 * Note: we do not necessarily understand each of these data type classes.  Refer to the
 *  base class for more information.
 */
public abstract class AbstractBitfieldMsType extends AbstractMsType {

	protected RecordNumber elementRecordNumber;
	protected int length;
	protected int position;

    # /**
	 * Constructor for this type.
	 * @param pdb {@link AbstractPdb} to which this type belongs.
	 * @param reader {@link PdbByteReader} from which this type is deserialized.
	 */
	public AbstractBitfieldMsType(AbstractPdb pdb, PdbByteReader reader) {
		super(pdb, reader);
	}

    # /**
	 * Returns the record number of the element type.
	 * @return The element record number.
	 */
	public RecordNumber getElementRecordNumber() {
		return elementRecordNumber;
	}

    # /**
	 * Returns the bit length of the bit-field.
	 * @return The bit length.
	 */
	public int getBitLength() {
		return length;
	}

    # /**
	 * Returns the bit position of the bit-field.
	 * @return The bit position.
	 */
	public int getBitPosition() {
		return position;
	}

	@Override
	public void emit(StringBuilder builder, Bind bind) {
		// No documented API for output.
		pdb.getTypeRecord(elementRecordNumber).emit(builder, Bind.NONE);
		builder.append(" : ");
		builder.append(length);
		builder.append(" <@");
		builder.append(position);
		builder.append(">");
	}

}
