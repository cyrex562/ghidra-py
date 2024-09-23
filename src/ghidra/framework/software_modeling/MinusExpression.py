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
# /*
# * Created on Feb 8, 2005
# *
# */
package ghidra.app.plugin.processors.sleigh.expression;

import ghidra.app.plugin.processors.sleigh.ParserWalker;
import ghidra.program.model.mem.MemoryAccessException;

# /**
# * 
# *
# * Form new expression by taking twos complement of a PatternExpression
# */
public class MinusExpression extends UnaryExpression {

	/* (non-Javadoc)
	 * @see ghidra.app.plugin.processors.sleigh.expression.PatternExpression#getValue(ghidra.app.plugin.processors.sleigh.ParserWalker)
	 */
	@Override
	public long getValue(ParserWalker walker) throws MemoryAccessException {
		long val = getUnary().getValue(walker);
		return -val;
	}

	@Override
	public String toString() {
		return "-(" + getUnary() + ")";
	}
}
