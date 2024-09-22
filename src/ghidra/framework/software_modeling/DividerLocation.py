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
# /* Generated by Together */

package ghidra.program.util;

import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Program;

# /**
 * <CODE>DividerLocation</CODE> provides information about the location 
 * (within a program) of an object that represents some kind of a separation.
 */
public class DividerLocation extends ProgramLocation {

	/**
	  * Create a new DividerLocation.
	  * 
	  * @param program the program of the location
	  * @param addr address of bookmark
	  * @param groupPath object that uniquely identifies a module or fragment
	  * by its hierarchy names; this parameter may be null
	  * @param charOffset character position of the location
	  */
	public DividerLocation(Program program, Address addr, GroupPath groupPath, int charOffset) {
		super(program, addr, addr, null, null, 0, 0, charOffset);
	}

	/**
	 * Default constructor needed for restoring
	 * a program location from XML
	 */
	public DividerLocation() {
	}

}
