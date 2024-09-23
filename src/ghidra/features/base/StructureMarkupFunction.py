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
package ghidra.app.util.bin.format.golang.structmapping;



import ghidra.util.exception.CancelledException;

/**
 * Function that decorates a Ghidra structure 
 * 
 * @param <T> structure mapped class type
 */
public interface StructureMarkupFunction<T> {

	/**
	 * Decorates the specified structure.
	 * 
	 * @param context {@link StructureContext}
	 * @param markupSession state and methods to assist marking up the program 
	 * @throws IOException thrown if error performing the markup
	 * @throws CancelledException 
	 */
	void markupStructure(StructureContext<T> context, MarkupSession markupSession)
			throws IOException, CancelledException;
}
