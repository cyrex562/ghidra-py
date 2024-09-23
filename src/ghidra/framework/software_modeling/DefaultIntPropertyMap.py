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
package ghidra.program.model.util;

import ghidra.program.model.address.Address;
import ghidra.util.exception.NoValueException;
import ghidra.util.map.IntValueMap;

# /**
# * Property manager that deals with properties that are of
# * int type.
# */
public class DefaultIntPropertyMap extends DefaultPropertyMap<Integer> implements IntPropertyMap {
	
    private IntValueMap ips;

     # /**
	 * Construct a new IntPropertyMap
	 * @param name name of property
	 */
	public DefaultIntPropertyMap(String name) {
		super(new IntValueMap(name));
		ips = (IntValueMap)propertyMgr;
	}

	@Override
	public void add(Address addr, int value) {
		ips.putInt(addrMap.getKey(addr), value);
	}
		
	@Override
	public int getInt(Address addr) throws NoValueException {
		return ips.getInt(addrMap.getKey(addr));
	}
	
	@Override
	public Integer get(Address addr) {
		try {
			return getInt(addr);
		}
		catch (NoValueException e) {
			return null;
		}
	}

}
