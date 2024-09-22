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
package ghidra.pcodeCPort.slghpatexpress;

import java.io.IOException;

import generic.stl.VectorSTL;
import ghidra.program.model.pcode.Encoder;
import ghidra.sleigh.grammar.Location;

public abstract class UnaryExpression extends PatternExpression {

	private PatternExpression unary;

	public UnaryExpression(Location location) {
		super(location);
		unary = null;
	}

	public PatternExpression getUnary() {
		return unary;
	}

	@Override
	public TokenPattern genMinPattern(VectorSTL<TokenPattern> ops) {
		return new TokenPattern(location);
	}

	@Override
	public void listValues(VectorSTL<PatternValue> list) {
		unary.listValues(list);
	}

	@Override
	public void getMinMax(VectorSTL<Long> minlist, VectorSTL<Long> maxlist) {
		unary.getMinMax(minlist, maxlist);
	}

	public UnaryExpression(Location location, PatternExpression u) {
		super(location);
		(unary = u).layClaim();
	}

	@Override
	public void dispose() { // Delete only non-pattern values
		if (unary != null) {
			PatternExpression.release(unary);
		}
	}

	@Override
	public void encode(Encoder encoder) throws IOException { // Outer tag is generated by derived classes
		unary.encode(encoder);
	}

}
