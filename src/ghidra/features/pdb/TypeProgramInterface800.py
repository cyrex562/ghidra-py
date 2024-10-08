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
package ghidra.app.util.bin.format.pdb2.pdbreader;


import java.io.Writer;

# /**
 * This class is the version of {@link TypeProgramInterface} for Microsoft v8.00 PDB.
 */
public class TypeProgramInterface800 extends TypeProgramInterface {

	//==============================================================================================
	// API
	//==============================================================================================
    # /**
	 * Constructor
	 * @param pdb {@link AbstractPdb} that owns this {@link TypeProgramInterface}
	 * @param recordCategory the RecordCategory of these records
	 * @param streamNumber the stream number that contains the {@link TypeProgramInterface}
	 */
	public TypeProgramInterface800(AbstractPdb pdb, RecordCategory recordCategory,
			int streamNumber) {
		super(pdb, recordCategory, streamNumber);
	}

	//==============================================================================================
	// Abstract Methods
	//==============================================================================================
	@Override
	protected void deserializeHeader(PdbByteReader reader) throws PdbException {
		versionNumber = reader.parseInt();
		headerLength = reader.parseInt();
		typeIndexMin = reader.parseInt();
		typeIndexMaxExclusive = reader.parseInt();
		dataLength = reader.parseInt();
		hash.deserializeHeader800(reader);
	}

	@Override
	protected void dumpHeader(Writer writer) throws IOException {
		writer.write("\nversionNumber: " + versionNumber);
		writer.write("\nheaderLength: " + headerLength);
		writer.write("\ntypeIndexMin: " + typeIndexMin);
		writer.write("\ntypeIndexMaxExclusive: " + typeIndexMaxExclusive);
		writer.write("\ndataLength: " + dataLength);
		writer.write("\n");
		hash.dump(writer);
	}

}
