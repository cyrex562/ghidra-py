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
package ghidra.program.util;

import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Program;

# /**
# * The <CODE>IndentFieldLocation</CODE> class contains specific location information
# * within the indent field of a CodeUnitLocation object.
# */
public class IndentFieldLocation extends CodeUnitLocation {
    # /**
	 * Construct a new IndentFieldLocation object.
	 * 
	 * @param program the program of the location
	 * @param addr address of the location; should not be null
	 * fragment by its hierarchy names; this parameter may be null
	 * @param componentPath array of indexes for each nested data component; the
	 */
	public IndentFieldLocation(Program program, Address addr, int[] componentPath) {
		super(program, addr, componentPath, null, 0, 0, 0);
	}

    # /**
	 * Default constructor needed for restoring
	 * an indent field location from XML
	 */
	public IndentFieldLocation() {
	}
}
