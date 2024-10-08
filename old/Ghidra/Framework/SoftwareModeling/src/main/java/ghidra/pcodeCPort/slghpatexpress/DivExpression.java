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
package ghidra.pcodeCPort.slghpatexpress;

import static ghidra.pcode.utils.SlaFormat.*;



import generic.stl.VectorSTL;
import ghidra.pcodeCPort.utils.MutableInt;
import ghidra.program.model.pcode.Encoder;
import ghidra.sleigh.grammar.Location;

public class DivExpression extends BinaryExpression {

	public DivExpression(Location location) {
		super(location);
	}

	public DivExpression(Location location, PatternExpression l, PatternExpression r) {
		super(location, l, r);
	}

	@Override
	public long getSubValue(VectorSTL<Long> replace, MutableInt listpos) {
		long leftval = getLeft().getSubValue(replace, listpos); // Must be left first
		long rightval = getRight().getSubValue(replace, listpos);
		return leftval / rightval;
	}

	@Override
	public void encode(Encoder encoder) throws IOException {
		encoder.openElement(ELEM_DIV_EXP);
		super.encode(encoder);
		encoder.closeElement(ELEM_DIV_EXP);
	}

}
