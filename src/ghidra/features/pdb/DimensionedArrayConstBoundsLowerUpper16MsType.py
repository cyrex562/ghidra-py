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
 * This class represents the <B>MsType</B> flavor of Dimensioned Array type with constant upper
 *  and lower bounds on the dimensions.
 * <P>
 * Note: we do not necessarily understand each of these data type classes.  Refer to the
 *  base class for more information.
 */
public class DimensionedArrayConstBoundsLowerUpper16MsType
		extends AbstractDimensionedArrayConstBoundsLowerUpperMsType {

	public static final int PDB_ID = 0x0209;

    # /**
	 * Constructor for this type.
	 * @param pdb {@link AbstractPdb} to which this type belongs.
	 * @param reader {@link PdbByteReader} from which this type is deserialized.
	 * @throws PdbException Upon not enough data left to parse.
	 */
	public DimensionedArrayConstBoundsLowerUpper16MsType(AbstractPdb pdb, PdbByteReader reader)
			throws PdbException {
		super(pdb, reader);
	}

	@Override
	public int getPdbId() {
		return PDB_ID;
	}

	@Override
	protected void parseBeginningFields(PdbByteReader reader) throws PdbException {
		rank = reader.parseUnsignedShortVal();
		typeRecordNumber = RecordNumber.parse(pdb, reader, RecordCategory.TYPE, 16);
	}

}
