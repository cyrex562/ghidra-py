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
package ghidra.app.util.bin.format.pdb2.pdbreader.msf;



import ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader;
import ghidra.app.util.bin.format.pdb2.pdbreader.PdbException;
import ghidra.util.exception.CancelledException;

# /**
 * This is the v700 of {@link MsfDirectoryStream}.  It is essentially no different than
 *  an {@link MsfStream}.
 * @see MsfDirectoryStream
 */
class MsfDirectoryStream700 extends MsfDirectoryStream {

	//==============================================================================================
	// Package-Protected Internals
	//==============================================================================================
    # /**
	 * Constructor.  Sets the byte length of the Stream to -1.  This method is used when the
	 *  Stream knows/reads its length
	 * @param msf the {@link Msf} to which the Stream belongs
	 */
	MsfDirectoryStream700(Msf msf) {
		super(msf);
	}

    # /**
	 * Deserializes Stream information from the bytes parameter starting at the index offset
	 *  and uses it to provide necessary information for the Stream to be usable.
	 *  The information from the deserialization of the byte parameter then points to additional
	 *  {@link Msf} pages that need to be read as a subStream and deserialized to create
	 *  the {@link MsfDirectoryStream700}.
	 *  <P>
	 *  Generally, deserialization is part of the step of loading the Stream information from
	 *  persistent storage (disk).
	 * @param reader {@link PdbByteReader} from which to parse the information
	 * @throws IOException on file seek or read, invalid parameters, bad file configuration, or
	 *  inability to read required bytes
	 * @throws PdbException upon not enough data left to parse
	 * @throws CancelledException upon user cancellation
	 */
	@Override
	void deserializeStreamInfo(PdbByteReader reader)
			throws IOException, PdbException, CancelledException {

		// Parse the length of the overall (larger) stream.
		deserializeStreamLengthAndMapTableAddress(reader);
		// Calculate the length of the subStream which contains all of the page numbers necessary
		// for the overall (larger) stream and create a subStream with this calculated length.
		int subStreamLength =
			Msf.floorDivisionWithLog2Divisor(streamLength, msf.getLog2PageSize()) *
				msf.getPageNumberSize();

		MsfStream subStream = new MsfStream(msf, subStreamLength);
		// Parse the page numbers of the subStream.
		subStream.deserializePageNumbers(reader);
		// Now read the whole subStream, creating a new byte array.
		byte[] bytes = subStream.read(0, subStreamLength);
		PdbByteReader pageNumberReader = new PdbByteReader(bytes);
		// Next parse the page numbers for the overall (larger) stream from this new byte array
		// that was read from the subStream.
		deserializePageNumbers(pageNumberReader);
		// The overall (larger) stream has now been set up with the overall stream length
		// and its page numbers parsed.
	}

}
