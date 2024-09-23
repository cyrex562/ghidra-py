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
# /* Generated by Together */

package ghidra.program.util;

import java.util.Objects;

import ghidra.framework.options.SaveState;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Program;

# /**
# * The <CODE>FieldNameFieldLocation</CODE> class provides specific information about the Function
# * Name field within a program location.
# */
public class FieldNameFieldLocation extends CodeUnitLocation {

	private String fieldName;

    # /**
	 * Construct a new FieldNameFieldLocation.
	 *
	 * @param program the program of the location
	 * @param addr the address of the code unit
	 * @param componentPath if not null, it is the array of indexes that point to a specific data
	 * type inside of another data type
	 * @param fieldName the field name
	 * @param charOffset the character position within the field name for this location.
	 */
	public FieldNameFieldLocation(Program program, Address addr, int[] componentPath,
			String fieldName, int charOffset) {

		super(program, addr, componentPath, 0, 0, charOffset);

		this.fieldName = fieldName;
	}

    # /**
	 * Default constructor needed for restoring a field name location from XML
	 */
	public FieldNameFieldLocation() {
	}

    # /**
	 * Returns the field name of this location.
	 * @return the name.
	 */
	public String getFieldName() {
		return fieldName;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + ((fieldName == null) ? 0 : fieldName.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) {
			return true;
		}
		if (!super.equals(obj)) {
			return false;
		}
		if (getClass() != obj.getClass()) {
			return false;
		}
		FieldNameFieldLocation other = (FieldNameFieldLocation) obj;
		if (!Objects.equals(fieldName, other.fieldName)) {
			return false;
		}
		return true;
	}

	@Override
	public void saveState(SaveState obj) {
		super.saveState(obj);
		obj.putString("_FIELD_NAME", fieldName);
	}

	@Override
	public void restoreState(Program p, SaveState obj) {
		super.restoreState(p, obj);
		fieldName = obj.getString("_FIELD_NAME", null);
	}

	@Override
	public String toString() {
		return super.toString() + ", Field Name = " + fieldName;
	}
}
