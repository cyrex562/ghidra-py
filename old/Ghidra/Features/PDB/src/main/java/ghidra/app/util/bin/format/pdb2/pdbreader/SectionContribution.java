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
package ghidra.app.util.bin.format.pdb2.pdbreader;



/**
 * This class represents Section Contribution component of a PDB file.  This class is only
 *  suitable for reading; not for writing or modifying a PDB.
 *  <P>
 *  We have intended to implement according to the Microsoft PDB API (source); see the API for
 *   truth.
 */
public abstract class SectionContribution {

	//==============================================================================================
	// Internals
	//==============================================================================================
	protected int isect; // unsigned 16-bit
	protected int offset; // signed 32-bit
	protected int length; // signed 32-bit
	protected int imod; // unsigned 16-bit

	protected long characteristics; // unsigned 32-bit

	protected long dataCrc; // unsigned 32-bit
	protected long relocationCrc; // unsigned 32-bit
	protected long unknownSectionContributionField; // unknown field for SCV1400

	//==============================================================================================
	// API
	//==============================================================================================
	public SectionContribution() {
	}

	public int getSection() {
		return isect;
	}

	public int getOffset() {
		return offset;
	}

	public int getLength() {
		return length;
	}

	public int getModule() {
		return imod;
	}

	@Override
	public String toString() {
		StringWriter writer = new StringWriter();
		try {
			dump(writer);
			return writer.toString();
		}
		catch (IOException e) {
			return "Issue in " + getClass().getSimpleName() + " toString(): " + e.getMessage();
		}
	}

	//==============================================================================================
	// Abstract Methods
	//==============================================================================================
	/**
	 * Deserializes the Section Contribution
	 * @param reader {@link PdbByteReader} from which to deserialize the data
	 * @throws PdbException upon not enough data left to parse
	 */
	abstract void deserialize(PdbByteReader reader) throws PdbException;

	/**
	 * Dumps the SectionContribution.  This method is for debugging only
	 * @param writer the writer
	 * @throws IOException upon issue with writing to the writer
	 */
	abstract void dumpInternals(Writer writer) throws IOException;

	//==============================================================================================
	// Package-Protected Internals
	//==============================================================================================
	/**
	 * Dumps the Section Contribution.  This method is for debugging only
	 * @param writer the writer
	 * @throws IOException upon issue with writing to the writer
	 */
	void dump(Writer writer) throws IOException {
		PdbReaderUtils.dumpHead(writer, this);
		dumpInternals(writer);
		PdbReaderUtils.dumpTail(writer, this);
	}

}
