# /* ###
# * IP: GHIDRA
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# * 
# *      http://www.apache.org/licenses/LICENSE-2.0
# * 
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# */
package ghidra.program.model.pcode;

import static ghidra.program.model.pcode.AttributeId.*;
import static ghidra.program.model.pcode.ElementId.*;



import ghidra.program.model.address.Address;
import ghidra.program.model.data.DataType;

public class EquateSymbol extends HighSymbol {

	public static final int FORMAT_DEFAULT = 0;
	public static final int FORMAT_HEX = 1;
	public static final int FORMAT_DEC = 2;
	public static final int FORMAT_OCT = 3;
	public static final int FORMAT_BIN = 4;
	public static final int FORMAT_CHAR = 5;
	public static final int FORMAT_FLOAT = 6;
	public static final int FORMAT_DOUBLE = 7;

	private long value;			// Value of the equate
	private int convert;		// Non-zero if this is a conversion equate

	public EquateSymbol(HighFunction func) {
		super(func);
	}

	public EquateSymbol(long uniqueId, String nm, long val, HighFunction func, Address addr,
			long hash) {
		super(uniqueId, nm, DataType.DEFAULT, func);
		category = 1;
		value = val;
		convert = FORMAT_DEFAULT;
		DynamicEntry entry = new DynamicEntry(this, addr, hash);
		addMapEntry(entry);
	}

	public EquateSymbol(long uniqueId, int conv, long val, HighFunction func, Address addr,
			long hash) {
		super(uniqueId, "", DataType.DEFAULT, func);
		category = 1;
		value = val;
		convert = conv;
		DynamicEntry entry = new DynamicEntry(this, addr, hash);
		addMapEntry(entry);
	}

	public long getValue() {
		return value;
	}

	public int getConvert() {
		return convert;
	}

	@Override
	public void decode(Decoder decoder) throws DecoderException {
		int symel = decoder.openElement(ELEM_EQUATESYMBOL);
		decodeHeader(decoder);
		type = DataType.DEFAULT;
		convert = FORMAT_DEFAULT;
		decoder.rewindAttributes();
		String formString = null;
		for (;;) {
			int attribId = decoder.getNextAttributeId();
			if (attribId == 0) {
				break;
			}
			if (attribId == ATTRIB_FORMAT.id()) {
				formString = decoder.readString();
			}
		}
		if (formString != null) {
			if (formString.equals("hex")) {
				convert = FORMAT_HEX;
			}
			else if (formString.equals("dec")) {
				convert = FORMAT_DEC;
			}
			else if (formString.equals("char")) {
				convert = FORMAT_CHAR;
			}
			else if (formString.equals("oct")) {
				convert = FORMAT_OCT;
			}
			else if (formString.equals("bin")) {
				convert = FORMAT_BIN;
			}
			else if (formString.equals("float")) {
				convert = FORMAT_FLOAT;
			}
			else if (formString.equals("double")) {
				convert = FORMAT_DOUBLE;
			}
		}
		int valel = decoder.openElement(ELEM_VALUE);
		value = decoder.readUnsignedInteger(ATTRIB_CONTENT);
		decoder.closeElement(valel);
		decoder.closeElement(symel);
	}

	@Override
	public void encode(Encoder encoder) throws IOException {
		encoder.openElement(ELEM_EQUATESYMBOL);
		encodeHeader(encoder);
		if (convert != 0) {
			String formString = "hex";
			if (convert == FORMAT_HEX) {
				// Most common case
			}
			else if (convert == FORMAT_DEC) {
				formString = "dec";
			}
			else if (convert == FORMAT_OCT) {
				formString = "oct";
			}
			else if (convert == FORMAT_BIN) {
				formString = "bin";
			}
			else if (convert == FORMAT_CHAR) {
				formString = "char";
			}
			else if (convert == FORMAT_FLOAT) {
				formString = "float";
			}
			else if (convert == FORMAT_DOUBLE) {
				formString = "double";
			}

			encoder.writeString(ATTRIB_FORMAT, formString);
		}
		encoder.openElement(ELEM_VALUE);
		encoder.writeUnsignedInteger(ATTRIB_CONTENT, value);
		encoder.closeElement(ELEM_VALUE);
		encoder.closeElement(ELEM_EQUATESYMBOL);
	}

    # /**
	 * Determine what format a given equate name is in.
	 * Integer format conversions are stored using an Equate object, where the name of the equate
	 * is the actual conversion String. So the only way to tell what kind of conversion is being performed
	 * is by examining the name of the equate.  The format code of the conversion is returned, or if
	 * the name is not a conversion,  FORMAT_DEFAULT is returned indicating a normal String equate.
	 * @param nm is the name of the equate
	 * @param val is the value being equated
	 * @return the format code for the conversion or FORMAT_DEFAULT if not a conversion
	 */
	public static int convertName(String nm, long val) {
		int pos = 0;
		char firstChar = nm.charAt(pos++);
		if (firstChar == '-') {
			if (nm.length() > pos) {
				firstChar = nm.charAt(pos++);
			}
			else {
				return FORMAT_DEFAULT;			// Bad equate name, just print number normally
			}
		}
		switch (firstChar) {
			case '\'':
			case '"':
				return FORMAT_CHAR;
			case '0':
				if (nm.length() >= (pos + 1) && nm.charAt(pos) == 'x') {
					return FORMAT_HEX;
				}
			case '1':
			case '2':
			case '3':
			case '4':
			case '5':
			case '6':
			case '7':
			case '8':
			case '9':
				break;
			case 'A':
			case 'B':
			case 'C':
			case 'D':
			case 'E':
			case 'F':
				if (nm.length() >= 3 && nm.charAt(2) == 'h') {
					char secondChar = nm.charAt(1);
					if (secondChar >= '0' && secondChar <= '9') {
						return FORMAT_CHAR;
					}
					if (secondChar >= 'A' && secondChar <= 'F') {
						return FORMAT_CHAR;
					}
				}
				return FORMAT_DEFAULT;
			default:
				return FORMAT_DEFAULT;					// Don't treat as a conversion
		}
		switch (nm.charAt(nm.length() - 1)) {
			case 'b':
				return FORMAT_BIN;
			case 'o':
				return FORMAT_OCT;
			case '\'':
			case '"':
			case 'h':									// The 'h' encoding is used for "unrepresentable" characters
				return FORMAT_CHAR;
		}
		return FORMAT_DEC;
	}
}
