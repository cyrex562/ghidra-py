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
package ghidra.pcodeCPort.slghsymbol;

import ghidra.pcodeCPort.slghpatexpress.ConstantValue;
import ghidra.pcodeCPort.slghpatexpress.PatternExpression;
import ghidra.sleigh.grammar.Location;

// Behaves like constant 0 pattern
public abstract class PatternlessSymbol extends SpecificSymbol {

	private ConstantValue patexp;

	@Override
	public PatternExpression getPatternExpression() {
		return patexp;
	}

	// The constructor must explicitly build the ConstantValue. It is not explicitly
	// decoded (or encoded)
	public PatternlessSymbol(Location location) {
		super(location);
		patexp = new ConstantValue(location, 0);
		patexp.layClaim();
	}

	public PatternlessSymbol(Location location, String nm) {
		super(location, nm);
		patexp = new ConstantValue(location, 0);
		patexp.layClaim();
	}

	@Override
	public void dispose() {
		PatternExpression.release(patexp);
	}
}
