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
 * Debug header for various, yet-to-be-determined debug structures.  {@link RvaVaDebugHeader}, an
 * extension of this class, is used for PData and XData within {@link DebugData}.
 */
public class DebugHeader {

	private long headerVersion;
	private long headerLength;
	private long dataLength;

	/**
	 * Returns the version of the header.
	 * @return the header version.
	 */
	public long getHeaderVersion() {
		return headerVersion;
	}

	/**
	 * Returns the header length.
	 * @return the header length.
	 */
	public long getHeaderLength() {
		return headerLength;
	}

	/**
	 * Returns the data length.
	 * @return the data length.
	 */
	public long getDataLength() {
		return dataLength;
	}

	/**
	 * Deserializes the {@link DebugHeader} information from a {@link PdbByteReader}
	 * @param reader the {@link PdbByteReader} from which to parse the data.
	 * @throws PdbException upon problem parsing the data.
	 */
	public void deserialize(PdbByteReader reader) throws PdbException {
		headerVersion = reader.parseUnsignedIntVal();
		headerLength = reader.parseUnsignedIntVal();
		dataLength = reader.parseUnsignedIntVal();
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

	/**
	 * Dumps this class to Writer.  This package-protected method is for debugging only
	 * @param writer the writer
	 * @throws IOException upon issue with writing to the writer
	 */
	void dump(Writer writer) throws IOException {
		PdbReaderUtils.dumpHead(writer, this);
		dumpInternal(writer);
		PdbReaderUtils.dumpTail(writer, this);
	}

	protected void dumpInternal(Writer writer) throws IOException {
		writer.write(String.format("headerVersion: 0X%08X\n", headerVersion));
		writer.write(String.format("headerLength: 0X%08X\n", headerLength));
		writer.write(String.format("dataLength: 0X%08X\n", dataLength));
	}

}
