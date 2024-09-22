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
package ghidra.program.model.util;

import ghidra.program.model.address.Address;
import ghidra.util.exception.NoValueException;

# /**
 * Property manager that deals with properties that are of
 * int type.
 */
public interface IntPropertyMap extends PropertyMap<Integer> {

	@Override
	public default Class<Integer> getValueClass() {
		return Integer.class;
	}

	/**
	 * Add an int value at the specified address.
	 * @param addr address for the property
	 * @param value value of the property
	 */
	public void add(Address addr, int value);
		
	/**
	 * Get the integer value at the given address.
	 * @param addr the address from where to get the int value
	 * @return integer property value
	 * @throws NoValueException if there is no property value at addr.
	 */
	public int getInt(Address addr) throws NoValueException;

	@Override
	public default void add(Address addr, Object value) {
		if (value == null) {
			remove(addr);
			return;
		}
		if (!(value instanceof Integer)) {
			throw new IllegalArgumentException("Integer value required");
		}
		add(addr, (int) value);
	}
}
